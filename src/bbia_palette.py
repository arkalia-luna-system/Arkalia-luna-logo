"""
🤖 BBIA Palette Module
Palette de couleurs officielle BBIA pour intégration future
Préparé pour intégration avec /Volumes/T7/bbia-branding/ (quand déplacé)

⚠️ IMPORTANT : Distinction entre palette branding et couleurs réelles du logo
Source analyse : bbia_logo_vertical_v2.svg, bbia_mark_only_v2.svg,
bbia_logo_horizontal.svg
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class BBIAColorPalette:
    """
    Palette de couleurs officielle BBIA Premium

    ⚠️ ATTENTION : Il existe DEUX palettes distinctes :
    1. Palette Branding (couleurs de marque) : #0066FF, #2C2C2C
    2. Couleurs réelles du logo SVG : #CCCCCC, #000000, #008181
    """

    # ============================================================================
    # PALETTE BRANDING (couleurs de marque officielles)
    # ============================================================================
    # Couleurs principales branding
    BRANDING_PRIMARY_BLUE: str = "#0066FF"  # BBIA Blue - Accents, branding
    BRANDING_SECONDARY_WHITE: str = "#FFFFFF"  # BBIA White - Fond, robot body
    BRANDING_TERTIARY_GRAY: str = "#2C2C2C"  # BBIA Gray - Texte branding

    # Variantes branding
    BRANDING_BLUE_LIGHT: str = "#3399FF"  # Light blue - Hover, états actifs
    BRANDING_BLUE_DARK: str = "#0052CC"  # Dark blue
    BRANDING_GRAY_LIGHT: str = "#E5E5E5"  # Light gray - Bordures subtiles
    BRANDING_GRAY_DARK: str = "#1A1A1A"  # Dark gray - Texte sur fond clair
    BRANDING_WHITE_OFF: str = "#FAFAFA"  # Off-white - Fonds subtils

    # ============================================================================
    # COULEURS RÉELLES DU LOGO SVG (analysées depuis les fichiers finaux)
    # ============================================================================
    # Source : Analyse de bbia_logo_vertical_v2.svg, bbia_mark_only_v2.svg,
    # bbia_logo_horizontal.svg
    LOGO_BACKGROUND: str = "#008181"  # Turquoise/Teal - Fond carré derrière le robot
    LOGO_BODY_WHITE: str = "#FFFFFF"  # Blanc - Corps principal du robot
    LOGO_BODY_SHADES: tuple[str, ...] = (
        "#fefefe",
        "#f9f9f9",
        "#e6e6e6",
        "#d1d1d1",
        "#c7c7c7",
        "#cccccc",
    )  # Nuances de gris pour ombres/dégradés
    LOGO_EYES: str = "#CCCCCC"  # Gris clair - Yeux du robot (⚠️ PAS #0066FF !)
    LOGO_TEXT: str = "#000000"  # Noir - Texte "BBIA" (⚠️ PAS #2C2C2C !)

    def to_dict(self) -> Dict[str, str]:
        """Convertit la palette complète en dictionnaire"""
        return {
            # Branding
            "branding_primary": self.BRANDING_PRIMARY_BLUE,
            "branding_secondary": self.BRANDING_SECONDARY_WHITE,
            "branding_tertiary": self.BRANDING_TERTIARY_GRAY,
            "branding_blue_light": self.BRANDING_BLUE_LIGHT,
            "branding_blue_dark": self.BRANDING_BLUE_DARK,
            "branding_gray_light": self.BRANDING_GRAY_LIGHT,
            "branding_gray_dark": self.BRANDING_GRAY_DARK,
            "branding_white_off": self.BRANDING_WHITE_OFF,
            # Logo réel
            "logo_background": self.LOGO_BACKGROUND,
            "logo_body_white": self.LOGO_BODY_WHITE,
            "logo_eyes": self.LOGO_EYES,
            "logo_text": self.LOGO_TEXT,
        }

    def get_branding_dict(self) -> Dict[str, str]:
        """Retourne uniquement la palette branding"""
        return {
            "primary": self.BRANDING_PRIMARY_BLUE,
            "secondary": self.BRANDING_SECONDARY_WHITE,
            "tertiary": self.BRANDING_TERTIARY_GRAY,
            "blue_light": self.BRANDING_BLUE_LIGHT,
            "blue_dark": self.BRANDING_BLUE_DARK,
            "gray_light": self.BRANDING_GRAY_LIGHT,
            "gray_dark": self.BRANDING_GRAY_DARK,
            "white_off": self.BRANDING_WHITE_OFF,
        }

    def get_logo_dict(self) -> Dict[str, str]:
        """Retourne uniquement les couleurs réelles du logo"""
        return {
            "background": self.LOGO_BACKGROUND,
            "body_white": self.LOGO_BODY_WHITE,
            "eyes": self.LOGO_EYES,
            "text": self.LOGO_TEXT,
        }

    def get_rgb(self, color_hex: str) -> tuple[int, int, int]:
        """Convertit hex en RGB"""
        color_hex = color_hex.lstrip("#")
        if len(color_hex) != 6:
            raise ValueError(f"Code couleur hex invalide : {color_hex}")
        r = int(color_hex[0:2], 16)
        g = int(color_hex[2:4], 16)
        b = int(color_hex[4:6], 16)
        return (r, g, b)

    def get_branding_primary_rgb(self) -> tuple[int, int, int]:
        """Retourne le RGB du bleu primaire branding"""
        return self.get_rgb(self.BRANDING_PRIMARY_BLUE)

    def get_branding_secondary_rgb(self) -> tuple[int, int, int]:
        """Retourne le RGB du blanc secondaire branding"""
        return self.get_rgb(self.BRANDING_SECONDARY_WHITE)

    def get_branding_tertiary_rgb(self) -> tuple[int, int, int]:
        """Retourne le RGB du gris tertiaire branding"""
        return self.get_rgb(self.BRANDING_TERTIARY_GRAY)

    def get_logo_eyes_rgb(self) -> tuple[int, int, int]:
        """Retourne le RGB des yeux du logo (gris clair)"""
        return self.get_rgb(self.LOGO_EYES)

    def get_logo_text_rgb(self) -> tuple[int, int, int]:
        """Retourne le RGB du texte du logo (noir)"""
        return self.get_rgb(self.LOGO_TEXT)

    def get_logo_background_rgb(self) -> tuple[int, int, int]:
        """Retourne le RGB du fond du logo (turquoise)"""
        return self.get_rgb(self.LOGO_BACKGROUND)


# Instance globale de la palette BBIA
BBIA_PALETTE = BBIAColorPalette()


def get_bbia_palette() -> BBIAColorPalette:
    """Retourne l'instance globale de la palette BBIA"""
    return BBIA_PALETTE
