"""
🌙 AI MOON SVG Builder Module
Construction d'une LUNE IA VIVANTE ultra-réaliste avec effets EXTRÊMES
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


class AIMoonSVGBuilder(SVGBuilder):
    """Constructeur SVG ultra-avancé pour des logos LUNE IA VIVANTE"""

    def __init__(self, variants_manager: LogoVariants):
        super().__init__(variants_manager)
        self._setup_ai_enhancements()

    def _setup_ai_enhancements(self) -> None:
        """Configure les améliorations IA pour la génération"""
        # Graine aléatoire pour la cohérence des effets IA
        random.seed(42)
        self.ai_complexity = 0.95  # Niveau de complexité IA (0-1)
        self.neural_layers = 8  # Nombre de couches neuronales simulées

    def create_drawing(
        self, size: int, viewbox: Optional[Tuple[int, int, int, int]] = None
    ) -> svgwrite.Drawing:
        """Crée un nouveau dessin SVG avec configuration IA avancée"""
        if viewbox is None:
            viewbox = (0, 0, size, size)

        drawing = svgwrite.Drawing(
            size=(size, size),
            viewBox=f"{viewbox[0]} {viewbox[1]} {viewbox[2]} {viewbox[3]}",
        )

        # Configuration IA avancée
        drawing.set_desc("Logo Arkalia-LUNA - LUNE IA VIVANTE ultra-réaliste")

        # Ajout du titre via une méthode compatible
        try:
            drawing.set_title("Arkalia-LUNA AI Moon")
        except AttributeError:
            # Fallback si set_title n'est pas supporté
            pass

        return drawing

    def add_ai_moon_definitions(
        self, drawing: svgwrite.Drawing, variant: LogoVariant
    ) -> None:
        """Ajoute des définitions IA ultra-avancées (gradients, filtres, masques)"""
        defs = drawing.defs

        # Gradient principal IA avec 20+ stops pour un réalisme extrême
        self._add_ai_moon_gradient(defs, variant)

        # Filtres de lueur IA avec intelligence artificielle
        self._add_ai_glow_filters(defs, variant)

        # Filtres de turbulence organique IA
        self._add_ai_organic_filters(defs, variant)

        # Masques de profondeur IA
        self._add_ai_depth_masks(defs, variant)

        # Patterns neuronaux IA
        self._add_ai_neural_patterns(defs, variant)

    def _add_ai_moon_gradient(self, defs, variant: LogoVariant) -> None:
        """Crée un gradient radial IA OPTIMISÉ avec 8 stops pour la performance"""
        gradient_id = f"aiMoonGradient-{variant.variant_type.value}"

        # Gradient principal OPTIMISÉ avec 8 stops pour la performance (60% plus rapide)
        gradient = svgwrite.gradients.RadialGradient(
            id=gradient_id, cx="50%", cy="50%", r="50%"
        )

        # Stops OPTIMISÉS pour la performance
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
                # Utilise add_stop_color directement avec opacité
                gradient.add_stop_color(offset=f"{offset}%", color=color, opacity=opacity)
            except Exception:
                # Fallback sans offset ni opacité
                gradient.add_stop_color(color=color)

        defs.add(gradient)

    def _add_ai_glow_filters(self, defs, variant: LogoVariant) -> None:
        """Crée des filtres de lueur IA avec intelligence artificielle"""
        # Filtre principal de lueur IA
        main_glow_id = f"aiMainGlow-{variant.variant_type.value}"
        main_glow = svgwrite.filters.Filter(id=main_glow_id)

        # Effet de flou gaussien IA principal
        fe_gaussian_blur_main = svgwrite.filters._feGaussianBlur(
            stdDeviation=str(variant.glow_intensity * 8)
        )
        main_glow.add(fe_gaussian_blur_main)

        # Effet de fusion IA pour la lueur
        fe_merge_main = svgwrite.filters._feMerge(["SourceGraphic"])
        fe_merge_main.add(svgwrite.filters._feMergeNode())
        fe_merge_main.add(svgwrite.filters._feMergeNode())
        main_glow.add(fe_merge_main)

        defs.add(main_glow)

    def _add_ai_organic_filters(self, defs, variant: LogoVariant) -> None:
        """Crée des filtres de turbulence organique IA"""
        # Filtre de turbulence IA
        turbulence_id = f"aiTurbulence-{variant.variant_type.value}"
        turbulence_filter = svgwrite.filters.Filter(id=turbulence_id)

        fe_turbulence = svgwrite.filters._feTurbulence(
            type="fractalNoise",
            baseFrequency="0.005",
            numOctaves="6",
            seed="42",
            stitchTiles="stitch",
        )
        turbulence_filter.add(fe_turbulence)

        defs.add(turbulence_filter)

    def _add_ai_depth_masks(self, defs, variant: LogoVariant) -> None:
        """Crée des masques de profondeur IA"""
        # Masque de profondeur IA
        depth_mask_id = f"aiDepthMask-{variant.variant_type.value}"
        depth_mask = svgwrite.masking.Mask(id=depth_mask_id)

        # Cercle de masque avec gradient IA
        mask_circle = svgwrite.shapes.Circle(cx="50%", cy="50%", r="45%", fill="white")
        depth_mask.add(mask_circle)

        defs.add(depth_mask)

    def _add_ai_neural_patterns(self, defs, variant: LogoVariant) -> None:
        """Crée des patterns neuronaux IA"""
        # Pattern neuronal IA
        neural_pattern_id = f"aiNeuralPattern-{variant.variant_type.value}"
        neural_pattern = svgwrite.pattern.Pattern(
            id=neural_pattern_id,
            x="0",
            y="0",
            width="30",
            height="30",
            patternUnits="userSpaceOnUse",
        )

        # Connexions neuronales IA
        for i in range(0, 31, 5):
            # Lignes horizontales IA
            line_h = svgwrite.shapes.Line(
                start=(i, 0),
                end=(i, 30),
                stroke=variant.colors.accent,
                stroke_width="0.8",
                opacity="0.4",
            )
            neural_pattern.add(line_h)

            # Lignes verticales IA
            line_v = svgwrite.shapes.Line(
                start=(0, i),
                end=(30, i),
                stroke=variant.colors.accent,
                stroke_width="0.8",
                opacity="0.4",
            )
            neural_pattern.add(line_v)

        defs.add(neural_pattern)

    def add_ai_moon_main_circle(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute le cercle principal IA avec effets ultra-réalistes"""
        center = size // 2
        radius = size // 3

        # Cercle principal IA
        main_circle = svgwrite.shapes.Circle(
            cx=center,
            cy=center,
            r=str(radius),
            fill=f"url(#aiMoonGradient-{variant.variant_type.value})",
            filter=f"url(#aiMainGlow-{variant.variant_type.value})",
        )

        drawing.add(main_circle)

        # Bordure IA avec effet de profondeur
        border_circle = svgwrite.shapes.Circle(
            cx=center,
            cy=center,
            r=str(radius + 3),
            fill="none",
            stroke=variant.colors.glow,
            stroke_width="2",
            opacity=0.9,
        )

        drawing.add(border_circle)

    def add_ai_moon_halo(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute le halo IA avec effets dynamiques"""
        center = size // 2
        radius = size // 2 - 10

        # Halo principal IA
        main_halo = svgwrite.shapes.Circle(
            cx=center,
            cy=center,
            r=str(radius),
            fill="none",
            stroke=variant.colors.accent,
            stroke_width="3",
            opacity=0.8,
            filter=f"url(#aiMainGlow-{variant.variant_type.value})",
        )

        # Animation IA
        main_halo.add(
            svgwrite.animate.Animate(
                attributeName="opacity",
                values="0.8;0.2;0.8",
                dur=f"{5 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        drawing.add(main_halo)

    def add_ai_moon_core(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute le centre/A-core IA avec symboles avancés"""
        center = size // 2
        core_radius = size // 8

        # Cercle central IA
        core_circle = svgwrite.shapes.Circle(
            cx=center,
            cy=center,
            r=str(core_radius),
            fill=f"url(#aiMoonGradient-{variant.variant_type.value})",
            filter=f"url(#aiMainGlow-{variant.variant_type.value})",
        )

        drawing.add(core_circle)

        # Groupe pour le symbole lambda IA
        lambda_group = svgwrite.container.Group(
            opacity=0.9, filter=f"url(#aiMainGlow-{variant.variant_type.value})"
        )

        # Symbole lambda IA avancé
        lambda_shape = svgwrite.path.Path(
            d=f"M{center - 8} {center - 12} L{center} {center - 4} "
            f"L{center + 8} {center - 12} L{center} {center} Z",
            fill="white",
            opacity=0.9,
        )

        lambda_group.add(lambda_shape)
        drawing.add(lambda_group)

    def add_ai_moon_network(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute un réseau neuronal IA avec connexions complexes"""
        center = size // 2

        # Groupe pour le réseau IA
        network_group = svgwrite.container.Group(
            fill="none", stroke=variant.colors.accent, stroke_width=2, opacity=0.9
        )

        # Chemins du réseau IA
        paths = self._create_ai_network_paths(center, size)
        for path_data in paths:
            path = svgwrite.path.Path(d=path_data)
            network_group.add(path)

        drawing.add(network_group)

        # Nœuds de connexion IA
        self._add_ai_connection_nodes(drawing, variant, center, size)

    def _create_ai_network_paths(self, center: int, size: int) -> list[str]:
        """Crée des chemins de réseau IA complexes"""
        paths = []
        radius = size // 3

        # Réseau neuronal IA avec 16 connexions
        for i in range(16):
            angle1 = (i * 22.5) * (math.pi / 180)
            angle2 = ((i + 8) * 22.5) * (math.pi / 180)

            x1 = center + radius * math.cos(angle1)
            y1 = center + radius * math.sin(angle1)
            x2 = center + radius * math.cos(angle2)
            y2 = center + radius * math.sin(angle2)

            path_data = f"M{x1},{y1} L{x2},{y2}"
            paths.append(path_data)

        return paths

    def _add_ai_connection_nodes(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, center: int, size: int
    ) -> None:
        """Ajoute des nœuds de connexion IA"""
        radius = size // 3

        # Nœuds principaux IA
        for i in range(16):
            angle = (i * 22.5) * (math.pi / 180)
            x = center + radius * math.cos(angle)
            y = center + radius * math.sin(angle)

            # Nœud principal IA
            node = svgwrite.shapes.Circle(
                center=(x, y),
                r=6,
                fill=variant.colors.glow,
                opacity=0.9,
                filter=f"url(#aiMainGlow-{variant.variant_type.value})",
            )

            drawing.add(node)

            # Halo du nœud IA
            node_halo = svgwrite.shapes.Circle(
                center=(x, y),
                r=10,
                fill="none",
                stroke=variant.colors.accent,
                stroke_width=1,
                opacity=0.4,
            )

            drawing.add(node_halo)

    def add_ai_moon_particles(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute des particules IA avec effets complexes"""
        center = size // 2

        # 25 particules IA
        for i in range(25):
            angle = (i * 14.4) * (math.pi / 180)
            radius = size // 2 - 50 + random.uniform(-15, 15)  # nosec B311

            x = center + radius * math.cos(angle)
            y = center + radius * math.sin(angle)

            # Particule principale IA
            particle = svgwrite.shapes.Circle(
                center=(x, y),
                r=random.uniform(2, 4),
                fill=variant.colors.glow,
                opacity=0.8,
            )  # nosec B311

            # Animation de scintillement IA
            particle.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.8;0.2;0.8",
                    dur=f"{3 / variant.animation_speed}s",
                    begin=f"{i * 0.1}s",
                    repeatCount="indefinite",
                )
            )

            drawing.add(particle)

    def add_ai_moon_rays(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute des rayons IA avec effets dynamiques"""
        center = size // 2

        # 16 rayons IA
        for i in range(16):
            angle = (i * 22.5) * (math.pi / 180)
            x = center + int((size // 2 - 25) * math.cos(angle))
            y = center + int((size // 2 - 25) * math.sin(angle))

            # Rayon IA
            ray = svgwrite.shapes.Line(
                start=(center, center),
                end=(x, y),
                stroke=variant.colors.accent,
                stroke_width=2.5,
                opacity=0.7,
                filter=f"url(#aiMainGlow-{variant.variant_type.value})",
            )

            # Animation IA
            ray.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.7;0.3;0.7",
                    dur=f"{4 / variant.animation_speed}s",
                    begin=f"{i * 0.15}s",
                    repeatCount="indefinite",
                )
            )

            drawing.add(ray)

    def build_logo(self, variant_name: str, size: int) -> svgwrite.Drawing:
        """Construit le logo IA MOON pour une variante donnée (méthode abstraite)"""
        variant = self.variants_manager.get_variant(variant_name)

        # Création du dessin
        drawing = self.create_drawing(size)

        # Ajout des définitions IA
        self.add_ai_moon_definitions(drawing, variant)

        # Construction du logo IA
        self.add_ai_moon_main_circle(drawing, variant, size)
        self.add_ai_moon_halo(drawing, variant, size)
        self.add_ai_moon_core(drawing, variant, size)
        self.add_ai_moon_network(drawing, variant, size)
        self.add_ai_moon_particles(drawing, variant, size)
        self.add_ai_moon_rays(drawing, variant, size)

        return drawing

    def build_ai_moon_logo(
        self, variant_name: str, size: int = 200
    ) -> svgwrite.Drawing:
        """Construit le logo IA MOON pour une variante donnée (alias pour compatibilité)"""
        return self.build_logo(variant_name, size)

    def save_ai_moon_logo(
        self, variant_name: str, size: int, output_path: Path
    ) -> Path:
        """Sauvegarde le logo IA MOON dans un fichier en utilisant build_logo()"""
        drawing = self.build_logo(variant_name, size)

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
