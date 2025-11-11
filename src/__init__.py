"""🌙 Arkalia-LUNA Logo Generator.

Package Python pour la génération de logos techno-mystiques
avec optimisations de performance.
"""

from typing import Any

__version__ = "2.0.0"  # Version majeure avec optimisations
__author__ = "Arkalia-LUNA Team"
__email__ = "team@arkalia-luna.dev"

# Import des classes principales
from .advanced_logo_generator import AdvancedArkaliaLunaLogo
from .ai_moon_generator import AIMoonLogoGenerator

# Import paresseux pour éviter RuntimeWarning lors de l'exécution via python -m src.cli
# from .cli import cli
from .dashboard_generator import DashboardLogoGenerator
from .generator_factory import (
    LogoGeneratorFactory,
    benchmark_all_generators,
    create_logo_generator,
)
from .logo_generator import ArkaliaLunaLogo
from .realism_max_generator import RealismMaxLogoGenerator
from .simple_advanced_generator import SimpleAdvancedLogoGenerator
from .svg_builder import SVGBuilder
from .svg_builder_advanced import AdvancedSVGBuilder
from .svg_builder_ai_moon import AIMoonSVGBuilder
from .svg_builder_dashboard import DashboardSVGBuilder
from .svg_builder_realism_max import RealismMaxSVGBuilder
from .svg_builder_simple_advanced import SimpleAdvancedSVGBuilder
from .svg_builder_ultimate import UltimateSVGBuilder
from .svg_builder_ultra_max import UltraMaxSVGBuilder
from .ultimate_generator import UltimateLogoGenerator
from .ultra_max_generator import UltraMaxLogoGenerator
from .variants import ColorScheme, LogoVariant, LogoVariants, VariantType


# Fonction de création rapide pour compatibilité
def create_generator(generator_type: str = "default", **kwargs: Any) -> ArkaliaLunaLogo:
    """Fonction de compatibilité pour créer rapidement un générateur."""
    return create_logo_generator(generator_type, **kwargs)


# Configuration du package avec toutes les fonctionnalités
__all__ = sorted(
    [
        # Classes principales
        "AdvancedArkaliaLunaLogo",
        "AIMoonLogoGenerator",
        "AIMoonSVGBuilder",
        "AdvancedSVGBuilder",
        "ArkaliaLunaLogo",
        "ColorScheme",
        "DashboardLogoGenerator",
        "DashboardSVGBuilder",
        "LogoVariant",
        "LogoVariants",
        "RealismMaxLogoGenerator",
        "RealismMaxSVGBuilder",
        "SimpleAdvancedLogoGenerator",
        "SimpleAdvancedSVGBuilder",
        "SVGBuilder",
        "UltimateLogoGenerator",  # 🌟 NOUVEAU : Générateur ULTIME cosmique
        "UltimateSVGBuilder",  # 🌟 NOUVEAU : Builder ULTIME cosmique
        "UltraMaxLogoGenerator",
        "UltraMaxSVGBuilder",
        "VariantType",
        # Factory et utilitaires
        "LogoGeneratorFactory",
        "benchmark_all_generators",
        "create_generator",
        "create_logo_generator",
        # CLI (import paresseux)
        "cli",
    ]
)


# Import paresseux pour éviter RuntimeWarning
def __getattr__(name: str) -> Any:
    """Import paresseux pour le module CLI"""
    if name == "cli":
        from .cli import cli as cli_module

        return cli_module
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
