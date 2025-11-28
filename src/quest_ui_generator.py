"""
🎮 Quest UI Generator Module
Générateur d'éléments UI pour Arkalia Quest
Boutons, cartes, icônes, indicateurs
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from PIL import Image, ImageDraw, ImageFont  # type: ignore[import-untyped]
except ImportError:
    Image = None  # type: ignore[assignment]
    ImageDraw = None  # type: ignore[assignment]
    ImageFont = None  # type: ignore[assignment]

import svgwrite  # type: ignore[import-untyped]

from .variants import LogoVariants  # type: ignore[import-untyped]


class QuestUIGenerator:
    """
    Générateur d'éléments UI pour Arkalia Quest

    Types d'éléments :
    - Bouton Mission (200×60)
    - Carte Mission (400×300)
    - Icône Niveau (64, 128)
    - Indicateur Score (200×40)
    """

    # Dimensions des éléments UI
    UI_DIMENSIONS: Dict[str, tuple[int, int]] = {
        "button": (200, 60),
        "card": (400, 300),
        "icon": (64, 64),  # Taille de base, peut être 128
        "indicator": (200, 40),
    }

    def __init__(self, output_dir: Optional[Path] = None) -> None:
        """
        Initialise le générateur d'éléments UI

        Args:
            output_dir: Répertoire de sortie
        """
        self.output_dir = output_dir or Path("exports") / "quest" / "ui"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.variants_manager = LogoVariants()

        # Configuration du logging
        import logging

        self.logger = logging.getLogger(__name__)
        self.logger.info("🎮 Quest UI Generator initialisé")

    def generate_ui_element(
        self,
        element_type: str,
        variant: str = "serenity",
        text: Optional[str] = None,
        icon_size: Optional[int] = None,
        score: Optional[int] = None,
        level: Optional[int] = None,
    ) -> Path:
        """
        Génère un élément UI Quest

        Args:
            element_type: Type d'élément (button, card, icon, indicator)
            variant: Variante émotionnelle
            text: Texte personnalisé
            icon_size: Taille de l'icône (pour icon, 64 ou 128)
            score: Score (pour indicator)
            level: Niveau (pour icon)

        Returns:
            Chemin de l'élément généré
        """
        if element_type not in self.UI_DIMENSIONS:
            raise ValueError(
                f"Type d'élément '{element_type}' non reconnu. "
                f"Types disponibles: {list(self.UI_DIMENSIONS.keys())}"
            )

        width, height = self.UI_DIMENSIONS[element_type]

        # Ajuster taille pour icon
        if element_type == "icon" and icon_size:
            width = height = icon_size

        self.logger.info(
            f"🎮 Génération élément UI '{element_type}' "
            f"({width}×{height}) variante '{variant}'"
        )

        # Récupérer la variante
        variant_obj = self.variants_manager.get_variant(variant)

        # Créer le SVG
        drawing = svgwrite.Drawing(
            size=(width, height),
            profile="tiny",
        )

        # Ajouter les définitions
        defs = drawing.defs
        self._add_ui_gradient(defs, variant_obj)

        # Générer selon le type
        if element_type == "button":
            self._draw_button(drawing, variant_obj, width, height, text or "Mission")
        elif element_type == "card":
            self._draw_card(drawing, variant_obj, width, height, text or "Mission Card")
        elif element_type == "icon":
            self._draw_icon(drawing, variant_obj, width, height, level or 1)
        elif element_type == "indicator":
            self._draw_indicator(drawing, variant_obj, width, height, score or 0)

        # Sauvegarder
        output_path = (
            self.output_dir / f"quest-ui-{element_type}-{variant}-{width}x{height}.svg"
        )
        drawing.saveas(str(output_path))

        self.logger.info(f"✅ Élément UI généré : {output_path}")
        return output_path

    def _add_ui_gradient(self, defs: Any, variant: Any) -> None:
        """Ajoute le gradient pour les éléments UI"""
        gradient_id = f"uiGradient-{variant.variant_type.value}"

        gradient = svgwrite.gradients.LinearGradient(
            id=gradient_id,
            x1="0%",
            y1="0%",
            x2="0%",
            y2="100%",
        )

        gradient.add_stop_color(offset="0%", color=variant.colors.primary, opacity=1.0)
        gradient.add_stop_color(
            offset="100%", color=variant.colors.secondary, opacity=0.9
        )

        defs.add(gradient)

    def _draw_button(
        self, drawing: Any, variant: Any, width: int, height: int, text: str
    ) -> None:
        """Dessine un bouton Mission"""
        corner_radius = height // 4

        # Fond du bouton
        drawing.add(
            drawing.rect(
                insert=(0, 0),
                size=(width, height),
                rx=corner_radius,
                ry=corner_radius,
                fill=f"url(#uiGradient-{variant.variant_type.value})",
                stroke=variant.colors.glow,
                stroke_width=2,
            )
        )

        # Texte
        font_size = height // 3
        drawing.add(
            drawing.text(
                text,
                insert=(width // 2, height // 2 + font_size // 3),
                font_size=font_size,
                fill=variant.colors.glow,
                text_anchor="middle",
                font_family="Arial, sans-serif",
                font_weight="bold",
            )
        )

    def _draw_card(
        self, drawing: Any, variant: Any, width: int, height: int, text: str
    ) -> None:
        """Dessine une carte Mission"""
        corner_radius = 10
        header_height = height // 4

        # Fond de la carte
        drawing.add(
            drawing.rect(
                insert=(0, 0),
                size=(width, height),
                rx=corner_radius,
                ry=corner_radius,
                fill=f"url(#uiGradient-{variant.variant_type.value})",
                stroke=variant.colors.glow,
                stroke_width=2,
            )
        )

        # Header
        drawing.add(
            drawing.rect(
                insert=(0, 0),
                size=(width, header_height),
                rx=corner_radius,
                ry=corner_radius,
                fill=variant.colors.accent,
                opacity=0.8,
            )
        )

        # Texte header
        font_size = header_height // 2
        drawing.add(
            drawing.text(
                text,
                insert=(width // 2, header_height // 2 + font_size // 3),
                font_size=font_size,
                fill=variant.colors.glow,
                text_anchor="middle",
                font_family="Arial, sans-serif",
                font_weight="bold",
            )
        )

    def _draw_icon(
        self, drawing: Any, variant: Any, width: int, height: int, level: int
    ) -> None:
        """Dessine une icône Niveau"""
        center = width // 2
        radius = width // 3

        # Cercle de fond
        drawing.add(
            drawing.circle(
                center=(center, center),
                r=radius,
                fill=f"url(#uiGradient-{variant.variant_type.value})",
                stroke=variant.colors.glow,
                stroke_width=2,
            )
        )

        # Nombre
        font_size = width // 2
        drawing.add(
            drawing.text(
                str(level),
                insert=(center, center + font_size // 3),
                font_size=font_size,
                fill=variant.colors.glow,
                text_anchor="middle",
                font_family="Arial, sans-serif",
                font_weight="bold",
            )
        )

    def _draw_indicator(
        self, drawing: Any, variant: Any, width: int, height: int, score: int
    ) -> None:
        """Dessine un indicateur Score"""
        bar_width = int(width * 0.8)
        bar_height = height // 2
        bar_x = (width - bar_width) // 2
        bar_y = (height - bar_height) // 2

        # Fond de la barre
        drawing.add(
            drawing.rect(
                insert=(bar_x, bar_y),
                size=(bar_width, bar_height),
                fill=variant.colors.secondary,
                opacity=0.3,
                rx=bar_height // 2,
                ry=bar_height // 2,
            )
        )

        # Barre de progression
        progress_width = int(bar_width * min(score / 100, 1.0))
        drawing.add(
            drawing.rect(
                insert=(bar_x, bar_y),
                size=(progress_width, bar_height),
                fill=f"url(#uiGradient-{variant.variant_type.value})",
                rx=bar_height // 2,
                ry=bar_height // 2,
            )
        )

        # Texte score
        font_size = height // 2
        drawing.add(
            drawing.text(
                f"{score}%",
                insert=(width // 2, height // 2 + font_size // 3),
                font_size=font_size,
                fill=variant.colors.glow,
                text_anchor="middle",
                font_family="Arial, sans-serif",
                font_weight="bold",
            )
        )

    def generate_all_ui_elements(
        self,
        variant: str = "serenity",
        element_type: Optional[str] = None,
    ) -> List[Path]:
        """
        Génère tous les éléments UI Quest

        Args:
            variant: Variante émotionnelle
            element_type: Type d'élément (None = tous)

        Returns:
            Liste des chemins des éléments générés
        """
        self.logger.info(
            f"🎮 Génération de tous les éléments UI Quest (variante: {variant})"
        )

        generated_elements = []
        types_to_generate = (
            [element_type] if element_type else self.UI_DIMENSIONS.keys()
        )

        for etype in types_to_generate:
            try:
                # Pour icon, générer les 2 tailles
                if etype == "icon":
                    for icon_size in [64, 128]:
                        element_path = self.generate_ui_element(
                            element_type=etype,
                            variant=variant,
                            icon_size=icon_size,
                        )
                        generated_elements.append(element_path)
                else:
                    element_path = self.generate_ui_element(
                        element_type=etype,
                        variant=variant,
                    )
                    generated_elements.append(element_path)
            except Exception as e:
                self.logger.error(f"Erreur génération élément '{etype}': {e}")

        self.logger.info(f"✅ {len(generated_elements)} éléments UI générés")
        return generated_elements
