"""
🌙 Generator Factory Module
Factory pattern optimisé pour la création des générateurs de logos
"""

from pathlib import Path
from typing import Any, Dict, Optional

from .advanced_logo_generator import AdvancedArkaliaLunaLogo
from .ai_logo_generator import AILogoGenerator
from .ai_moon_generator import AIMoonLogoGenerator
from .cosmic_logo_generator import CosmicLogoGenerator
from .dashboard_generator import DashboardLogoGenerator
from .hyper_ai_generator import HyperAIGenerator
from .logo_generator import ArkaliaLunaLogo
from .realism_max_generator import RealismMaxLogoGenerator
from .simple_advanced_generator import SimpleAdvancedLogoGenerator
from .ultimate_generator import UltimateLogoGenerator
from .ultra_max_generator import UltraMaxLogoGenerator


class LogoGeneratorFactory:
    """Factory optimisée pour la création des générateurs de logos"""

    # Cache des générateurs pour éviter la recréation (pattern Singleton)
    _generators_cache: Dict[str, ArkaliaLunaLogo] = {}

    # Mapping des types de générateurs - TOUS héritent maintenant de ArkaliaLunaLogo
    GENERATOR_TYPES = {
        "default": ArkaliaLunaLogo,
        "realism": RealismMaxLogoGenerator,
        "ultra_max": UltraMaxLogoGenerator,
        "simple_advanced": SimpleAdvancedLogoGenerator,
        "dashboard": DashboardLogoGenerator,
        "ai_moon": AIMoonLogoGenerator,  # ✅ Maintenant hérite correctement
        "advanced": AdvancedArkaliaLunaLogo,  # ✅ Maintenant hérite correctement
        "ultimate": UltimateLogoGenerator,  # 🌟 NOUVEAU : Générateur ULTIME cosmique
        "ai": AILogoGenerator,  # 🤖 NOUVEAU : Générateur IA avec Stable Diffusion
        "cosmic": CosmicLogoGenerator,  # 🌌 NOUVEAU : Générateur COSMIQUE avec sphères lumineuses
        "hyper_ai": HyperAIGenerator,  # 🧠 NOUVEAU : Générateur HYPER-IA avec ComfyUI + SDXL + ControlNet
    }

    @classmethod
    def create_generator(
        cls,
        generator_type: str = "default",
        output_dir: Optional[Path] = None,
        use_cache: bool = True,
    ) -> ArkaliaLunaLogo:
        """
        Crée un générateur de logo avec optimisations de performance

        Args:
            generator_type: Type de générateur à créer
            output_dir: Répertoire de sortie personnalisé
            use_cache: Utilise le cache pour éviter la recréation

        Returns:
            Instance du générateur configuré
        """
        # Validation du type de générateur
        if generator_type not in cls.GENERATOR_TYPES:
            raise ValueError(
                f"Type de générateur '{generator_type}' non reconnu. "
                f"Types disponibles: {list(cls.GENERATOR_TYPES.keys())}"
            )

        # Clé de cache unique
        cache_key = f"{generator_type}_{output_dir}"

        # Vérification du cache si activé
        if use_cache and cache_key in cls._generators_cache:
            return cls._generators_cache[cache_key]

        # Création du générateur
        generator_class = cls.GENERATOR_TYPES[generator_type]
        generator = generator_class(output_dir)

        # Mise en cache si activé
        if use_cache:
            cls._generators_cache[cache_key] = generator

        return generator

    @classmethod
    def get_available_generators(cls) -> Dict[str, Dict[str, str]]:
        """Retourne la liste des générateurs disponibles avec descriptions"""
        return {
            "default": {
                "name": "Générateur de base",
                "description": "Générateur de base standard",
            },
            "realism": {
                "name": "Realism Max",
                "description": "Générateur ultra-réaliste avec effets organiques",
            },
            "ultra_max": {
                "name": "Ultra Max",
                "description": "Générateur ULTRA-MAX avec effets exceptionnels",
            },
            "simple_advanced": {
                "name": "Simple Advanced",
                "description": "Générateur simple-advanced équilibré",
            },
            "dashboard": {
                "name": "Dashboard",
                "description": "Générateur dashboard optimisé interface",
            },
            "ai_moon": {
                "name": "AI Moon",
                "description": "Générateur IA avec lune vivante",
            },
            "advanced": {
                "name": "Advanced",
                "description": "Générateur avancé techno-mystique",
            },
            "ultimate": {
                "name": "Ultimate",
                "description": "🌟 Générateur ULTIME avec effets cosmiques extrêmes",
            },
            "ai": {
                "name": "AI Generator",
                "description": "🤖 Générateur IA avec Stable Diffusion local",
            },
            "cosmic": {
                "name": "Cosmic Sphere",
                "description": "🌌 Générateur COSMIQUE avec sphères lumineuses et réseaux neuronaux",
            },
            "hyper_ai": {
                "name": "Hyper AI",
                "description": "🧠 Générateur HYPER-IA avec ComfyUI + SDXL + ControlNet - INTELLIGENCE EXTRÊME",
            },
        }

    @classmethod
    def clear_cache(cls) -> None:
        """Vide le cache des générateurs"""
        cls._generators_cache.clear()

    @classmethod
    def get_cache_stats(cls) -> Dict[str, Any]:
        """Retourne les statistiques du cache"""
        return {
            "cached_generators": len(cls._generators_cache),
            "cache_keys": list(cls._generators_cache.keys()),
            "memory_usage": "Optimisé avec pattern Singleton",
        }

    @classmethod
    def create_all_generators(
        cls, output_dir: Optional[Path] = None
    ) -> Dict[str, ArkaliaLunaLogo]:
        """Crée tous les types de générateurs disponibles"""
        generators = {}

        for generator_type in cls.GENERATOR_TYPES:
            try:
                generators[generator_type] = cls.create_generator(
                    generator_type, output_dir, use_cache=False
                )
            except Exception as e:
                # Log de l'erreur mais continue avec les autres
                print(f"⚠️ Erreur création générateur '{generator_type}': {e}")
                continue

        return generators

    @classmethod
    def benchmark_generators(
        cls,
        output_dir: Optional[Path] = None,
        variant: str = "serenity",
        size: int = 200,
    ) -> Dict[str, float]:
        """Benchmark de performance de tous les générateurs"""
        import time

        results = {}
        generators = cls.create_all_generators(output_dir)

        for generator_type, generator in generators.items():
            try:
                start_time = time.time()

                # Test de génération - utilise la méthode standard maintenant
                if hasattr(generator, f"generate_{generator_type}_logo"):
                    method_name = f"generate_{generator_type}_logo"
                elif hasattr(
                    generator, f"generate_{generator_type.replace('_', '')}_logo"
                ):
                    method_name = f"generate_{generator_type.replace('_', '')}_logo"
                else:
                    # Fallback sur la méthode standard (maintenant disponible partout)
                    method_name = "generate_svg_logo"

                method = getattr(generator, method_name)
                method(variant, size)

                end_time = time.time()
                results[generator_type] = end_time - start_time

            except Exception as e:
                results[generator_type] = f"Erreur: {e}"

        return results


# Fonction utilitaire pour création rapide
def create_logo_generator(
    generator_type: str = "default", output_dir: Optional[Path] = None
) -> ArkaliaLunaLogo:
    """Fonction utilitaire pour créer rapidement un générateur"""
    return LogoGeneratorFactory.create_generator(generator_type, output_dir)


# Fonction utilitaire pour benchmark rapide
def benchmark_all_generators(output_dir: Optional[Path] = None) -> Dict[str, float]:
    """Fonction utilitaire pour benchmark rapide de tous les générateurs"""
    return LogoGeneratorFactory.benchmark_generators(output_dir)
