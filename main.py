"""
🌙 API Web pour Arkalia-LUNA Logo Generator
API FastAPI pour la génération de logos via interface web
"""

import logging
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import uvicorn
from fastapi import BackgroundTasks, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, PlainTextResponse
from pydantic import BaseModel, Field
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

try:
    from src.generator_factory import LogoGeneratorFactory
    from src.logo_generator import ArkaliaLunaLogo
    from src.variants import LogoVariants
except ImportError as e:
    print(f"Erreur d'import: {e}")
    ArkaliaLunaLogo = None  # type: ignore
    LogoGeneratorFactory = None  # type: ignore
    LogoVariants = None  # type: ignore

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Métriques Prometheus
class PrometheusMetrics:
    def __init__(self):
        self.start_time = time.time()
        self.request_count = 0
        self.request_count_by_route: Dict[str, int] = {}
        self.response_status_by_route: Dict[str, Dict[int, int]] = {}
        self.logo_generation_count = 0
        self.logo_generation_count_by_label: Dict[str, int] = {}
        self.total_generation_time = 0.0
        self.error_count = 0
        self.last_generation_time = 0.0
        # Histogram (seconds)
        self.duration_buckets = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]
        self.bucket_counts: Dict[float, int] = dict.fromkeys(self.duration_buckets, 0)
        self.bucket_inf_count = 0
        self.hist_count = 0
        self.hist_sum = 0.0

    def increment_request(self, route: Optional[str] = None) -> None:
        self.request_count += 1
        if route:
            self.request_count_by_route[route] = (
                self.request_count_by_route.get(route, 0) + 1
            )

    def increment_logo_generation(
        self,
        duration: float,
        variant: Optional[str] = None,
        generator: Optional[str] = None,
    ) -> None:
        self.logo_generation_count += 1
        self.last_generation_time = duration
        self.total_generation_time += duration
        # label key format: variant|generator
        label_key = f"variant={variant or 'unknown'},generator={generator or 'simple'}"
        self.logo_generation_count_by_label[label_key] = (
            self.logo_generation_count_by_label.get(label_key, 0) + 1
        )

    def increment_error(self) -> None:
        self.error_count += 1

    def observe_generation_duration(self, duration: float) -> None:
        placed = False
        for b in self.duration_buckets:
            if duration <= b:
                self.bucket_counts[b] = self.bucket_counts.get(b, 0) + 1
                placed = True
                break
        if not placed:
            self.bucket_inf_count += 1
        self.hist_sum += duration
        self.hist_count += 1

    def record_response_status(self, route: str, status_code: int) -> None:
        by_status = self.response_status_by_route.setdefault(route, {})
        by_status[status_code] = by_status.get(status_code, 0) + 1

    def get_metrics(self) -> str:
        uptime = time.time() - self.start_time
        lines: List[str] = []
        # Uptime
        lines.append("# HELP arkalia_luna_uptime_seconds Total uptime in seconds")
        lines.append("# TYPE arkalia_luna_uptime_seconds counter")
        lines.append(f"arkalia_luna_uptime_seconds {uptime}")
        lines.append("")
        # Requests total
        lines.append("# HELP arkalia_luna_requests_total Total number of requests")
        lines.append("# TYPE arkalia_luna_requests_total counter")
        lines.append(f"arkalia_luna_requests_total {self.request_count}")
        # Requests by route (labels)
        for route, count in self.request_count_by_route.items():
            lines.append(f'arkalia_luna_requests_total{{route="{route}"}} {count}')
        lines.append("")
        # Responses by route and status
        lines.append(
            "# HELP arkalia_luna_responses_total Total responses by status and route"
        )
        lines.append("# TYPE arkalia_luna_responses_total counter")
        for route, by_status in self.response_status_by_route.items():
            for status, count in by_status.items():
                lines.append(
                    f'arkalia_luna_responses_total{{route="{route}",status_code="{status}"}} {count}'
                )
        lines.append("")
        # Generations total
        lines.append(
            "# HELP arkalia_luna_logo_generations_total Total number of logo generations"
        )
        lines.append("# TYPE arkalia_luna_logo_generations_total counter")
        lines.append(
            f"arkalia_luna_logo_generations_total {self.logo_generation_count}"
        )
        # Generations by labels (variant, generator)
        for label_key, count in self.logo_generation_count_by_label.items():
            # label_key is already key=value pairs separated by comma
            lines.append(f"arkalia_luna_logo_generations_total{{{label_key}}} {count}")
        lines.append("")
        # Errors
        lines.append("# HELP arkalia_luna_errors_total Total number of errors")
        lines.append("# TYPE arkalia_luna_errors_total counter")
        lines.append(f"arkalia_luna_errors_total {self.error_count}")
        lines.append("")
        # Last and average duration
        lines.append(
            "# HELP arkalia_luna_last_generation_duration_seconds Duration of last logo generation"
        )
        lines.append("# TYPE arkalia_luna_last_generation_duration_seconds gauge")
        lines.append(
            f"arkalia_luna_last_generation_duration_seconds {self.last_generation_time}"
        )
        avg = (
            self.total_generation_time / self.logo_generation_count
            if self.logo_generation_count
            else 0.0
        )
        lines.append(
            "# HELP arkalia_luna_avg_generation_duration_seconds Average logo generation duration"
        )
        lines.append("# TYPE arkalia_luna_avg_generation_duration_seconds gauge")
        lines.append(f"arkalia_luna_avg_generation_duration_seconds {avg}")
        lines.append("")
        # Histogram
        lines.append(
            "# HELP arkalia_luna_generation_duration_seconds Logo generation duration histogram"
        )
        lines.append("# TYPE arkalia_luna_generation_duration_seconds histogram")
        cumulative = 0
        for b in sorted(self.duration_buckets):
            cumulative += self.bucket_counts.get(b, 0)
            lines.append(
                f'arkalia_luna_generation_duration_seconds_bucket{{le="{b}"}} {cumulative}'
            )
        lines.append(
            f'arkalia_luna_generation_duration_seconds_bucket{{le="+Inf"}} {cumulative + self.bucket_inf_count}'
        )
        lines.append(f"arkalia_luna_generation_duration_seconds_sum {self.hist_sum}")
        lines.append(
            f"arkalia_luna_generation_duration_seconds_count {self.hist_count}"
        )
        lines.append("")
        # Health
        lines.append(
            "# HELP arkalia_luna_health_status Health status (1=healthy, 0=unhealthy)"
        )
        lines.append("# TYPE arkalia_luna_health_status gauge")
        lines.append("arkalia_luna_health_status 1")
        return "\n".join(lines) + "\n"


