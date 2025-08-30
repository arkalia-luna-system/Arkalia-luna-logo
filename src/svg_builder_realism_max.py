"""
🌙 Realism Max SVG Builder Module
Construction de logos ultra-réalistes avec effets organiques et IA
"""

import math
import random
from typing import Optional, Tuple

import svgwrite

try:
    from .svg_builder import SVGBuilder
    from .variants import LogoVariant, LogoVariants
except ImportError:
    # Fallback pour exécution directe
    from svg_builder import SVGBuilder
    from variants import LogoVariant, LogoVariants


class RealismMaxSVGBuilder(SVGBuilder):
    """Constructeur SVG ultra-réaliste avec effets organiques et optimisations IA"""

    def __init__(self, variants_manager: LogoVariants):
        super().__init__(variants_manager)
        self._setup_realism_enhancements()

    def _setup_realism_enhancements(self) -> None:
        """Configure les améliorations réalistes pour la génération"""
        # Graine aléatoire pour la cohérence des effets organiques
        random.seed(42)
        self.realism_level = 0.95  # Niveau de réalisme (0-1)
        self.organic_complexity = 0.8  # Complexité organique
        self.ai_enhancement = True  # Amélioration IA active

    def create_drawing(
        self, size: int, viewbox: Optional[Tuple[int, int, int, int]] = None
    ) -> svgwrite.Drawing:
        """Crée un nouveau dessin SVG avec configuration réaliste"""
        if viewbox is None:
            viewbox = (0, 0, size, size)

        drawing = svgwrite.Drawing(
            size=(size, size),
            viewBox=f"{viewbox[0]} {viewbox[1]} {viewbox[2]} {viewbox[3]}",
        )

        # Configuration réaliste
        drawing.set_desc(
            "Logo Arkalia-LUNA - Style ultra-réaliste avec effets organiques"
        )
        # drawing.set_title("Arkalia-LUNA Realism Max")
        # Commenté car pas supporté par svgwrite

        return drawing

    def add_realism_definitions(
        self, drawing: svgwrite.Drawing, variant: LogoVariant
    ) -> None:
        """Ajoute des définitions ultra-réalistes (gradients, filtres, masques)"""
        defs = drawing.defs

        # Gradients réalistes optimisés (5-7 stops au lieu de 20+)
        self._add_realistic_gradients(defs, variant)

        # Filtres de lueur réalistes
        self._add_realistic_glow_filters(defs, variant)

        # Filtres organiques et turbulence
        self._add_organic_filters(defs, variant)

        # Masques de profondeur réalistes
        self._add_depth_masks(defs, variant)

    def _add_realistic_gradients(self, defs, variant: LogoVariant) -> None:
        """Crée des gradients réalistes optimisés (5-7 stops max pour la performance)"""
        gradient_id = f"realisticGradient-{variant.variant_type.value}"

        # Gradient principal optimisé avec 7 stops max
        gradient = svgwrite.gradients.RadialGradient(
            id=gradient_id, cx="50%", cy="50%", r="50%"
        )

        # Stops optimisés pour la performance
        stops = [
            (0, variant.colors.primary, 1.0),
            (20, variant.colors.secondary, 0.8),
            (40, variant.colors.accent, 0.6),
            (60, variant.colors.glow, 0.4),
            (80, variant.colors.secondary, 0.2),
            (100, variant.colors.primary, 0.0),
        ]

        for offset, color, opacity in stops:
            try:
                # Méthode correcte pour svgwrite
                stop = svgwrite.gradients.Stop(
                    offset=f"{offset}%", color=color, opacity=opacity
                )
                gradient.add_stop(stop)
            except Exception:
                # Fallback sans opacity si non supporté
                gradient.add_stop_color(offset=f"{offset}%", color=color)

        defs.add(gradient)

        # Gradient de bordure réaliste
        border_gradient_id = f"realisticBorderGradient-{variant.variant_type.value}"
        border_gradient = svgwrite.gradients.RadialGradient(
            id=border_gradient_id, cx="50%", cy="50%", r="50%"
        )

        border_gradient.add_stop_color(offset="0%", color=variant.colors.glow)
        border_gradient.add_stop_color(offset="100%", color=variant.colors.accent)

        defs.add(border_gradient)

    def _add_realistic_glow_filters(self, defs, variant: LogoVariant) -> None:
        """Crée des filtres de lueur réalistes optimisés"""
        # Filtre de lueur principal
        glow_filter_id = f"realisticGlowFilter-{variant.variant_type.value}"
        glow_filter = svgwrite.filters.Filter(id=glow_filter_id)

        # Lueur gaussienne optimisée
        fe_gaussian_blur = svgwrite.filters._feGaussianBlur(stdDeviation=3)
        glow_filter.add(fe_gaussian_blur)

        defs.add(glow_filter)

    def _add_organic_filters(self, defs, variant: LogoVariant) -> None:
        """Crée des filtres organiques et de turbulence"""
        # Filtre de turbulence organique
        turbulence_filter_id = f"organicTurbulenceFilter-{variant.variant_type.value}"
        turbulence_filter = svgwrite.filters.Filter(id=turbulence_filter_id)

        # Turbulence réaliste
        fe_turbulence = svgwrite.filters._feTurbulence(
            type="fractalNoise", baseFrequency=0.01, numOctaves=3, seed=42
        )
        turbulence_filter.add(fe_turbulence)

        defs.add(turbulence_filter)

    def _add_depth_masks(self, defs, variant: LogoVariant) -> None:
        """Crée des masques de profondeur réalistes"""
        # Masque de profondeur principal
        depth_mask_id = f"depthMask-{variant.variant_type.value}"
        depth_mask = svgwrite.masking.Mask(id=depth_mask_id)

        # Rectangle de masque avec gradient
        mask_rect = svgwrite.shapes.Rect(
            x=0,
            y=0,
            width="100%",
            height="100%",
            fill=f"url(#realisticGradient-{variant.variant_type.value})",
        )
        depth_mask.add(mask_rect)

        defs.add(depth_mask)

    def build_logo(self, variant_name: str, size: int) -> svgwrite.Drawing:
        """Construit le logo ultra-réaliste pour une variante donnée (méthode abstraite)"""
        variant = self.variants_manager.get_variant(variant_name)

        # Création du dessin
        drawing = self.create_drawing(size)

        # Ajout des définitions réalistes
        self.add_realism_definitions(drawing, variant)

        # Ajout des éléments du logo
        self._add_realistic_logo_elements(drawing, variant, size)

        return drawing

    def _add_realistic_logo_elements(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute les éléments du logo avec style réaliste"""
        # Cercle principal avec gradient réaliste
        center = size // 2
        radius = size // 3

        main_circle = svgwrite.shapes.Circle(
            cx=center,
            cy=center,
            r=radius,
            fill=f"url(#realisticGradient-{variant.variant_type.value})",
            filter=f"url(#realisticGlowFilter-{variant.variant_type.value})",
        )
        drawing.add(main_circle)

        # Effets organiques supplémentaires selon le niveau de réalisme
        if self.realism_level > 0.7:
            self._add_organic_effects(drawing, variant, size, center, radius)

    def _add_organic_effects(
        self,
        drawing: svgwrite.Drawing,
        variant: LogoVariant,
        size: int,
        center: int,
        radius: int,
    ) -> None:
        """Ajoute des effets organiques avancés"""
        # Particules organiques
        num_particles = int(5 * self.realism_level)
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(radius * 0.8, radius * 1.2)

            x = center + distance * math.cos(angle)
            y = center + distance * math.sin(angle)

            particle = svgwrite.shapes.Circle(
                cx=x,
                cy=y,
                r=random.uniform(1, 3),
                fill=variant.colors.glow,
                opacity=random.uniform(0.3, 0.7),
            )
            drawing.add(particle)
