"""
🤖 BBIA Variants Module
Variantes émotionnelles pour les logos BBIA
Adaptation des variantes Arkalia-LUNA pour BBIA avec palette officielle
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict

from .bbia_palette import BBIA_PALETTE


class BBIAVariantType(Enum):
    """Types de variantes BBIA disponibles"""

    SERENITY = "serenity"
    POWER = "power"
    MYSTERY = "mystery"
    AWAKENING = "awakening"
    CREATIVE = "creative"
    RAINY = "rainy"
    STORMY = "stormy"
    EXPLOSIVE = "explosive"
    SUNNY = "sunny"
    SNOWY = "snowy"


@dataclass
class BBIAColorScheme:
    """Schéma de couleurs pour une variante BBIA"""

    primary: str
    secondary: str
    accent: str
    glow: str

    def to_dict(self) -> Dict[str, str]:
        """Convertit en dictionnaire"""
        return {
            "primary": self.primary,
            "secondary": self.secondary,
            "accent": self.accent,
            "glow": self.glow,
        }


@dataclass
class BBIAVariant:
    """Définition complète d'une variante de logo BBIA"""

    variant_type: BBIAVariantType
    name: str
    description: str
    colors: BBIAColorScheme
    animation_speed: float
    glow_intensity: float
    halo_enabled: bool = True
    particles_enabled: bool = True

    def to_dict(self) -> Dict[str, Any]:
        """Convertit en dictionnaire"""
        return {
            "variant_type": self.variant_type.value,
            "name": self.name,
            "description": self.description,
            "colors": self.colors.to_dict(),
            "animation_speed": self.animation_speed,
            "glow_intensity": self.glow_intensity,
            "halo_enabled": self.halo_enabled,
            "particles_enabled": self.particles_enabled,
        }


