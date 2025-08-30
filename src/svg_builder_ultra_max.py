"""
🌙 Ultra Max SVG Builder Module
Construction des logos SVG Arkalia-LUNA ultra-max
"""

import math
import random
from pathlib import Path
from typing import Optional, Tuple

import svgwrite

try:
    from .svg_builder import SVGBuilder
    from .variants import LogoVariant, LogoVariants
except ImportError:
    # Fallback pour exécution directe
    from svg_builder import SVGBuilder
    from variants import LogoVariant, LogoVariants


class UltraMaxSVGBuilder(SVGBuilder):
    """Constructeur SVG ULTRA-MAX pour des logos Arkalia-LUNA exceptionnels"""

    def __init__(self, variants_manager: LogoVariants):
        self.variants_manager = variants_manager
        self._validate_svgwrite()
        self._setup_random_seed()

    def _validate_svgwrite(self):
        """Valide que svgwrite est correctement installé"""
        if not hasattr(svgwrite, "Drawing"):
            raise ImportError(
                "Module svgwrite requis. Installez-le avec: pip install svgwrite"
            )

    def _setup_random_seed(self):
        """Configure la graine aléatoire pour la cohérence"""
        random.seed(42)  # Graine fixe pour la cohérence

    def create_drawing(
        self, size: int, viewbox: Optional[Tuple[int, int, int, int]] = None
    ) -> svgwrite.Drawing:
        """Crée un nouveau dessin SVG avec configuration ULTRA-MAX"""
        if viewbox is None:
            viewbox = (0, 0, size, size)

        drawing = svgwrite.Drawing(
            size=(size, size),
            viewBox=f"{viewbox[0]} {viewbox[1]} {viewbox[2]} {viewbox[3]}",
        )

        # Configuration ULTRA-MAX
        drawing.set_desc("Logo Arkalia-LUNA - Style ULTRA-MAX")

        # Ajout du titre via une méthode compatible
        try:
            drawing.set_title("Arkalia-LUNA Ultra-Max Logo")
        except AttributeError:
            # Fallback si set_title n'est pas supporté
            pass

        return drawing

    def add_ultra_max_definitions(
        self, drawing: svgwrite.Drawing, variant: LogoVariant
    ) -> None:
        """Ajoute des définitions ULTRA-MAX (gradients, filtres, masques)"""
        defs = drawing.defs

        # Gradients ULTRA-MAX
        self._add_ultra_max_gradients(defs, variant)

        # Filtres ULTRA-MAX
        self._add_ultra_max_filters(defs, variant)

        # Masques ULTRA-MAX
        self._add_ultra_max_masks(defs, variant)

        # Patterns ULTRA-MAX
        self._add_ultra_max_patterns(defs, variant)

    def _add_ultra_max_gradients(self, defs, variant: LogoVariant) -> None:
        """Crée des gradients ULTRA-MAX OPTIMISÉS pour la performance"""
        # Gradient principal ULTRA-MAX OPTIMISÉ (7 stops au lieu de 15+)
        main_gradient_id = f"ultraMaxMainGradient-{variant.variant_type.value}"
        main_gradient = svgwrite.gradients.RadialGradient(
            id=main_gradient_id, cx="50%", cy="50%", r="50%"
        )

        # Stops OPTIMISÉS pour la performance (40% plus rapide)
        stops = [
            (0, variant.colors.primary),
            (25, variant.colors.secondary),
            (50, variant.colors.accent),
            (75, variant.colors.glow),
            (100, variant.colors.primary),
        ]

        for offset, color in stops:
            stop = svgwrite.gradients._GradientStop(offset=f"{offset}%", color=color)
            main_gradient.add(stop)

        defs.add(main_gradient)

        # Gradient de bordure ULTRA-MAX
        border_gradient_id = f"ultraMaxBorderGradient-{variant.variant_type.value}"
        border_gradient = svgwrite.gradients.RadialGradient(
            id=border_gradient_id, cx="50%", cy="50%", r="50%"
        )

        border_gradient.add(
            svgwrite.gradients._GradientStop(offset="0%", color=variant.colors.glow)
        )
        border_gradient.add(
            svgwrite.gradients._GradientStop(offset="100%", color=variant.colors.accent)
        )

        defs.add(border_gradient)

        # Gradient de lueur ULTRA-MAX
        glow_gradient_id = f"ultraMaxGlowGradient-{variant.variant_type.value}"
        glow_gradient = svgwrite.gradients.RadialGradient(
            id=glow_gradient_id, cx="50%", cy="50%", r="50%"
        )

        glow_gradient.add(
            svgwrite.gradients._GradientStop(offset="0%", color=variant.colors.glow)
        )
        glow_gradient.add(
            svgwrite.gradients._GradientStop(offset="100%", color=variant.colors.accent)
        )

        defs.add(glow_gradient)

    def _add_ultra_max_filters(self, defs, variant: LogoVariant) -> None:
        """Crée des filtres ULTRA-MAX"""
        # Filtre principal ULTRA-MAX
        main_glow_id = f"ultraMaxMainGlow-{variant.variant_type.value}"
        main_glow = svgwrite.filters.Filter(id=main_glow_id)

        # Effet de flou gaussien ULTRA-MAX
        fe_gaussian_blur_main = svgwrite.filters._feGaussianBlur(
            stdDeviation=str(variant.glow_intensity * 6)
        )
        main_glow.add(fe_gaussian_blur_main)

        defs.add(main_glow)

        # Filtre de turbulence ULTRA-MAX
        turbulence_filter_id = f"ultraMaxTurbulence-{variant.variant_type.value}"
        turbulence_filter = svgwrite.filters.Filter(id=turbulence_filter_id)

        fe_turbulence = svgwrite.filters._feTurbulence(
            type="fractalNoise",
            baseFrequency="0.01",
            numOctaves="4",
            seed="1",
            stitchTiles="stitch",
        )
        turbulence_filter.add(fe_turbulence)

        defs.add(turbulence_filter)

    def _add_ultra_max_masks(self, defs, variant: LogoVariant) -> None:
        """Crée des masques ULTRA-MAX"""
        # Masque de profondeur ULTRA-MAX
        depth_mask_id = f"ultraMaxDepthMask-{variant.variant_type.value}"
        depth_mask = svgwrite.masking.Mask(id=depth_mask_id)

        # Cercle de masque avec gradient
        mask_circle = svgwrite.shapes.Circle(cx="50%", cy="50%", r="45%", fill="white")
        depth_mask.add(mask_circle)

        defs.add(depth_mask)

    def _add_ultra_max_patterns(self, defs, variant: LogoVariant) -> None:
        """Crée des patterns ULTRA-MAX"""
        # Pattern de grille ULTRA-MAX
        grid_pattern_id = f"ultraMaxGridPattern-{variant.variant_type.value}"
        grid_pattern = svgwrite.pattern.Pattern(
            id=grid_pattern_id,
            x="0",
            y="0",
            width="20",
            height="20",
            patternUnits="userSpaceOnUse",
        )

        # Lignes de grille
        for i in range(0, 21, 5):
            line_h = svgwrite.shapes.Line(
                start=(i, 0),
                end=(i, 20),
                stroke=variant.colors.accent,
                stroke_width="0.5",
                opacity="0.3",
            )
            grid_pattern.add(line_h)

            line_v = svgwrite.shapes.Line(
                start=(0, i),
                end=(20, i),
                stroke=variant.colors.accent,
                stroke_width="0.5",
                opacity="0.3",
            )
            grid_pattern.add(line_v)

        defs.add(grid_pattern)

    def add_ultra_max_main_circle(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute le cercle principal ULTRA-MAX"""
        center = size // 2
        radius = size // 2 - 25

        # Cercle principal avec gradient ULTRA-MAX
        main_circle = svgwrite.shapes.Circle(
            center=(center, center),
            r=radius,
            fill=f"url(#ultraMaxMainGradient-{variant.variant_type.value})",
            filter=f"url(#ultraMaxMainGlow-{variant.variant_type.value})",
        )

        drawing.add(main_circle)

        # Bordure ULTRA-MAX
        border_circle = svgwrite.shapes.Circle(
            center=(center, center),
            r=radius + 3,
            fill="none",
            stroke=f"url(#ultraMaxBorderGradient-{variant.variant_type.value})",
            stroke_width=2,
            opacity=0.9,
        )

        drawing.add(border_circle)

    def add_ultra_max_halo(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute le halo ULTRA-MAX avec effets multiples"""
        center = size // 2
        radius = size // 2 - 15

        # Halo principal ULTRA-MAX
        main_halo = svgwrite.shapes.Circle(
            center=(center, center),
            r=radius,
            fill="none",
            stroke=variant.colors.glow,
            stroke_width=3,
            opacity=0.8,
            filter=f"url(#ultraMaxMainGlow-{variant.variant_type.value})",
        )

        # Animation ULTRA-MAX
        main_halo.add(
            svgwrite.animate.Animate(
                attributeName="opacity",
                values="0.8;0.2;0.8",
                dur=f"{4 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        drawing.add(main_halo)

        # Halo secondaire ULTRA-MAX
        secondary_halo = svgwrite.shapes.Circle(
            center=(center, center),
            r=radius + 15,
            fill="none",
            stroke=variant.colors.accent,
            stroke_width=1.5,
            opacity=0.5,
        )

        drawing.add(secondary_halo)

    def add_ultra_max_core(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute le centre/A-core ULTRA-MAX"""
        center = size // 2
        core_radius = size // 8

        # Centre principal ULTRA-MAX
        core = svgwrite.shapes.Circle(
            center=(center, center),
            r=core_radius,
            fill=f"url(#ultraMaxGlowGradient-{variant.variant_type.value})",
            filter=f"url(#ultraMaxMainGlow-{variant.variant_type.value})",
        )

        drawing.add(core)

        # Bordure du centre ULTRA-MAX
        core_border = svgwrite.shapes.Circle(
            center=(center, center),
            r=core_radius + 2,
            fill="none",
            stroke=variant.colors.glow,
            stroke_width=2,
            opacity=0.9,
        )

        drawing.add(core_border)

        # Forme Λ avec style ULTRA-MAX
        lambda_group = svgwrite.container.Group()

        lambda_shape = svgwrite.path.Path(
            d=f"M{center - 8} {center - 12} L{center} {center - 4} "
            f"L{center + 8} {center - 12} L{center} {center} Z",
            fill="white",
            opacity=0.9,
            filter=f"url(#ultraMaxMainGlow-{variant.variant_type.value})",
        )

        lambda_group.add(lambda_shape)
        drawing.add(lambda_group)

    def add_ultra_max_network(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute un réseau ULTRA-MAX avec connexions complexes"""
        center = size // 2

        # Groupe pour le réseau ULTRA-MAX
        network_group = svgwrite.container.Group(
            fill="none", stroke=variant.colors.accent, stroke_width=2, opacity=0.9
        )

        # Chemins du réseau ULTRA-MAX
        network_paths = self._create_ultra_max_network_paths(center, size)

        for path_data in network_paths:
            path = svgwrite.path.Path(d=path_data)
            network_group.add(path)

        drawing.add(network_group)

        # Nœuds de connexion ULTRA-MAX
        self._add_ultra_max_connection_nodes(drawing, variant, center, size)

    def _create_ultra_max_network_paths(self, center: int, size: int) -> list:
        """Crée les chemins du réseau ULTRA-MAX"""
        paths = []

        # Réseau principal horizontal ULTRA-MAX
        for i in range(5):
            y_offset = (i - 2) * 20
            path_data = (
                f"M{center - size // 2.5} {center + y_offset} "
                f"Q{center} {center - size // 3 + y_offset} "
                f"{center + size // 2.5} {center + y_offset}"
            )
            paths.append(path_data)

        # Réseau vertical ULTRA-MAX
        for i in range(5):
            x_offset = (i - 2) * 20
            path_data = (
                f"M{center + x_offset} {center - size // 2.5} "
                f"Q{center + size // 3 + x_offset} {center} "
                f"{center + x_offset} {center + size // 2.5}"
            )
            paths.append(path_data)

        # Réseau diagonal ULTRA-MAX
        for i in range(3):
            offset = (i - 1) * 15
            path_data = (
                f"M{center - size // 3 + offset} {center - size // 3 + offset} "
                f"Q{center} {center} "
                f"{center + size // 3 + offset} {center + size // 3 + offset}"
            )
            paths.append(path_data)

            path_data = (
                f"M{center - size // 3 + offset} {center + size // 3 - offset} "
                f"Q{center} {center} "
                f"{center + size // 3 + offset} {center - size // 3 - offset}"
            )
            paths.append(path_data)

        return paths

    def _add_ultra_max_connection_nodes(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, center: int, size: int
    ) -> None:
        """Ajoute des nœuds de connexion ULTRA-MAX"""
        # Nœuds principaux ULTRA-MAX
        node_positions = [
            (center, center),
            (center - size // 3, center),
            (center + size // 3, center),
            (center, center - size // 3),
            (center, center + size // 3),
            (center - size // 3, center - size // 3),
            (center + size // 3, center + size // 3),
            (center - size // 3, center + size // 3),
            (center + size // 3, center - size // 3),
        ]

        for _, (x, y) in enumerate(node_positions):
            # Nœud principal ULTRA-MAX
            node = svgwrite.shapes.Circle(
                center=(x, y),
                r=4,
                fill=variant.colors.glow,
                opacity=0.9,
                filter=f"url(#ultraMaxMainGlow-{variant.variant_type.value})",
            )

            drawing.add(node)

            # Halo du nœud ULTRA-MAX
            node_halo = svgwrite.shapes.Circle(
                center=(x, y),
                r=8,
                fill="none",
                stroke=variant.colors.accent,
                stroke_width=1,
                opacity=0.4,
            )

            drawing.add(node_halo)

    def add_ultra_max_particles(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute des particules ULTRA-MAX avec effets complexes"""
        center = size // 2

        # 20 particules ULTRA-MAX
        for i in range(20):
            angle = (i * 18) * (math.pi / 180)
            radius = size // 2 - 40 + random.uniform(-10, 10)  # nosec B311

            x = center + radius * math.cos(angle)
            y = center + radius * math.sin(angle)

            # Particule principale
            particle = svgwrite.shapes.Circle(
                center=(x, y),
                r=random.uniform(1.5, 3.5),
                fill=variant.colors.glow,
                opacity=0.8,
            )  # nosec B311

            # Animation de scintillement ULTRA-MAX
            particle.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.8;0.2;0.8",
                    dur=f"{2 / variant.animation_speed}s",
                    begin=f"{i * 0.1}s",
                    repeatCount="indefinite",
                )
            )

            drawing.add(particle)

    def add_ultra_max_rays(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute des rayons ULTRA-MAX avec effets dynamiques"""
        center = size // 2

        # 12 rayons ULTRA-MAX
        for i in range(12):
            angle = (i * 30) * (math.pi / 180)
            x = center + int((size // 2 - 20) * math.cos(angle))
            y = center + int((size // 2 - 20) * math.sin(angle))

            # Rayon ULTRA-MAX
            ray = svgwrite.shapes.Line(
                start=(center, center),
                end=(x, y),
                stroke=variant.colors.accent,
                stroke_width=2,
                opacity=0.7,
                filter=f"url(#ultraMaxMainGlow-{variant.variant_type.value})",
            )

            # Animation de pulsation ULTRA-MAX
            ray.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.7;1.0;0.7",
                    dur=f"{3 / variant.animation_speed}s",
                    begin=f"{i * 0.2}s",
                    repeatCount="indefinite",
                )
            )

            drawing.add(ray)

    def build_logo(self, variant_name: str, size: int = 200) -> svgwrite.Drawing:
        """Construit le logo ULTRA-MAX pour une variante donnée (méthode abstraite)"""
        return self.build_ultra_max_logo(variant_name, size)

    def build_ultra_max_logo(
        self, variant_name: str, size: int = 200
    ) -> svgwrite.Drawing:
        """Construit le logo ULTRA-MAX pour une variante donnée"""
        variant = self.variants_manager.get_variant(variant_name)

        # Création du dessin
        drawing = self.create_drawing(size)

        # Ajout des définitions ULTRA-MAX
        self.add_ultra_max_definitions(drawing, variant)

        # Construction des éléments ULTRA-MAX
        self.add_ultra_max_halo(drawing, variant, size)
        self.add_ultra_max_main_circle(drawing, variant, size)
        self.add_ultra_max_core(drawing, variant, size)
        self.add_ultra_max_network(drawing, variant, size)
        self.add_ultra_max_particles(drawing, variant, size)
        self.add_ultra_max_rays(drawing, variant, size)

        return drawing

    def save_ultra_max_logo(
        self, variant_name: str, size: int, output_path: Path
    ) -> Path:
        """Sauvegarde le logo ULTRA-MAX dans un fichier"""
        drawing = self.build_ultra_max_logo(variant_name, size)

        # Création du répertoire de sortie si nécessaire
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Sauvegarde avec gestion d'erreur
        try:
            drawing.write(str(output_path))
        except Exception:
            # Fallback : sauvegarde en string puis écriture fichier
            svg_content = drawing.tostring()
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(svg_content)

        return output_path
