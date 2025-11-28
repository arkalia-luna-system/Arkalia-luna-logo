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
        """Initialise toutes les variantes BBIA disponibles"""
        return {
            BBIAVariantType.SERENITY.value: BBIAVariant(
                variant_type=BBIAVariantType.SERENITY,
                name="🤖 BBIA Sérénité",
                description="Robot calme, yeux doux, halo bleu apaisant",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent="#60a5fa",  # Blue light
                    glow="#a5f3fc",  # Cyan soft
                ),
                animation_speed=1.0,
                glow_intensity=0.7,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.POWER.value: BBIAVariant(
                variant_type=BBIAVariantType.POWER,
                name="⚡ BBIA Puissance",
                description="Robot énergique, yeux brillants, halo électrique",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent="#7c3aed",  # Violet
                    glow="#a855f7",  # Violet clair
                ),
                animation_speed=1.5,
                glow_intensity=0.9,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.MYSTERY.value: BBIAVariant(
                variant_type=BBIAVariantType.MYSTERY,
                name="🔮 BBIA Mystère",
                description="Robot mystérieux, yeux sombres, halo violet",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent="#4c1d95",  # Violet sombre
                    glow="#581c87",  # Violet mystique
                ),
                animation_speed=0.8,
                glow_intensity=0.6,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.AWAKENING.value: BBIAVariant(
                variant_type=BBIAVariantType.AWAKENING,
                name="✨ BBIA Éveil",
                description="Robot éveillé, yeux lumineux, halo doré",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent="#059669",  # Vert émeraude
                    glow="#10b981",  # Vert clair
                ),
                animation_speed=1.2,
                glow_intensity=0.8,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.CREATIVE.value: BBIAVariant(
                variant_type=BBIAVariantType.CREATIVE,
                name="🎇 BBIA Créatif",
                description="Robot créatif, yeux multicolores, halo arc-en-ciel",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent="#06b6d4",  # Cyan vif
                    glow="#f59e0b",  # Jaune doré
                ),
                animation_speed=2.0,
                glow_intensity=1.0,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.RAINY.value: BBIAVariant(
                variant_type=BBIAVariantType.RAINY,
                name="🌧️ BBIA Pluie",
                description="Robot mélancolique, gouttes sur le visage, halo gris",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent="#6b7280",  # Gris moyen
                    glow="#d1d5db",  # Gris très clair
                ),
                animation_speed=0.6,
                glow_intensity=0.4,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.STORMY.value: BBIAVariant(
                variant_type=BBIAVariantType.STORMY,
                name="⚡ BBIA Orage",
                description="Robot colérique, éclairs dans les yeux, halo sombre",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent="#4c1d95",  # Violet sombre
                    glow="#7c3aed",  # Violet éclair
                ),
                animation_speed=3.0,
                glow_intensity=1.2,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.EXPLOSIVE.value: BBIAVariant(
                variant_type=BBIAVariantType.EXPLOSIVE,
                name="💥 BBIA Explosif",
                description="Robot explosif, particules autour, halo rouge",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent="#ea580c",  # Orange vif
                    glow="#f97316",  # Orange éclatant
                ),
                animation_speed=2.5,
                glow_intensity=1.5,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.SUNNY.value: BBIAVariant(
                variant_type=BBIAVariantType.SUNNY,
                name="☀️ BBIA Ensoleillé",
                description="Robot joyeux, rayons de soleil, halo jaune",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent="#f97316",  # Orange chaud
                    glow="#fef3c7",  # Jaune très clair
                ),
                animation_speed=1.8,
                glow_intensity=1.1,
                halo_enabled=True,
                particles_enabled=True,
            ),
            BBIAVariantType.SNOWY.value: BBIAVariant(
                variant_type=BBIAVariantType.SNOWY,
                name="❄️ BBIA Neige",
                description="Robot serein, flocons autour, halo blanc",
                colors=BBIAColorScheme(
                    primary=BBIA_PALETTE.LOGO_BACKGROUND,  # #008181
                    secondary=BBIA_PALETTE.LOGO_BODY_WHITE,  # #FFFFFF
                    accent="#e2e8f0",  # Gris très clair
                    glow="#f1f5f9",  # Blanc cassé
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
