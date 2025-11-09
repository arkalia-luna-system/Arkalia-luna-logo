"""🌙 Logo Variants Module
Définition des variantes émotionnelles du logo Arkalia-LUNA
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict


class VariantType(Enum):
    """Types de variantes disponibles"""

    SERENITY = "serenity"
    POWER = "power"
    MYSTERY = "mystery"
    AWAKENING = "awakening"
    CREATIVE = "creative"
    # Nouvelles variantes émotionnelles dynamiques
    RAINY = "rainy"  # Pluie/Gris
    STORMY = "stormy"  # Orage/Colère
    EXPLOSIVE = "explosive"  # Vive/Explosion
    SUNNY = "sunny"  # Ensoleillé
    SNOWY = "snowy"  # Neige


@dataclass
class ColorScheme:
    """Schéma de couleurs pour une variante"""

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
class LogoVariant:
    """Définition complète d'une variante de logo"""

    variant_type: VariantType
    name: str
    description: str
    colors: ColorScheme
    animation_speed: float
    glow_intensity: float

    def to_dict(self) -> Dict[str, Any]:
        """Convertit en dictionnaire"""
        return {
            "variant_type": self.variant_type.value,
            "name": self.name,
            "description": self.description,
            "colors": self.colors.to_dict(),
            "animation_speed": self.animation_speed,
            "glow_intensity": self.glow_intensity,
        }