class BBIAVariants:
    """Gestionnaire des variantes de logo BBIA"""

    def __init__(self) -> None:
        self._variants = self._initialize_variants()

    def _initialize_variants(self) -> Dict[str, BBIAVariant]:
        """Initialise toutes les variantes BBIA disponibles avec palette officielle"""
        return {
            BBIAVariantType.SERENITY.value: BBIAVariant(
                variant_type=BBIAVariantType.SERENITY,
                name="🤖 BBIA Sérénité",
                description="Robot calme, fond bleu apaisant, ondes douces",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    # #0066FF - Bleu BBIA officiel
                    accent=BBIA_PALETTE.BRANDING_PRIMARY_BLUE,
                    glow=BBIA_PALETTE.BRANDING_BLUE_LIGHT,  # #3399FF - Bleu clair BBIA
                ),
                animation_speed=1.0,
                glow_intensity=0.7,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.POWER.value: BBIAVariant(
                variant_type=BBIAVariantType.POWER,
                name="⚡ BBIA Puissance",
                description="Robot énergique, fond bleu électrique, ondes rapides",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent=BBIA_PALETTE.BRANDING_BLUE_DARK,  # #0052CC - Bleu foncé BBIA
                    glow=BBIA_PALETTE.BRANDING_PRIMARY_BLUE,  # #0066FF - Bleu BBIA
                ),
                animation_speed=1.5,
                glow_intensity=0.9,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.MYSTERY.value: BBIAVariant(
                variant_type=BBIAVariantType.MYSTERY,
                name="🔮 BBIA Mystère",
                description="Robot mystérieux, fond gris sombre, ondes irrégulières",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent=BBIA_PALETTE.BRANDING_TERTIARY_GRAY,  # #2C2C2C - Gris BBIA
                    glow=BBIA_PALETTE.BRANDING_GRAY_DARK,  # #1A1A1A - Gris foncé BBIA
                ),
                animation_speed=0.8,
                glow_intensity=0.6,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.AWAKENING.value: BBIAVariant(
                variant_type=BBIAVariantType.AWAKENING,
                name="✨ BBIA Éveil",
                description="Robot éveillé, fond bleu lumineux, ondes rayonnantes",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    # #3399FF - Bleu clair BBIA
                    accent=BBIA_PALETTE.BRANDING_BLUE_LIGHT,
                    glow=BBIA_PALETTE.BRANDING_PRIMARY_BLUE,  # #0066FF - Bleu BBIA
                ),
                animation_speed=1.2,
                glow_intensity=0.8,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.CREATIVE.value: BBIAVariant(
                variant_type=BBIAVariantType.CREATIVE,
                name="🎇 BBIA Créatif",
                description="Robot créatif, fond bleu vif, ondes multicolores",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent=BBIA_PALETTE.BRANDING_PRIMARY_BLUE,  # #0066FF - Bleu BBIA
                    glow=BBIA_PALETTE.BRANDING_BLUE_LIGHT,  # #3399FF - Bleu clair BBIA
                ),
                animation_speed=2.0,
                glow_intensity=1.0,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.RAINY.value: BBIAVariant(
                variant_type=BBIAVariantType.RAINY,
                name="🌧️ BBIA Pluie",
                description="Robot mélancolique, fond gris, ondes lentes",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    # #E5E5E5 - Gris clair BBIA
                    accent=BBIA_PALETTE.BRANDING_GRAY_LIGHT,
                    glow=BBIA_PALETTE.BRANDING_TERTIARY_GRAY,  # #2C2C2C - Gris BBIA
                ),
                animation_speed=0.6,
                glow_intensity=0.4,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.STORMY.value: BBIAVariant(
                variant_type=BBIAVariantType.STORMY,
                name="⚡ BBIA Orage",
                description="Robot colérique, fond bleu foncé, ondes électriques",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent=BBIA_PALETTE.BRANDING_BLUE_DARK,  # #0052CC - Bleu foncé BBIA
                    glow=BBIA_PALETTE.BRANDING_PRIMARY_BLUE,  # #0066FF - Bleu BBIA
                ),
                animation_speed=3.0,
                glow_intensity=1.2,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.EXPLOSIVE.value: BBIAVariant(
                variant_type=BBIAVariantType.EXPLOSIVE,
                name="💥 BBIA Explosif",
                description="Robot explosif, fond bleu intense, ondes radiales",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent=BBIA_PALETTE.BRANDING_PRIMARY_BLUE,  # #0066FF - Bleu BBIA
                    glow=BBIA_PALETTE.BRANDING_BLUE_LIGHT,  # #3399FF - Bleu clair BBIA
                ),
                animation_speed=2.5,
                glow_intensity=1.5,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.SUNNY.value: BBIAVariant(
                variant_type=BBIAVariantType.SUNNY,
                name="☀️ BBIA Ensoleillé",
                description="Robot joyeux, fond bleu clair, ondes lumineuses",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    # #3399FF - Bleu clair BBIA
                    accent=BBIA_PALETTE.BRANDING_BLUE_LIGHT,
                    glow=BBIA_PALETTE.BRANDING_PRIMARY_BLUE,  # #0066FF - Bleu BBIA
                ),
                animation_speed=1.8,
                glow_intensity=1.1,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.SNOWY.value: BBIAVariant(
                variant_type=BBIAVariantType.SNOWY,
                name="❄️ BBIA Neige",
                description="Robot serein, fond blanc cassé, ondes douces",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    # #FAFAFA - Blanc cassé BBIA
                    accent=BBIA_PALETTE.BRANDING_WHITE_OFF,
                    glow=BBIA_PALETTE.BRANDING_GRAY_LIGHT,  # #E5E5E5 - Gris clair BBIA
                ),
                animation_speed=0.4,
                glow_intensity=0.5,
                halo_enabled=True,
                particles_enabled=True,
            ),
        }

    def get_variant(self, variant_name: str) -> BBIAVariant:
        """Récupère une variante par son nom"""
        variant = self._variants.get(variant_name.lower())
        if variant is None:
            raise ValueError(
                f"Variante BBIA '{variant_name}' non trouvée. "
                f"Variantes disponibles : {', '.join(self._variants.keys())}"
            )
        return variant

    def get_all_variants(self) -> Dict[str, BBIAVariant]:
        """Retourne toutes les variantes"""
        return self._variants.copy()

    def list_variant_names(self) -> list[str]:
        """Liste tous les noms de variantes"""
        return list(self._variants.keys())


# Instance globale des variantes BBIA
BBIA_VARIANTS = BBIAVariants()


def get_bbia_variant(variant_name: str) -> BBIAVariant:
    """Retourne une variante BBIA par son nom"""
    return BBIA_VARIANTS.get_variant(variant_name)


def get_all_bbia_variants() -> Dict[str, BBIAVariant]:
    """Retourne toutes les variantes BBIA"""
    return BBIA_VARIANTS.get_all_variants()
