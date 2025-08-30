"""
🌙 Arkalia-LUNA Logo Generator
Package Python pour la génération de logos techno-mystiques
avec optimisations de performance
"""

__version__ = "2.0.0"  # Version majeure avec optimisations
__author__ = "Arkalia-LUNA Team"
__email__ = "team@arkalia-luna.dev"

# Import des classes principales
from .advanced_logo_generator import AdvancedArkaliaLunaLogo
from .ai_moon_generator import AIMoonLogoGenerator
from .cli import cli
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

# Configuration du package avec toutes les fonctionnalités
__all__ = [
    # Classes principales
    "ArkaliaLunaLogo",
    "LogoVariant",
    "LogoVariants",
    "VariantType",
    "ColorScheme",
    # Générateurs spécialisés
    "RealismMaxLogoGenerator",
    "UltraMaxLogoGenerator",
    "SimpleAdvancedLogoGenerator",
    "DashboardLogoGenerator",
    "AIMoonLogoGenerator",
    "AdvancedArkaliaLunaLogo",
    "UltimateLogoGenerator",  # 🌟 NOUVEAU : Générateur ULTIME cosmique
    # Builders SVG
    "SVGBuilder",
    "RealismMaxSVGBuilder",
    "UltraMaxSVGBuilder",
    "SimpleAdvancedSVGBuilder",
    "DashboardSVGBuilder",
    "AIMoonSVGBuilder",
    "AdvancedSVGBuilder",
    "UltimateSVGBuilder",  # 🌟 NOUVEAU : Builder ULTIME cosmique
    # Factory et utilitaires
    "LogoGeneratorFactory",
    "create_logo_generator",
    "benchmark_all_generators",
    # CLI
    "cli",
]


# Fonction de création rapide pour compatibilité
def create_generator(generator_type: str = "default", **kwargs):
    """Fonction de compatibilité pour créer rapidement un générateur"""
    return create_logo_generator(generator_type, **kwargs)


# Ajout à __all__ pour la compatibilité
__all__.append("create_generator")
