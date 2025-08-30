"""
🌙 Advanced SVG Builder Module
Construction des logos SVG Arkalia-LUNA avec effets avancés
"""

import math
from pathlib import Path
from typing import List, Optional, Tuple

import svgwrite

try:
    from .svg_builder import SVGBuilder
    from .variants import LogoVariant, LogoVariants
except ImportError:
    # Fallback pour exécution directe
    from svg_builder import SVGBuilder
    from variants import LogoVariant, LogoVariants


class AdvancedSVGBuilder(SVGBuilder):
    """Constructeur SVG ultra-avancé pour des logos Arkalia-LUNA exceptionnels"""

    def __init__(self, variants_manager: LogoVariants):
        self.variants_manager = variants_manager
        self._validate_svgwrite()

    def _validate_svgwrite(self):
        """Valide que svgwrite est correctement installé"""
        if not hasattr(svgwrite, "Drawing"):
            raise ImportError(
                "Module svgwrite requis. Installez-le avec: pip install svgwrite"
            )

    def create_drawing(
        self, size: int, viewbox: Optional[Tuple[int, int, int, int]] = None
    ) -> svgwrite.Drawing:
        """Crée un nouveau dessin SVG avec configuration avancée"""
        if viewbox is None:
            viewbox = (0, 0, size, size)

        drawing = svgwrite.Drawing(
            size=(size, size),
            viewBox=f"{viewbox[0]} {viewbox[1]} {viewbox[2]} {viewbox[3]}",
        )

        # Configuration avancée
        drawing.set_desc("Logo Arkalia-LUNA - Variante techno-mystique avancée")

        return drawing

    def add_advanced_definitions(
        self, drawing: svgwrite.Drawing, variant: LogoVariant
    ) -> None:
        """Ajoute des définitions ultra-avancées (gradients, filtres, masques)"""
        defs = drawing.defs

        # Gradient radial ultra-avancé pour la lune
        self._add_advanced_moon_gradient(defs, variant)

        # Filtres de lueur ultra-avancés
        self._add_advanced_glow_filters(defs, variant)

        # Filtres de turbulence pour l'effet organique
        self._add_organic_turbulence_filters(defs, variant)

        # Masques pour les effets de profondeur
        self._add_depth_masks(defs, variant)

        # Gradients pour les réseaux neuronaux
        self._add_neural_network_gradients(defs, variant)

    def _add_advanced_moon_gradient(self, defs, variant: LogoVariant) -> None:
        """Crée un gradient radial ultra-avancé avec multiples stops"""
        gradient_id = f"advancedMoonGradient-{variant.variant_type.value}"

        # Gradient principal avec 8 stops pour une profondeur maximale
        gradient = svgwrite.gradients.RadialGradient(
            id=gradient_id, cx="50%", cy="50%", r="50%"
        )

        # Stops avancés avec opacité
        gradient.add_stop_color(offset="0%", color=variant.colors.primary, opacity=1.0)
        gradient.add_stop_color(offset="100%", color=variant.colors.accent, opacity=0.8)

        defs.add(gradient)

        # Gradient secondaire pour l'effet de bordure
        border_gradient_id = f"borderGradient-{variant.variant_type.value}"
        border_gradient = svgwrite.gradients.RadialGradient(
            id=border_gradient_id, cx="50%", cy="50%", r="50%"
        )

        # Stops avec syntaxe correcte
        border_gradient.add_stop_color(
            offset="0%", color=variant.colors.glow, opacity=0.8
        )
        border_gradient.add_stop_color(
            offset="100%", color=variant.colors.primary, opacity=0.2
        )

        defs.add(border_gradient)

    def _add_advanced_glow_filters(self, defs, variant: LogoVariant) -> None:
        """Crée des filtres de lueur ultra-avancés avec multiples effets"""
        # Filtre principal de lueur
        main_glow_id = f"mainGlow-{variant.variant_type.value}"
        main_glow = svgwrite.filters.Filter(id=main_glow_id)

        # Effet de flou gaussien principal
        fe_gaussian_blur_main = svgwrite.filters._feGaussianBlur(
            stdDeviation=str(variant.glow_intensity * 4)
        )
        main_glow.add(fe_gaussian_blur_main)

        # Effet de fusion pour la lueur
        fe_merge_main = svgwrite.filters._feMerge(["SourceGraphic"])
        fe_merge_main.add(svgwrite.filters._feMergeNode())
        fe_merge_main.add(svgwrite.filters._feMergeNode())
        main_glow.add(fe_merge_main)

        defs.add(main_glow)

        # Filtre de lueur secondaire pour les détails
        detail_glow_id = f"detailGlow-{variant.variant_type.value}"
        detail_glow = svgwrite.filters.Filter(id=detail_glow_id)

        fe_gaussian_blur_detail = svgwrite.filters._feGaussianBlur(stdDeviation="1.5")
        detail_glow.add(fe_gaussian_blur_detail)

        defs.add(detail_glow)

    def _add_organic_turbulence_filters(self, defs, variant: LogoVariant) -> None:
        """Crée des filtres de turbulence pour l'effet organique"""
        # Filtre de turbulence principal
        turbulence_id = f"turbulence-{variant.variant_type.value}"
        turbulence_filter = svgwrite.filters.Filter(id=turbulence_id)

        # Effet de turbulence pour l'organique
        fe_turbulence = svgwrite.filters._feTurbulence(
            type="fractalNoise",
            baseFrequency="0.02",
            numOctaves="3",
            seed="1",
            stitchTiles="stitch",
        )
        turbulence_filter.add(fe_turbulence)

        # Effet de déplacement pour l'organique
        fe_displacement_map = svgwrite.filters._feDisplacementMap(
            in2="SourceGraphic", scale="8"
        )
        turbulence_filter.add(fe_displacement_map)

        defs.add(turbulence_filter)

    def _add_depth_masks(self, defs, variant: LogoVariant) -> None:
        """Crée des masques pour les effets de profondeur"""
        # Masque de profondeur principal
        depth_mask_id = f"depthMask-{variant.variant_type.value}"
        depth_mask = svgwrite.masking.Mask(id=depth_mask_id)

        # Cercle de masque avec gradient
        mask_circle = svgwrite.shapes.Circle(cx="50%", cy="50%", r="45%", fill="white")
        depth_mask.add(mask_circle)

        defs.add(depth_mask)

    def _add_neural_network_gradients(self, defs, variant: LogoVariant) -> None:
        """Crée des gradients pour les réseaux neuronaux"""
        # Gradient linéaire pour les connexions
        neural_gradient_id = f"neuralGradient-{variant.variant_type.value}"
        neural_gradient = svgwrite.gradients.LinearGradient(
            id=neural_gradient_id, x1="0%", y1="0%", x2="100%", y2="100%"
        )

        # Stops du gradient neuronal
        neural_gradient.add_stop_color(
            offset="0%", color=variant.colors.primary, opacity=1.0
        )
        neural_gradient.add_stop_color(
            offset="100%", color=variant.colors.accent, opacity=0.6
        )

        defs.add(neural_gradient)

    def add_advanced_halo(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute un halo ultra-avancé avec effets multiples"""
        center = size // 2
        radius = size // 2 - 15

        # Halo principal avec gradient
        main_halo = svgwrite.shapes.Circle(
            cx=center,
            cy=center,
            r=str(radius),
            fill="none",
            stroke=f"url(#borderGradient-{variant.variant_type.value})",
            stroke_width="3",
            opacity=variant.glow_intensity,
            filter=f"url(#mainGlow-{variant.variant_type.value})",
        )

        # Animation de respiration avancée
        main_halo.add(
            svgwrite.animate.Animate(
                attributeName="opacity",
                values=f"{variant.glow_intensity};"
                f"{variant.glow_intensity * 0.3};"
                f"{variant.glow_intensity}",
                dur=f"{4 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        drawing.add(main_halo)

        # Halo secondaire avec effet de pulsation
        secondary_halo = svgwrite.shapes.Circle(
            cx=center,
            cy=center,
            r=str(radius + 5),
            fill="none",
            stroke=variant.colors.glow,
            stroke_width="1",
            opacity=0.4,
            filter=f"url(#detailGlow-{variant.variant_type.value})",
        )

        # Animation de pulsation
        secondary_halo.add(
            svgwrite.animate.Animate(
                attributeName="r",
                values=f"{radius + 5};{radius + 15};{radius + 5}",
                dur=f"{3 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        drawing.add(secondary_halo)

    def add_advanced_moon_core(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute un noyau lunaire ultra-avancé avec effets multiples"""
        center = size // 2
        radius = size // 3

        # Lune principale avec gradient avancé
        main_moon = svgwrite.shapes.Circle(
            cx=center,
            cy=center,
            r=str(radius),
            fill=f"url(#advancedMoonGradient-{variant.variant_type.value})",
            filter=f"url(#mainGlow-{variant.variant_type.value})",
        )

        # Animation de pulsation avancée
        main_moon.add(
            svgwrite.animate.Animate(
                attributeName="r",
                values=f"{radius};{radius * 1.08};{radius}",
                dur=f"{2.5 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        drawing.add(main_moon)

        # Bordure lumineuse de la lune
        moon_border = svgwrite.shapes.Circle(
            cx=center,
            cy=center,
            r=str(radius + 2),
            fill="none",
            stroke=variant.colors.glow,
            stroke_width="2",
            opacity=0.6,
            filter=f"url(#detailGlow-{variant.variant_type.value})",
        )

        drawing.add(moon_border)

    def add_advanced_neural_network(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute un réseau neuronal ultra-avancé avec connexions complexes"""
        center = size // 2

        # Groupe principal du réseau
        network_group = svgwrite.container.Group(
            fill="none",
            stroke=f"url(#neuralGradient-{variant.variant_type.value})",
            stroke_width="2.5",
            opacity=0.9,
            filter=f"url(#detailGlow-{variant.variant_type.value})",
        )

        # Réseau principal avec courbes de Bézier complexes
        network_paths = self._generate_complex_neural_paths(center, size)

        for i, path_data in enumerate(network_paths):
            path = svgwrite.path.Path(d=path_data)

            # Animation de flux avancée
            path.add(
                svgwrite.animate.Animate(
                    attributeName="stroke-dashoffset",
                    values="0;-200;0",
                    dur=f"{5 / variant.animation_speed}s",
                    begin=f"{i * 0.3}s",
                    repeatCount="indefinite",
                )
            )

            # Animation d'opacité
            path.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.9;0.4;0.9",
                    dur=f"{4 / variant.animation_speed}s",
                    begin=f"{i * 0.2}s",
                    repeatCount="indefinite",
                )
            )

            network_group.add(path)

        drawing.add(network_group)

        # Nœuds neuronaux lumineux
        self._add_neural_nodes(drawing, variant, center, size)

    def _generate_complex_neural_paths(self, center: int, size: int) -> List[str]:
        """Génère des chemins neuronaux complexes avec courbes de Bézier"""
        paths = []

        # Réseau principal horizontal
        paths.append(
            f"M{center - size//3} {center} Q{center} {center - size//3} "
            f"{center + size//3} {center}"
        )
        paths.append(
            f"M{center - size//3 + 10} {center - 10} Q{center} "
            f"{center - size//3 - 10} {center + size//3 - 10} {center - 10}"
        )
        paths.append(
            f"M{center - size//3 + 20} {center + 10} Q{center} "
            f"{center - size//3 + 10} {center + size//3 - 20} {center + 10}"
        )

        # Réseau diagonal
        paths.append(
            f"M{center - size//4} {center - size//4} Q{center} {center} "
            f"{center + size//4} {center - size//4}"
        )
        paths.append(
            f"M{center - size//4} {center + size//4} Q{center} {center} "
            f"{center + size//4} {center + size//4}"
        )

        # Réseau vertical
        paths.append(
            f"M{center} {center - size//3} Q{center + size//3} {center} "
            f"{center} {center + size//3}"
        )
        paths.append(
            f"M{center - 10} {center - size//3 + 10} Q{center + size//3 - 10} "
            f"{center} {center - 10} {center + size//3 - 10}"
        )

        # Réseau circulaire
        for i in range(8):
            angle = (i * 45) * (math.pi / 180)
            radius = size // 4
            x1 = center + radius * math.cos(angle)
            y1 = center + radius * math.sin(angle)
            x2 = center + radius * math.cos(angle + math.pi / 4)
            y2 = center + radius * math.sin(angle + math.pi / 4)

            paths.append(f"M{x1} {y1} Q{center} {center} {x2} {y2}")

        return paths

    def _add_neural_nodes(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, center: int, size: int
    ) -> None:
        """Ajoute des nœuds neuronaux lumineux"""
        # Nœuds principaux
        node_positions = [
            (center - size // 3, center),
            (center + size // 3, center),
            (center, center - size // 3),
            (center, center + size // 3),
            (center - size // 4, center - size // 4),
            (center + size // 4, center - size // 4),
            (center - size // 4, center + size // 4),
            (center + size // 4, center + size // 4),
        ]

        for i, (x, y) in enumerate(node_positions):
            node = svgwrite.shapes.Circle(
                center=(x, y),
                r=3,
                fill=variant.colors.glow,
                opacity=0.8,
                filter=f"url(#detailGlow-{variant.variant_type.value})",
            )

            # Animation de scintillement
            node.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.8;1.0;0.8",
                    dur=f"{2 / variant.animation_speed}s",
                    begin=f"{i * 0.2}s",
                    repeatCount="indefinite",
                )
            )

            drawing.add(node)

    def add_advanced_lambda_core(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute un cœur Λ ultra-avancé avec effets cristallins"""
        center = size // 2
        lambda_group = svgwrite.container.Group()

        # Forme Λ principale avec gradient
        lambda_shape = svgwrite.path.Path(
            d=f"M{center - 15} {center - 25} L{center} {center - 8} "
            f"L{center + 15} {center - 25} L{center} {center} Z",
            fill=variant.colors.glow,
            filter=f"url(#mainGlow-{variant.variant_type.value})",
        )

        # Animation de rayonnement avancée
        lambda_shape.add(
            svgwrite.animate.Animate(
                attributeName="opacity",
                values="0.9;1.0;0.9",
                dur=f"{2 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        lambda_group.add(lambda_shape)

        # Rayonnement central avec effet de pulsation
        core_glow = svgwrite.shapes.Circle(
            center=(center, center - 8),
            r=8,
            fill=variant.colors.glow,
            opacity=0.9,
            filter=f"url(#mainGlow-{variant.variant_type.value})",
        )

        # Animation de pulsation avancée
        core_glow.add(
            svgwrite.animate.Animate(
                attributeName="r",
                values="8;12;8",
                dur=f"{2.5 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        lambda_group.add(core_glow)

        # Effets de lumière supplémentaires
        light_effects = svgwrite.container.Group()

        # Rayons lumineux
        for i in range(6):
            angle = (i * 60) * (math.pi / 180)
            x = center + 20 * math.cos(angle)
            y = center - 8 + 20 * math.sin(angle)

            ray = svgwrite.shapes.Circle(
                center=(x, y), r=2, fill=variant.colors.glow, opacity=0.6
            )

            # Animation de pulsation
            ray.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.6;1.0;0.6",
                    dur=f"{3 / variant.animation_speed}s",
                    begin=f"{i * 0.3}s",
                    repeatCount="indefinite",
                )
            )

            light_effects.add(ray)

        lambda_group.add(light_effects)
        drawing.add(lambda_group)

    def add_advanced_particle_effects(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute des effets de particules ultra-avancés"""
        center = size // 2

        # Particules principales
        for i in range(12):
            angle = (i * 30) * (math.pi / 180)
            radius = size // 2 - 25
            x = center + radius * math.cos(angle)
            y = center + radius * math.sin(angle)

            particle = svgwrite.shapes.Circle(
                center=(x, y),
                r=2.5,
                fill=variant.colors.glow,
                opacity=0.7,
                filter=f"url(#detailGlow-{variant.variant_type.value})",
            )

            # Animation de scintillement avancée
            particle.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.7;1.0;0.7",
                    dur=f"{2.5 / variant.animation_speed}s",
                    begin=f"{i * 0.2}s",
                    repeatCount="indefinite",
                )
            )

            # Animation de mouvement orbital
            particle.add(
                svgwrite.animate.Animate(
                    attributeName="cx",
                    values=f"{x};{x + 5 * math.cos(angle + math.pi/6)};{x}",
                    dur=f"{4 / variant.animation_speed}s",
                    begin=f"{i * 0.1}s",
                    repeatCount="indefinite",
                )
            )

            particle.add(
                svgwrite.animate.Animate(
                    attributeName="cy",
                    values=f"{y};{y + 5 * math.sin(angle + math.pi/6)};{y}",
                    dur=f"{4 / variant.animation_speed}s",
                    begin=f"{i * 0.1}s",
                    repeatCount="indefinite",
                )
            )

            drawing.add(particle)

    def build_logo(self, variant_name: str, size: int) -> svgwrite.Drawing:
        """Construit le logo avancé pour une variante donnée (méthode abstraite)"""
        variant = self.variants_manager.get_variant(variant_name)

        # Création du dessin
        drawing = self.create_drawing(size)

        # Ajout des définitions ultra-avancées
        self.add_advanced_definitions(drawing, variant)

        # Construction des éléments avec ordre de profondeur
        self.add_advanced_halo(drawing, variant, size)
        self.add_advanced_moon_core(drawing, variant, size)
        self.add_advanced_neural_network(drawing, variant, size)
        self.add_advanced_lambda_core(drawing, variant, size)
        self.add_advanced_particle_effects(drawing, variant, size)

        return drawing

    def build_advanced_logo(
        self, variant_name: str, size: int = 200
    ) -> svgwrite.Drawing:
        """Construit le logo ultra-avancé pour une variante donnée (alias pour compatibilité)"""
        return self.build_logo(variant_name, size)

    def save_advanced_logo(
        self, variant_name: str, size: int, output_path: Path
    ) -> Path:
        """Sauvegarde le logo ultra-avancé dans un fichier"""
        drawing = self.build_advanced_logo(variant_name, size)

        # Création du répertoire de sortie si nécessaire
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Sauvegarde avec gestion d'erreur avancée
        try:
            drawing.write(str(output_path))
        except Exception:
            # Fallback : sauvegarde en string puis écriture fichier
            svg_content = drawing.tostring()
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(svg_content)

        return output_path
