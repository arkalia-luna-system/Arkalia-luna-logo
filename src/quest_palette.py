"""
🎮 Quest Palette Module
Palette de couleurs officielle Arkalia Quest pour intégration
Couleurs adaptées au thème éducatif et gamification
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class QuestColorPalette:
    """
    Palette de couleurs officielle Arkalia Quest

    Couleurs principales adaptées au thème éducatif et gamification
    """

    # ============================================================================
    # COULEURS PRINCIPALES
    # ============================================================================
    PRIMARY: str = "#667eea"  # Bleu-violet éducatif - Logo principal
    SECONDARY: str = "#764ba2"  # Violet profond - Accents
    SUCCESS: str = "#10b981"  # Vert émeraude - Succès, validation
    WARNING: str = "#f59e0b"  # Orange doré - Avertissements
    DANGER: str = "#ef4444"  # Rouge - Erreurs, échecs
    INFO: str = "#3b82f6"  # Bleu clair - Informations

    # ============================================================================
    # COULEURS UI
    # ============================================================================
    BACKGROUND: str = "#0f172a"  # Bleu très foncé - Fond dark mode
    SURFACE: str = "#1e293b"  # Bleu-gris foncé - Surfaces, cartes
    TEXT_PRIMARY: str = "#f1f5f9"  # Blanc cassé - Texte principal
    TEXT_SECONDARY: str = "#cbd5e1"  # Gris clair - Texte secondaire

    # ============================================================================
    # VARIANTES DE COULEURS
    # ============================================================================
    PRIMARY_LIGHT: str = "#818cf8"  # Bleu-violet clair
    PRIMARY_DARK: str = "#4f46e5"  # Bleu-violet foncé
    SECONDARY_LIGHT: str = "#a78bfa"  # Violet clair
    SECONDARY_DARK: str = "#5b21b6"  # Violet foncé

    def to_dict(self) -> Dict[str, str]:
        """Convertit la palette complète en dictionnaire"""
        return {
            "primary": self.PRIMARY,
            "secondary": self.SECONDARY,
            "success": self.SUCCESS,
            "warning": self.WARNING,
            "danger": self.DANGER,
            "info": self.INFO,
            "background": self.BACKGROUND,
            "surface": self.SURFACE,
            "text_primary": self.TEXT_PRIMARY,
            "text_secondary": self.TEXT_SECONDARY,
            "primary_light": self.PRIMARY_LIGHT,
            "primary_dark": self.PRIMARY_DARK,
            "secondary_light": self.SECONDARY_LIGHT,
            "secondary_dark": self.SECONDARY_DARK,
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

    def get_primary_rgb(self) -> tuple[int, int, int]:
        """Retourne le RGB du bleu-violet primaire"""
        return self.get_rgb(self.PRIMARY)

    def get_secondary_rgb(self) -> tuple[int, int, int]:
        """Retourne le RGB du violet secondaire"""
        return self.get_rgb(self.SECONDARY)


# Instance globale de la palette Quest
QUEST_PALETTE = QuestColorPalette()


def get_quest_palette() -> QuestColorPalette:
    """Retourne l'instance globale de la palette Quest"""
    return QUEST_PALETTE