# Instance globale des métriques
metrics = PrometheusMetrics()

# Rate limiter
limiter = Limiter(key_func=get_remote_address)

# Initialisation de l'application FastAPI
app = FastAPI(
    title="Arkalia-LUNA Logo Generator API",
    description="API pour la génération de logos techno-mystiques",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configuration du rate limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Modèles Pydantic pour l'API
class LogoGenerationRequest(BaseModel):
    variant: str = Field(
        ...,
        description="Variante du logo (serenity, power, mystery, awakening, creative)",
    )
    size: int = Field(200, description="Taille du logo en pixels")
    generator_type: str = Field(
        "simple",
        description="Type de générateur (simple, advanced, ultimate, ultra_max, realism_max, ai_moon, dashboard)",
    )


class LogoGenerationResponse(BaseModel):
    success: bool
    message: str
    file_path: Optional[str] = None
    download_url: Optional[str] = None
    generation_time: Optional[float] = None


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str
    environment: str


# Variables globales
logo_generator: Optional[ArkaliaLunaLogo] = None
generator_factory: Optional[LogoGeneratorFactory] = None


@app.on_event("startup")
async def startup_event():
    """Initialisation au démarrage de l'application"""
    global logo_generator, generator_factory

    try:
        # Initialisation du générateur de logos
        logo_generator = ArkaliaLunaLogo()
        generator_factory = LogoGeneratorFactory()

        # Création des répertoires nécessaires
        os.makedirs("exports", exist_ok=True)
        os.makedirs("cache", exist_ok=True)
        os.makedirs("logs", exist_ok=True)

        logger.info("🚀 Arkalia-LUNA Logo Generator API démarrée avec succès")

    except Exception as e:
        logger.error(f"❌ Erreur lors du démarrage: {e}")
        raise


@app.get("/", response_model=Dict[str, str])
async def root():
    """Endpoint racine"""
    return {
        "message": "🌙 Arkalia-LUNA Logo Generator API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Vérification de l'état de l'API"""
    try:
        metrics.increment_request(route="/health")
        return HealthResponse(
            status="healthy",
            timestamp=datetime.now(),
            version="1.0.0",
            environment=os.getenv("ENVIRONMENT", "development"),
        )
    except Exception as e:
        logger.error(f"Erreur lors de la vérification de santé: {e}")
        metrics.increment_error()
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.get("/metrics", response_class=PlainTextResponse)
async def prometheus_metrics():
    """Endpoint des métriques Prometheus"""
    try:
        metrics.increment_request(route="/metrics")
        return metrics.get_metrics()
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des métriques: {e}")
        metrics.increment_error()
        return f"# ERROR: {str(e)}\n"


@app.get("/variants", response_model=List[str])
async def get_available_variants():
    """Récupérer toutes les variantes disponibles"""
    try:
        metrics.increment_request(route="/variants")
        variants = LogoVariants()
        return list(variants.get_all_variants().keys())
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des variantes: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.get("/generators", response_model=List[str])
async def get_available_generators():
    """Récupérer tous les types de générateurs disponibles"""
    try:
        metrics.increment_request(route="/generators")
        if generator_factory and hasattr(generator_factory, "get_available_generators"):
            return generator_factory.get_available_generators()
        return ["simple"]
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des générateurs: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.post("/generate", response_model=LogoGenerationResponse)
@limiter.limit("100/minute")
async def generate_logo(
    request: Request,
    logo_request: LogoGenerationRequest,
    background_tasks: BackgroundTasks,
):
    """Générer un logo selon les paramètres spécifiés"""
    try:
        metrics.increment_request(route="/generate")
        start_time = time.time()

        if not logo_generator:
            raise HTTPException(status_code=500, detail="Générateur non initialisé")

        logger.info(
            f"🎨 Génération de logo: {logo_request.variant} - {logo_request.size}px - {logo_request.generator_type}"
        )

        # Validation des paramètres
        if logo_request.size not in [50, 100, 200, 500]:
            raise HTTPException(
                status_code=400,
                detail="Taille invalide. Utilisez: 50, 100, 200, ou 500",
            )

        # Génération du logo
        start_time = time.time()

        # Utilisation du générateur approprié
        if logo_request.generator_type != "simple":
            if not generator_factory:
                raise HTTPException(
                    status_code=500, detail="Factory de générateurs non initialisée"
                )
            generator = generator_factory.create_generator(logo_request.generator_type)
            if generator:
                # Logique spécifique au générateur
                file_path = generator.generate_svg_logo(
                    variant_name=logo_request.variant, size=logo_request.size
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail=f"Type de générateur '{logo_request.generator_type}' non supporté",
                )
        else:
            # Générateur simple par défaut
            file_path = logo_generator.generate_svg_logo(
                variant_name=logo_request.variant, size=logo_request.size
            )

        generation_time = time.time() - start_time
        metrics.increment_logo_generation(
            generation_time,
            variant=logo_request.variant,
            generator=logo_request.generator_type,
        )
        metrics.observe_generation_duration(generation_time)

        # Le fichier est déjà créé par le générateur
        filename = file_path.name

        # Nettoyage en arrière-plan
        background_tasks.add_task(cleanup_old_files)

        logger.info(f"✅ Logo généré avec succès: {filename} en {generation_time:.2f}s")

        return LogoGenerationResponse(
            success=True,
            message=f"Logo {logo_request.variant} généré avec succès",
            file_path=str(file_path),
            download_url=f"/download/{filename}",
            generation_time=generation_time,
        )

    except HTTPException as http_exc:
        try:
            metrics.record_response_status(route="/generate", status_code=http_exc.status_code)  # type: ignore[attr-defined]
        except Exception:
            pass
        raise
    except Exception as e:
        logger.error(f"Erreur lors de la génération du logo: {e}")
        metrics.increment_error()
        metrics.record_response_status(route="/generate", status_code=500)
        raise HTTPException(
            status_code=500, detail=f"Erreur de génération: {str(e)}"
        ) from e


@app.get("/download/{filename}")
async def download_logo(filename: str):
    """Télécharger un logo généré"""
    try:
        file_path = Path("exports") / filename

        if not file_path.exists():
            raise HTTPException(status_code=404, detail="Fichier non trouvé")

        return FileResponse(
            path=file_path, filename=filename, media_type="image/svg+xml"
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erreur lors du téléchargement: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.get("/stats")
async def get_generation_stats():
    """Récupérer les statistiques de génération"""
    try:
        if logo_generator:
            stats = logo_generator.get_generation_stats()
            return {
                "total_generated": stats.get("total", 0),
                "variants_used": stats.get("variants", {}),
                "sizes_used": stats.get("sizes", {}),
                "last_generation": stats.get("last_generation"),
                "cache_hits": stats.get("cache_hits", 0),
            }
        return {"error": "Générateur non initialisé"}

    except Exception as e:
        logger.error(f"Erreur lors de la récupération des stats: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.delete("/cleanup")
async def cleanup_files():
    """Nettoyer les fichiers générés"""
    try:
        if logo_generator:
            count = logo_generator.cleanup_generated_files()
            return {"message": f"{count} fichiers nettoyés", "cleaned_count": count}
        return {"error": "Générateur non initialisé"}

    except Exception as e:
        logger.error(f"Erreur lors du nettoyage: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e


async def cleanup_old_files():
    """Nettoyage automatique des anciens fichiers"""
    try:
        # Supprimer les fichiers de plus de 24h
        exports_dir = Path("exports")
        if exports_dir.exists():
            current_time = datetime.now()
            for file_path in exports_dir.glob("*.svg"):
                if (
                    current_time - datetime.fromtimestamp(file_path.stat().st_mtime)
                ).days > 1:
                    file_path.unlink()
                    logger.info(f"🗑️ Fichier ancien supprimé: {file_path.name}")
    except Exception as e:
        logger.error(f"Erreur lors du nettoyage automatique: {e}")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
