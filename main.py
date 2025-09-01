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
from fastapi import BackgroundTasks, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, PlainTextResponse
from pydantic import BaseModel, Field

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
        self.logo_generation_count = 0
        self.error_count = 0
        self.last_generation_time = 0.0

    def increment_request(self):
        self.request_count += 1

    def increment_logo_generation(self, duration: float):
        self.logo_generation_count += 1
        self.last_generation_time = duration

    def increment_error(self):
        self.error_count += 1

    def get_metrics(self) -> str:
        uptime = time.time() - self.start_time
        return f"""# HELP arkalia_luna_uptime_seconds Total uptime in seconds
# TYPE arkalia_luna_uptime_seconds counter
arkalia_luna_uptime_seconds {uptime}

# HELP arkalia_luna_requests_total Total number of requests
# TYPE arkalia_luna_requests_total counter
arkalia_luna_requests_total {self.request_count}

# HELP arkalia_luna_logo_generations_total Total number of logo generations
# TYPE arkalia_luna_logo_generations_total counter
arkalia_luna_logo_generations_total {self.logo_generation_count}

# HELP arkalia_luna_errors_total Total number of errors
# TYPE arkalia_luna_errors_total counter
arkalia_luna_errors_total {self.error_count}

# HELP arkalia_luna_last_generation_duration_seconds Duration of last logo generation
# TYPE arkalia_luna_last_generation_duration_seconds gauge
arkalia_luna_last_generation_duration_seconds {self.last_generation_time}

# HELP arkalia_luna_health_status Health status (1=healthy, 0=unhealthy)
# TYPE arkalia_luna_health_status gauge
arkalia_luna_health_status 1
"""


# Instance globale des métriques
metrics = PrometheusMetrics()

# Initialisation de l'application FastAPI
app = FastAPI(
    title="Arkalia-LUNA Logo Generator API",
    description="API pour la génération de logos techno-mystiques",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

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
        metrics.increment_request()
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
        metrics.increment_request()
        return metrics.get_metrics()
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des métriques: {e}")
        metrics.increment_error()
        return f"# ERROR: {str(e)}\n"


@app.get("/variants", response_model=List[str])
async def get_available_variants():
    """Récupérer toutes les variantes disponibles"""
    try:
        variants = LogoVariants()
        return list(variants.get_all_variants().keys())
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des variantes: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.get("/generators", response_model=List[str])
async def get_available_generators():
    """Récupérer tous les types de générateurs disponibles"""
    try:
        if generator_factory and hasattr(generator_factory, "get_available_generators"):
            return generator_factory.get_available_generators()
        return ["simple"]
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des générateurs: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.post("/generate", response_model=LogoGenerationResponse)
async def generate_logo(
    request: LogoGenerationRequest, background_tasks: BackgroundTasks
):
    """Générer un logo selon les paramètres spécifiés"""
    try:
        metrics.increment_request()
        start_time = time.time()

        if not logo_generator:
            raise HTTPException(status_code=500, detail="Générateur non initialisé")

        logger.info(
            f"🎨 Génération de logo: {request.variant} - {request.size}px - {request.generator_type}"
        )

        # Validation des paramètres
        if request.size not in [50, 100, 200, 500]:
            raise HTTPException(
                status_code=400,
                detail="Taille invalide. Utilisez: 50, 100, 200, ou 500",
            )

        # Génération du logo
        start_time = time.time()

        # Utilisation du générateur approprié
        if request.generator_type != "simple":
            if not generator_factory:
                raise HTTPException(
                    status_code=500, detail="Factory de générateurs non initialisée"
                )
            generator = generator_factory.create_generator(request.generator_type)
            if generator:
                # Logique spécifique au générateur
                file_path = generator.generate_svg_logo(
                    variant_name=request.variant, size=request.size
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail=f"Type de générateur '{request.generator_type}' non supporté",
                )
        else:
            # Générateur simple par défaut
            file_path = logo_generator.generate_svg_logo(
                variant_name=request.variant, size=request.size
            )

        generation_time = time.time() - start_time
        metrics.increment_logo_generation(generation_time)

        # Le fichier est déjà créé par le générateur
        filename = file_path.name

        # Nettoyage en arrière-plan
        background_tasks.add_task(cleanup_old_files)

        logger.info(f"✅ Logo généré avec succès: {filename} en {generation_time:.2f}s")

        return LogoGenerationResponse(
            success=True,
            message=f"Logo {request.variant} généré avec succès",
            file_path=str(file_path),
            download_url=f"/download/{filename}",
            generation_time=generation_time,
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erreur lors de la génération du logo: {e}")
        metrics.increment_error()
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
