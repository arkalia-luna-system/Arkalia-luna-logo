"""🤖 BBIA Palette Module
Palette de couleurs officielle BBIA pour intégration future
Préparé pour intégration avec /Volumes/T7/bbia-branding/ (quand déplacé)
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class BBIAColorPalette:
    """Palette de couleurs officielle BBIA Premium"""

    # Couleurs principales
    PRIMARY_BLUE: str = "#0066FF"  # BBIA Blue - Accents, logo
    SECONDARY_WHITE: str = "#FFFFFF"  # BBIA White - Fond, robot body
    TERTIARY_GRAY: str = "#2C2C2C"  # BBIA Gray - Texte, éléments secondaires

    # Variantes
    BLUE_LIGHT: str = "#3399FF"  # Light blue - Hover, états actifs
    BLUE_DARK: str = "#0052CC"  # Dark blue
    GRAY_LIGHT: str = "#E5E5E5"  # Light gray - Bordures subtiles
    GRAY_DARK: str = "#1A1A1A"  # Dark gray - Texte sur fond clair
    WHITE_OFF: str = "#FAFAFA"  # Off-white - Fonds subtils

    def to_dict(self) -> Dict[str, str]:
        """Convertit la palette en dictionnaire"""
        return {
            "primary": self.PRIMARY_BLUE,
            "secondary": self.SECONDARY_WHITE,
            "tertiary": self.TERTIARY_GRAY,
            "blue_light": self.BLUE_LIGHT,
            "blue_dark": self.BLUE_DARK,
            "gray_light": self.GRAY_LIGHT,
            "gray_dark": self.GRAY_DARK,
            "white_off": self.WHITE_OFF,
        }

    def get_rgb(self, color_hex: str) -> tuple[int, int, int]:
        """Convertit hex en RGB"""
        color_hex = color_hex.lstrip("#")
        return tuple(int(color_hex[i : i + 2], 16) for i in (0, 2, 4))

    def get_primary_rgb(self) -> tuple[int, int, int]:
        """Retourne le RGB du bleu primaire"""
        return self.get_rgb(self.PRIMARY_BLUE)

    def get_secondary_rgb(self) -> tuple[int, int, int]:
        """Retourne le RGB du blanc secondaire"""
        return self.get_rgb(self.SECONDARY_WHITE)

    def get_tertiary_rgb(self) -> tuple[int, int, int]:
        """Retourne le RGB du gris tertiaire"""
        return self.get_rgb(self.TERTIARY_GRAY)


# Instance globale de la palette BBIA
BBIA_PALETTE = BBIAColorPalette()


def get_bbia_palette() -> BBIAColorPalette:
    """Retourne l'instance globale de la palette BBIA"""
    return BBIA_PALETTE