class LogoVariants:
    """Gestionnaire des variantes de logo"""

    def __init__(self):
        self._variants = self._initialize_variants()

    def _initialize_variants(self) -> Dict[str, LogoVariant]:
        """Initialise toutes les variantes disponibles"""
        return {
            VariantType.SERENITY.value: LogoVariant(
                variant_type=VariantType.SERENITY,
                name="🌙 Sérénité",
                description="Halo doux, pulsations lentes, ambiance calme et mystique",
                colors=ColorScheme(
                    primary="#1e3a8a",  # Bleu profond
                    secondary="#3b82f6",  # Bleu royal
                    accent="#06b6d4",  # Cyan
                    glow="#60a5fa",  # Bleu clair
                ),
                animation_speed=1.0,
                glow_intensity=0.7,
            ),
            VariantType.POWER.value: LogoVariant(
                variant_type=VariantType.POWER,
                name="⚡ Puissance",
                description="Halo vibrant, réseau accéléré, énergie intense",
                colors=ColorScheme(
                    primary="#1e40af",  # Bleu électrique
                    secondary="#7c3aed",  # Violet
                    accent="#ec4899",  # Rose vif
                    glow="#a855f7",  # Violet clair
                ),
                animation_speed=1.5,
                glow_intensity=0.9,
            ),
            VariantType.MYSTERY.value: LogoVariant(
                variant_type=VariantType.MYSTERY,
                name="🔮 Mystère",
                description="Brumes mouvantes, réseau irrégulier, ambiance mystérieuse",
                colors=ColorScheme(
                    primary="#312e81",  # Indigo profond
                    secondary="#4c1d95",  # Violet sombre
                    accent="#7c2d12",  # Brun mystérieux
                    glow="#581c87",  # Violet mystique
                ),
                animation_speed=0.8,
                glow_intensity=0.6,
            ),
            VariantType.AWAKENING.value: LogoVariant(
                variant_type=VariantType.AWAKENING,
                name="✨ Éveil/Sagesse",
                description="Halo rayonnant, Λ-core clair, sagesse éclairée",
                colors=ColorScheme(
                    primary="#0f766e",  # Vert-bleu profond
                    secondary="#059669",  # Vert émeraude
                    accent="#d97706",  # Orange doré
                    glow="#10b981",  # Vert clair
                ),
                animation_speed=1.2,
                glow_intensity=0.8,
            ),
            VariantType.CREATIVE.value: LogoVariant(
                variant_type=VariantType.CREATIVE,
                name="🎇 Énergie créative",
                description="Flux rapides, reflets multicolores, créativité débordante",
                colors=ColorScheme(
                    primary="#1e40af",  # Bleu créatif
                    secondary="#06b6d4",  # Cyan vif
                    accent="#ec4899",  # Rose créatif
                    glow="#f59e0b",  # Jaune doré
                ),
                animation_speed=2.0,
                glow_intensity=1.0,
            ),
            # Nouvelles variantes émotionnelles dynamiques
            VariantType.RAINY.value: LogoVariant(
                variant_type=VariantType.RAINY,
                name="🌧️ Pluie/Gris",
                description=(
                    "Gouttes de pluie, nuages gris, "
                    "ambiance mélancolique mais élégante"
                ),
                colors=ColorScheme(
                    primary="#4b5563",  # Gris foncé
                    secondary="#6b7280",  # Gris moyen
                    accent="#9ca3af",  # Gris clair
                    glow="#d1d5db",  # Gris très clair
                ),
                animation_speed=0.6,
                glow_intensity=0.4,
            ),
            VariantType.STORMY.value: LogoVariant(
                variant_type=VariantType.STORMY,
                name="⚡ Orage/Colère",
                description=(
                    "Éclairs zigzagants, nuages sombres, "
                    "énergie explosive et dynamique"
                ),
                colors=ColorScheme(
                    primary="#1f2937",  # Noir-gris
                    secondary="#4c1d95",  # Violet sombre
                    accent="#fbbf24",  # Jaune éclair
                    glow="#7c3aed",  # Violet éclair
                ),
                animation_speed=3.0,
                glow_intensity=1.2,
            ),
            VariantType.EXPLOSIVE.value: LogoVariant(
                variant_type=VariantType.EXPLOSIVE,
                name="💥 Vive/Explosion",
                description=(
                    "Particules explosives, feux d'artifice, "
                    "mouvement radial et énergique"
                ),
                colors=ColorScheme(
                    primary="#dc2626",  # Rouge vif
                    secondary="#ea580c",  # Orange vif
                    accent="#fbbf24",  # Jaune vif
                    glow="#f97316",  # Orange éclatant
                ),
                animation_speed=2.5,
                glow_intensity=1.5,
            ),
            VariantType.SUNNY.value: LogoVariant(
                variant_type=VariantType.SUNNY,
                name="☀️ Ensoleillé",
                description=(
                    "Rayons de soleil, chaleur et luminosité, "
                    "optimisme et énergie positive"
                ),
                colors=ColorScheme(
                    primary="#f59e0b",  # Jaune doré
                    secondary="#f97316",  # Orange chaud
                    accent="#fbbf24",  # Jaune clair
                    glow="#fef3c7",  # Jaune très clair
                ),
                animation_speed=1.8,
                glow_intensity=1.1,
            ),
            VariantType.SNOWY.value: LogoVariant(
                variant_type=VariantType.SNOWY,
                name="❄️ Neige",
                description=(
                    "Flocons qui tombent, froid et pureté, " "sérénité cristalline"
                ),
                colors=ColorScheme(
                    primary="#f8fafc",  # Blanc pur
                    secondary="#e2e8f0",  # Gris très clair
                    accent="#cbd5e1",  # Gris clair
                    glow="#f1f5f9",  # Blanc cassé
                ),
                animation_speed=0.4,
                glow_intensity=0.3,
            ),
        }

    def get_variant(self, variant_name: str) -> LogoVariant:
        """Récupère une variante par son nom"""
        if variant_name not in self._variants:
            available = list(self._variants.keys())
            raise ValueError(
                f"Variante '{variant_name}' non reconnue. "
                f"Variantes disponibles: {available}",
            )
        return self._variants[variant_name]

    def get_all_variants(self) -> Dict[str, LogoVariant]:
        """Récupère toutes les variantes"""
        return self._variants.copy()

    def list_variants(self) -> list:
        """Liste les noms des variantes disponibles"""
        return list(self._variants.keys())

    def validate_variant(self, variant_name: str) -> bool:
        """Valide qu'une variante existe"""
        return variant_name in self._variants

    def get_variant_info(self, variant_name: str) -> Dict[str, Any]:
        """Récupère les informations d'une variante au format dictionnaire"""
        variant = self.get_variant(variant_name)
        return variant.to_dict()
