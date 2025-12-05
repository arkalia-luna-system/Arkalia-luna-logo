"""
🎮 Quest SVG Builder Module
Construction de logos Quest avec éléments de gamification et éducatifs
"""

import math
from pathlib import Path
from typing import Optional, Tuple

try:
    import svgwrite  # type: ignore[import-untyped,import-not-found]
    from svgwrite.container import Defs  # type: ignore[import-untyped,import-not-found]
except ImportError:
    svgwrite = None  # type: ignore[assignment]
    Defs = None  # type: ignore[assignment]

try:
    from .svg_builder import SVGBuilder
    from .variants import LogoVariant, LogoVariants
except ImportError:
    from svg_builder import (
        SVGBuilder,  # type: ignore[import-untyped,import-not-found,no-redef]
    )
    from variants import (  # type: ignore[import-untyped,import-not-found,no-redef]
        LogoVariant,
        LogoVariants,
    )


class QuestSVGBuilder(SVGBuilder):
    """Constructeur SVG Quest pour logos de jeu éducatif avec gamification"""

    def __init__(self, variants_manager: LogoVariants) -> None:
        self.variants_manager = variants_manager
        self._validate_svgwrite()

    def _validate_svgwrite(self) -> None:
        """Valide que svgwrite est correctement installé"""
        if svgwrite is None:
            raise ImportError(
                "Module svgwrite requis. Installez-le avec: pip install svgwrite",
            )
        if not hasattr(svgwrite, "Drawing"):
            raise ImportError(
                "Module svgwrite requis. Installez-le avec: pip install svgwrite",
            )

    def create_drawing(
        self,
        size: int,
        viewbox: Optional[Tuple[int, int, int, int]] = None,
    ) -> svgwrite.Drawing:
        """Crée un nouveau dessin SVG avec configuration Quest"""
        if viewbox is None:
            viewbox = (0, 0, size, size)

        drawing = svgwrite.Drawing(
            size=(size, size),
            viewBox=f"{viewbox[0]} {viewbox[1]} {viewbox[2]} {viewbox[3]}",
        )

        drawing.set_desc("Logo Arkalia Quest - Jeu éducatif avec gamification")

        return drawing

    def build_logo(self, variant_name: str, size: int) -> svgwrite.Drawing:
        """Construit le logo Quest pour une variante donnée"""
        variant = self.variants_manager.get_variant(variant_name)

        # Création du dessin
        drawing = self.create_drawing(size)

        # Ajout des définitions Quest
        self.add_quest_definitions(drawing, variant)

        # Construction des éléments Quest
        self.add_quest_background(drawing, variant, size)
        self.add_quest_badge(drawing, variant, size)
        self.add_quest_stars(drawing, variant, size)
        self.add_quest_educational_elements(drawing, variant, size)
        self.add_quest_glow_effects(drawing, variant, size)

        return drawing

    def add_quest_definitions(
        self,
        drawing: svgwrite.Drawing,
        variant: LogoVariant,
    ) -> None:
        """Ajoute des définitions Quest (gradients, filtres)"""
        defs = drawing.defs

        # Gradient principal Quest
        self._add_quest_main_gradient(defs, variant)

        # Gradient badge
        self._add_quest_badge_gradient(defs, variant)

        # Gradient étoiles
        self._add_quest_star_gradient(defs, variant)

        # Filtres de lueur
        self._add_quest_glow_filters(defs, variant)

    def _add_quest_main_gradient(self, defs: Defs, variant: LogoVariant) -> None:
        """Crée le gradient principal Quest"""
        gradient_id = f"questMainGradient-{variant.variant_type.value}"

        gradient = svgwrite.gradients.RadialGradient(
            id=gradient_id,
            cx="50%",
            cy="50%",
            r="70%",
        )

        gradient.add_stop_color(offset="0%", color=variant.colors.primary, opacity=1.0)
        gradient.add_stop_color(
            offset="40%", color=variant.colors.secondary, opacity=0.9
        )
        gradient.add_stop_color(offset="70%", color=variant.colors.accent, opacity=0.7)
        gradient.add_stop_color(
            offset="100%", color=variant.colors.primary, opacity=0.3
        )

        defs.add(gradient)

    def _add_quest_badge_gradient(self, defs: Defs, variant: LogoVariant) -> None:
        """Crée le gradient pour le badge"""
        gradient_id = f"questBadgeGradient-{variant.variant_type.value}"

        gradient = svgwrite.gradients.LinearGradient(
            id=gradient_id,
            x1="0%",
            y1="0%",
            x2="0%",
            y2="100%",
        )

        gradient.add_stop_color(offset="0%", color=variant.colors.glow, opacity=1.0)
        gradient.add_stop_color(
            offset="50%", color=variant.colors.secondary, opacity=0.9
        )
        gradient.add_stop_color(
            offset="100%", color=variant.colors.primary, opacity=0.8
        )

        defs.add(gradient)

    def _add_quest_star_gradient(self, defs: Defs, variant: LogoVariant) -> None:
        """Crée le gradient pour les étoiles"""
        gradient_id = f"questStarGradient-{variant.variant_type.value}"

        gradient = svgwrite.gradients.RadialGradient(
            id=gradient_id,
            cx="50%",
            cy="50%",
            r="50%",
        )

        gradient.add_stop_color(offset="0%", color="#FFD700", opacity=1.0)
        gradient.add_stop_color(offset="50%", color=variant.colors.accent, opacity=0.9)
        gradient.add_stop_color(offset="100%", color=variant.colors.glow, opacity=0.7)

        defs.add(gradient)

    def _add_quest_glow_filters(self, defs: Defs, variant: LogoVariant) -> None:
        """Crée les filtres de lueur Quest"""
        filter_id = f"questGlow-{variant.variant_type.value}"

        glow_filter = svgwrite.filters.Filter(id=filter_id)
        glow_filter["x"] = "-50%"
        glow_filter["y"] = "-50%"
        glow_filter["width"] = "200%"
        glow_filter["height"] = "200%"

        fe_gaussian = svgwrite.filters._feGaussianBlur(
            stdDeviation=str(3 * variant.glow_intensity),
        )
        glow_filter.add(fe_gaussian)

        defs.add(glow_filter)

    def add_quest_background(
        self,
        drawing: svgwrite.Drawing,
        variant: LogoVariant,
        size: int,
    ) -> None:
        """Ajoute le fond Quest avec style éducatif"""
        center = size // 2

        # Fond principal avec gradient
        background = svgwrite.shapes.Circle(
            center=(center, center),
            r=size // 2 - 5,
            fill=f"url(#questMainGradient-{variant.variant_type.value})",
            opacity=0.95,
        )
        drawing.add(background)

        # Bordure badge
        border = svgwrite.shapes.Circle(
            center=(center, center),
            r=size // 2 - 5,
            fill="none",
            stroke=variant.colors.glow,
            stroke_width=3,
            opacity=0.8,
            filter=f"url(#questGlow-{variant.variant_type.value})",
        )
        drawing.add(border)

    def add_quest_badge(
        self,
        drawing: svgwrite.Drawing,
        variant: LogoVariant,
        size: int,
    ) -> None:
        """Ajoute le badge central Quest (forme écusson/bouclier)"""
        center_x = size // 2
        center_y = size // 2
        badge_size = size * 0.35  # Réduit pour mieux s'adapter

        # Forme de badge (écusson/bouclier)
        badge_path = svgwrite.path.Path(
            d=(
                f"M {center_x} {center_y - badge_size * 0.7} "
                f"L {center_x - badge_size * 0.6} {center_y - badge_size * 0.3} "
                f"L {center_x - badge_size * 0.6} {center_y + badge_size * 0.4} "
                f"Q {center_x - badge_size * 0.6} {center_y + badge_size * 0.7} "
                f"{center_x} {center_y + badge_size * 0.7} "
                f"Q {center_x + badge_size * 0.6} {center_y + badge_size * 0.7} "
                f"{center_x + badge_size * 0.6} {center_y + badge_size * 0.4} "
                f"L {center_x + badge_size * 0.6} {center_y - badge_size * 0.3} Z"
            ),
            fill=f"url(#questBadgeGradient-{variant.variant_type.value})",
            stroke=variant.colors.primary,
            stroke_width=2,
            filter=f"url(#questGlow-{variant.variant_type.value})",
        )
        drawing.add(badge_path)

        # Symbole "Q" stylisé dans le badge
        q_symbol = svgwrite.text.Text(
            "Q",
            x=[center_x],
            y=[center_y + badge_size * 0.15],
            font_family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif",
            font_size=int(badge_size * 0.6),
            font_weight="bold",
            fill=variant.colors.primary,
            text_anchor="middle",
            dominant_baseline="middle",
        )
        drawing.add(q_symbol)

        # Ligne décorative dans le badge
        line = svgwrite.shapes.Line(
            start=(center_x - badge_size * 0.4, center_y),
            end=(center_x + badge_size * 0.4, center_y),
            stroke=variant.colors.glow,
            stroke_width=2,
            opacity=0.7,
        )
        drawing.add(line)

    def add_quest_stars(
        self,
        drawing: svgwrite.Drawing,
        variant: LogoVariant,
        size: int,
    ) -> None:
        """Ajoute des étoiles (achievements) autour du badge"""
        center = size // 2
        star_size = size * 0.08  # Taille des étoiles
        star_distance = size * 0.38  # Distance du centre pour les étoiles

        # 5 étoiles autour du badge (achievements)
        num_stars = 5
        for i in range(num_stars):
            angle = (i * 360 / num_stars - 90) * (
                math.pi / 180
            )  # -90 pour commencer en haut
            # Positionner les étoiles autour du badge, en restant dans les limites
            star_x = center + star_distance * math.cos(angle)
            star_y = center + star_distance * math.sin(angle)

            # Vérifier que les étoiles restent dans les limites (avec marge)
            margin = star_size
            if margin < star_x < size - margin and margin < star_y < size - margin:
                star = self._create_star(star_x, star_y, star_size, variant, i)
                drawing.add(star)

    def _create_star(
        self,
        center_x: float,
        center_y: float,
        radius: float,
        variant: LogoVariant,
        index: int,
    ) -> svgwrite.container.Group:
        """Crée une étoile (achievement)"""
        star_group = svgwrite.container.Group()

        # Forme d'étoile à 5 branches
        points = []
        for i in range(10):
            angle = (i * 36 - 90) * (math.pi / 180)
            r = radius if i % 2 == 0 else radius * 0.4
            x = center_x + r * math.cos(angle)
            y = center_y + r * math.sin(angle)
            points.append((x, y))

        star_path = svgwrite.path.Path(
            d=f"M {points[0][0]} {points[0][1]} "
            + " ".join([f"L {p[0]} {p[1]}" for p in points[1:]])
            + " Z",
            fill=f"url(#questStarGradient-{variant.variant_type.value})",
            stroke=variant.colors.glow,
            stroke_width=1,
            filter=f"url(#questGlow-{variant.variant_type.value})",
        )

        # Animation de scintillement
        star_path.add(
            svgwrite.animate.Animate(
                attributeName="opacity",
                values="0.7;1.0;0.7",
                dur=f"{2.5 / variant.animation_speed}s",
                begin=f"{index * 0.3}s",
                repeatCount="indefinite",
            )
        )

        star_group.add(star_path)
        return star_group

    def add_quest_educational_elements(
        self,
        drawing: svgwrite.Drawing,
        variant: LogoVariant,
        size: int,
    ) -> None:
        """Ajoute des éléments éducatifs (livres, savoir)"""
        center = size // 2
        badge_radius = size * 0.35  # Ajusté pour correspondre au badge

        # Livres stylisés autour du badge (plus petits et mieux positionnés)
        book_group = svgwrite.container.Group()

        # 3 livres stylisés
        for i in range(3):
            angle = (i * 120 - 60) * (math.pi / 180)
            book_x = center + (badge_radius * 0.6) * math.cos(angle)
            book_y = center + (badge_radius * 0.6) * math.sin(angle)

            # Vérifier que les livres restent dans les limites
            if 0 < book_x < size and 0 < book_y < size:
                # Livre stylisé (rectangle avec lignes)
                book = svgwrite.shapes.Rect(
                    insert=(book_x - size * 0.03, book_y - size * 0.05),
                    size=(size * 0.06, size * 0.1),
                    fill=variant.colors.accent,
                    opacity=0.6,
                    rx=2,
                )
                book_group.add(book)

                # Lignes de texte sur le livre
                for j in range(3):
                    line = svgwrite.shapes.Line(
                        start=(
                            book_x - size * 0.025,
                            book_y - size * 0.03 + j * size * 0.015,
                        ),
                        end=(
                            book_x + size * 0.025,
                            book_y - size * 0.03 + j * size * 0.015,
                        ),
                        stroke=variant.colors.primary,
                        stroke_width=1,
                        opacity=0.5,
                    )
                    book_group.add(line)

        drawing.add(book_group)

    def add_quest_glow_effects(
        self,
        drawing: svgwrite.Drawing,
        variant: LogoVariant,
        size: int,
    ) -> None:
        """Ajoute des effets de lueur Quest"""
        center = size // 2

        # Halo pulsant autour du badge
        halo = svgwrite.shapes.Circle(
            center=(center, center),
            r=size * 0.42,
            fill="none",
            stroke=variant.colors.glow,
            stroke_width=2,
            opacity=0.6 * variant.glow_intensity,
            filter=f"url(#questGlow-{variant.variant_type.value})",
        )

        # Animation de pulsation
        halo.add(
            svgwrite.animate.Animate(
                attributeName="opacity",
                values=f"{0.6 * variant.glow_intensity};{0.3 * variant.glow_intensity};{0.6 * variant.glow_intensity}",
                dur=f"{3 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        drawing.add(halo)

    def save_logo(self, variant_name: str, size: int, output_path: Path) -> None:
        """Sauvegarde le logo Quest"""
        drawing = self.build_logo(variant_name, size)
        drawing.saveas(str(output_path), pretty=True)
