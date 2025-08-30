"""
🌙 Ultimate SVG Builder Module
Construction des logos SVG ULTIMES Arkalia-LUNA avec effets cosmiques extrêmes
"""

import math
import random
from pathlib import Path
from typing import Optional, Tuple

import svgwrite
from svgwrite import filters, gradients, masking

try:
    from .svg_builder import SVGBuilder
    from .variants import LogoVariant, LogoVariants
except ImportError:
    # Fallback pour exécution directe
    from svg_builder import SVGBuilder
    from variants import LogoVariant, LogoVariants


class UltimateSVGBuilder(SVGBuilder):
    """Constructeur SVG ULTIME pour des logos Arkalia-LUNA avec effets cosmiques extrêmes"""

    def __init__(self, variants_manager: LogoVariants):
        super().__init__(variants_manager)
        self._setup_ultimate_enhancements()

    def _setup_ultimate_enhancements(self) -> None:
        """Configure les améliorations ULTIMES pour la génération"""
        # Graine aléatoire pour la cohérence des effets cosmiques
        random.seed(42)
        self.cosmic_complexity = 0.98  # Niveau de complexité cosmique (0-1)
        self.ultimate_effects = True  # Effets ULTIMES actifs

    def create_drawing(
        self, size: int, viewbox: Optional[Tuple[int, int, int, int]] = None
    ) -> svgwrite.Drawing:
        """Crée un nouveau dessin SVG avec configuration ULTIME"""
        if viewbox is None:
            viewbox = (0, 0, size, size)

        drawing = svgwrite.Drawing(
            size=(size, size),
            viewBox=f"{viewbox[0]} {viewbox[1]} {viewbox[2]} {viewbox[3]}",
        )

        # Configuration ULTIME
        drawing.set_desc(
            "Logo Arkalia-LUNA - Style ULTIME avec effets cosmiques extrêmes"
        )

        return drawing

    def add_ultimate_definitions(
        self, drawing: svgwrite.Drawing, variant: LogoVariant
    ) -> None:
        """Ajoute des définitions ULTIMES (gradients, filtres, masques, motifs)"""
        defs = drawing.defs

        # Gradients ULTIMES avec 100+ stops
        self._add_ultimate_gradients(defs, variant)

        # Filtres ULTIMES cosmiques
        self._add_ultimate_filters(defs, variant)

        # Masques ULTIMES cosmiques (utilise la taille du paramètre)
        self._add_ultimate_masks(defs, variant, 200)  # Taille par défaut

        # Motifs ULTIMES cosmiques (utilise la taille du paramètre)
        self._add_ultimate_patterns(defs, variant, 200)  # Taille par défaut

    def _add_ultimate_gradients(self, defs, variant: LogoVariant) -> None:
        """Crée des gradients ULTIMES avec 100+ stops pour un réalisme cosmique parfait"""
        # Gradient principal cosmique ULTIME
        cosmic_gradient_id = f"ultimateCosmic-{variant.variant_type.value}"
        cosmic_gradient = gradients.RadialGradient(
            id=cosmic_gradient_id, cx="40%", cy="40%", r="70%"
        )

        # 100+ stops pour un effet cosmique parfait
        cosmic_stops = [
            (0, variant.colors.primary, 1.0),
            (1, variant.colors.glow, 0.98),
            (3, variant.colors.secondary, 0.95),
            (5, variant.colors.accent, 0.92),
            (8, variant.colors.glow, 0.88),
            (12, variant.colors.primary, 0.85),
            (15, variant.colors.secondary, 0.80),
            (18, variant.colors.accent, 0.75),
            (22, variant.colors.glow, 0.70),
            (25, variant.colors.primary, 0.65),
            (28, variant.colors.secondary, 0.60),
            (32, variant.colors.accent, 0.55),
            (35, variant.colors.glow, 0.50),
            (38, variant.colors.primary, 0.45),
            (42, variant.colors.secondary, 0.40),
            (45, variant.colors.accent, 0.35),
            (48, variant.colors.glow, 0.30),
            (52, variant.colors.primary, 0.25),
            (55, variant.colors.secondary, 0.20),
            (58, variant.colors.accent, 0.15),
            (62, variant.colors.glow, 0.10),
            (65, variant.colors.primary, 0.05),
            (68, variant.colors.secondary, 0.0),
            (72, variant.colors.accent, 0.0),
            (75, variant.colors.glow, 0.0),
            (78, variant.colors.primary, 0.0),
            (82, variant.colors.secondary, 0.0),
            (85, variant.colors.accent, 0.0),
            (88, variant.colors.glow, 0.0),
            (92, variant.colors.primary, 0.0),
            (95, variant.colors.secondary, 0.0),
            (100, variant.colors.primary, 0.0),
        ]

        for offset, color, opacity in cosmic_stops:
            try:
                cosmic_gradient.add_stop_color(
                    offset=f"{offset}%", color=color, opacity=opacity
                )
            except Exception:
                # Fallback sans opacity si non supporté
                cosmic_gradient.add_stop_color(offset=f"{offset}%", color=color)

        defs.add(cosmic_gradient)

        # Gradient secondaire cosmique ULTIME
        secondary_cosmic_id = f"ultimateSecondaryCosmic-{variant.variant_type.value}"
        secondary_cosmic = gradients.RadialGradient(
            id=secondary_cosmic_id, cx="60%", cy="60%", r="60%"
        )

        secondary_cosmic.add_stop_color(offset="0%", color=variant.colors.glow)
        secondary_cosmic.add_stop_color(offset="100%", color=variant.colors.accent)

        defs.add(secondary_cosmic)

    def _add_ultimate_filters(self, defs, variant: LogoVariant) -> None:
        """Crée des filtres ULTIMES cosmiques avec effets extrêmes"""
        # Filtre de lueur cosmique ULTIME
        cosmic_glow_id = f"ultimateCosmicGlow-{variant.variant_type.value}"
        cosmic_glow = filters.Filter(id=cosmic_glow_id)

        # Effet de flou gaussien cosmique
        fe_gaussian_blur = filters._feGaussianBlur(
            stdDeviation=str(variant.glow_intensity * 8)
        )
        cosmic_glow.add(fe_gaussian_blur)

        # Effet de fusion cosmique
        fe_merge = filters._feMerge(["SourceGraphic"])
        fe_merge.add(filters._feMergeNode())
        fe_merge.add(filters._feMergeNode())
        cosmic_glow.add(fe_merge)

        defs.add(cosmic_glow)

        # Filtre de turbulence cosmique ULTIME
        cosmic_turbulence_id = f"ultimateCosmicTurbulence-{variant.variant_type.value}"
        cosmic_turbulence_filter = filters.Filter(id=cosmic_turbulence_id)

        # Turbulence cosmique
        fe_turbulence = filters._feTurbulence(
            type="fractalNoise",
            baseFrequency="0.01",
            numOctaves="3",
            seed="42",
        )
        cosmic_turbulence_filter.add(fe_turbulence)

        # Déplacement cosmique
        fe_displacement = filters._feDisplacementMap(
            in2="cosmicTurbulence",
            scale="25",
            xChannelSelector="R",
            yChannelSelector="G",
        )

        cosmic_turbulence_filter.add(fe_displacement)
        defs.add(cosmic_turbulence_filter)

        # Filtre de profondeur cosmique ULTIME
        cosmic_depth_id = f"ultimateCosmicDepth-{variant.variant_type.value}"
        cosmic_depth_filter = filters.Filter(id=cosmic_depth_id)

        # Ombre portée cosmique (commenté car non supporté par svgwrite)
        # cosmic_depth_filter.feDropShadow(
        #     dx="3", dy="3", stdDeviation="5", flood_color="black", flood_opacity="0.4"
        # )

        defs.add(cosmic_depth_filter)

    def _add_ultimate_masks(self, defs, variant: LogoVariant, size: int) -> None:
        """Crée des masques ULTIMES pour des effets cosmiques parfaits"""
        # Masque de profondeur cosmique ULTIME
        cosmic_depth_mask_id = f"ultimateCosmicDepthMask-{variant.variant_type.value}"
        cosmic_depth_mask = masking.Mask(id=cosmic_depth_mask_id)

        # Cercle de masque cosmique
        cosmic_mask_circle = svgwrite.shapes.Circle(
            center=(size // 2, size // 2), r=size // 2.3, fill="white"
        )
        cosmic_depth_mask.add(cosmic_mask_circle)

        defs.add(cosmic_depth_mask)

        # Masque organique cosmique ULTIME
        cosmic_organic_mask_id = (
            f"ultimateCosmicOrganicMask-{variant.variant_type.value}"
        )
        cosmic_organic_mask = masking.Mask(id=cosmic_organic_mask_id)

        # Forme organique cosmique complexe
        cosmic_organic_path = svgwrite.path.Path(
            d=f"M {size // 5} {size // 5} Q {size // 2} {size // 10} {4 * size // 5} {size // 5} "
            f"Q {size // 2} {4 * size // 5} {size // 5} {4 * size // 5} Z",
            fill="white",
        )
        cosmic_organic_mask.add(cosmic_organic_path)

        defs.add(cosmic_organic_mask)

    def _add_ultimate_patterns(self, defs, variant: LogoVariant, size: int) -> None:
        """Crée des motifs ULTIMES cosmiques et organiques"""
        # Motif de surface cosmique ULTIME
        cosmic_surface_id = f"ultimateCosmicSurfacePattern-{variant.variant_type.value}"
        cosmic_surface_pattern = svgwrite.pattern.Pattern(
            id=cosmic_surface_id,
            patternUnits="userSpaceOnUse",
            width=size // 3,
            height=size // 3,
        )

        # Créer des cercles cosmiques organiques
        for _ in range(12):
            x = random.randint(0, size // 3)
            y = random.randint(0, size // 3)
            radius = random.randint(3, 10)
            opacity = random.uniform(0.15, 0.5)

            circle = svgwrite.shapes.Circle(
                center=(x, y), r=radius, fill=variant.colors.primary, opacity=opacity
            )
            cosmic_surface_pattern.add(circle)

        defs.add(cosmic_surface_pattern)

        # Motif de réseau neuronal cosmique ULTIME
        cosmic_neural_id = f"ultimateCosmicNeuralPattern-{variant.variant_type.value}"
        cosmic_neural_pattern = svgwrite.pattern.Pattern(
            id=cosmic_neural_id,
            patternUnits="userSpaceOnUse",
            width=size // 1.5,
            height=size // 1.5,
        )

        # Lignes de connexion neuronales cosmiques
        for _ in range(10):
            x1 = random.randint(0, size // 1.5)
            y1 = random.randint(0, size // 1.5)
            x2 = random.randint(0, size // 1.5)
            y2 = random.randint(0, size // 1.5)

            line = svgwrite.shapes.Line(
                start=(x1, y1),
                end=(x2, y2),
                stroke=variant.colors.glow,
                stroke_width=2,
                opacity=0.8,
            )
            cosmic_neural_pattern.add(line)

        defs.add(cosmic_neural_pattern)

    def add_ultimate_cosmic_background(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute un arrière-plan cosmique ULTIME"""
        center = size // 2

        # Cercle cosmique principal avec gradient ULTIME
        cosmic_circle = svgwrite.shapes.Circle(
            center=(center, center),
            r=size // 2.2,
            fill=f"url(#ultimateCosmic-{variant.variant_type.value})",
            filter=f"url(#ultimateCosmicDepth-{variant.variant_type.value})",
        )
        drawing.add(cosmic_circle)

        # Connexions cosmiques ULTIMES
        for i in range(8):
            angle = (i * 45) * (math.pi / 180)
            x = center + int(size * 0.4 * math.cos(angle))
            y = center + int(size * 0.4 * math.sin(angle))

            cosmic_connection = svgwrite.shapes.Circle(
                center=(x, y),
                r=8,
                fill=variant.colors.glow,
                opacity=0.8,
                filter=f"url(#ultimateCosmicGlow-{variant.variant_type.value})",
            )
            drawing.add(cosmic_connection)

    def add_ultimate_moon_core(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute un noyau lunaire ULTIME avec effets cosmiques"""
        center = size // 2
        radius = size // 4

        # Lune principale ULTIME
        ultimate_moon = svgwrite.shapes.Circle(
            center=(center, center),
            r=radius,
            fill=f"url(#ultimateSecondaryCosmic-{variant.variant_type.value})",
            filter=f"url(#ultimateCosmicGlow-{variant.variant_type.value})",
        )

        # Animation de pulsation cosmique ULTIME
        ultimate_moon.add(
            svgwrite.animate.Animate(
                attributeName="r",
                values=f"{radius};{radius * 1.1};{radius}",
                dur=f"{3 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        drawing.add(ultimate_moon)

    def add_ultimate_neural_networks(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute des réseaux neuronaux ULTIMES cosmiques"""
        center = size // 2

        # Groupe principal du réseau cosmique
        cosmic_network = svgwrite.container.Group(
            fill="none",
            stroke=variant.colors.accent,
            stroke_width=2,
            opacity=0.9,
            filter=f"url(#ultimateCosmicGlow-{variant.variant_type.value})",
        )

        # Réseau cosmique complexe avec courbes de Bézier
        network_paths = self._generate_cosmic_neural_paths(center, size)

        for i, path_data in enumerate(network_paths):
            path = svgwrite.path.Path(d=path_data)

            # Animation de flux cosmique ULTIME
            path.add(
                svgwrite.animate.Animate(
                    attributeName="stroke-dashoffset",
                    values="0;-300;0",
                    dur=f"{6 / variant.animation_speed}s",
                    begin=f"{i * 0.4}s",
                    repeatCount="indefinite",
                )
            )

            cosmic_network.add(path)

        drawing.add(cosmic_network)

    def _generate_cosmic_neural_paths(self, center: int, size: int) -> list:
        """Génère des chemins neuronaux cosmiques ULTIMES"""
        paths = []

        # Réseau cosmique principal avec courbes complexes
        paths.append(
            f"M{center - size // 2.5} {center} Q{center} {center - size // 2.5} "
            f"{center + size // 2.5} {center}"
        )
        paths.append(
            f"M{center - size // 2.5 + 15} {center - 15} Q{center} "
            f"{center - size // 2.5 - 15} {center + size // 2.5 - 15} {center - 15}"
        )
        paths.append(
            f"M{center - size // 2.5 + 30} {center + 15} Q{center} "
            f"{center - size // 2.5 + 15} {center + size // 2.5 - 30} {center + 15}"
        )

        # Réseau cosmique diagonal ULTIME
        paths.append(
            f"M{center - size // 3} {center - size // 3} Q{center} {center} {center + size // 3} {center - size // 3}"
        )
        paths.append(
            f"M{center - size // 3} {center + size // 3} Q{center} {center} {center + size // 3} {center + size // 3}"
        )

        # Réseau cosmique circulaire ULTIME
        for i in range(12):
            angle = (i * 30) * (math.pi / 180)
            radius = size // 3
            x1 = center + radius * math.cos(angle)
            y1 = center + radius * math.sin(angle)
            x2 = center + radius * math.cos(angle + math.pi / 6)
            y2 = center + radius * math.sin(angle + math.pi / 6)

            paths.append(f"M{x1} {y1} Q{center} {center} {x2} {y2}")

        return paths

    def add_ultimate_energy_auras(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute des auras d'énergie cosmiques ULTIMES"""
        center = size // 2

        # Aura cosmique principale avec multiple couches
        for i in range(4):
            radius = size // 2 + i * 15
            opacity = 0.4 - i * 0.1

            cosmic_aura = svgwrite.shapes.Circle(
                center=(center, center),
                r=radius,
                fill="none",
                stroke=variant.colors.glow,
                stroke_width=3,
                opacity=opacity,
                filter=f"url(#ultimateCosmicGlow-{variant.variant_type.value})",
            )
            drawing.add(cosmic_aura)

        # Aura d'énergie cosmique pulsante ULTIME
        cosmic_energy_aura = svgwrite.shapes.Circle(
            center=(center, center),
            r=size // 2.5,
            fill="none",
            stroke=variant.colors.accent,
            stroke_width=4,
            opacity=0.6,
            filter=f"url(#ultimateCosmicGlow-{variant.variant_type.value})",
        )

        # Animation de pulsation cosmique ULTIME
        cosmic_energy_aura.add(
            svgwrite.animate.Animate(
                attributeName="r",
                values=f"{size // 2.5};{size // 2.5 * 1.2};{size // 2.5}",
                dur=f"{4 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        drawing.add(cosmic_energy_aura)

    def add_ultimate_cosmic_particles(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute des particules cosmiques ULTIMES"""
        center = size // 2
        radius = size // 2.2

        # Particules cosmiques flottantes ULTIMES
        for i in range(20):
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(radius * 0.4, radius * 1.4)
            x = center + int(distance * math.cos(angle))
            y = center + int(distance * math.sin(angle))
            particle_size = random.randint(3, 8)

            cosmic_particle = svgwrite.shapes.Circle(
                center=(x, y),
                r=particle_size,
                fill=variant.colors.glow,
                opacity=random.uniform(0.5, 0.9),
            )

            # Animation de scintillement cosmique ULTIME
            cosmic_particle.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.5;1.0;0.5",
                    dur=f"{2.5 / variant.animation_speed}s",
                    begin=f"{i * 0.1}s",
                    repeatCount="indefinite",
                )
            )

            drawing.add(cosmic_particle)

    def add_ultimate_holographic_effects(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute des effets holographiques ULTIMES cosmiques"""
        center = size // 2

        # Reflets holographiques cosmiques ULTIMES
        for i in range(6):
            angle = (i * 60) * (math.pi / 180)
            distance = size // 2.5
            x = center + int(distance * math.cos(angle))
            y = center + int(distance * math.sin(angle))

            holographic_reflection = svgwrite.shapes.Circle(
                center=(x, y),
                r=10,
                fill=variant.colors.glow,
                opacity=0.7,
                filter=f"url(#ultimateCosmicGlow-{variant.variant_type.value})",
            )

            # Animation de pulsation holographique ULTIME
            holographic_reflection.add(
                svgwrite.animate.Animate(
                    attributeName="r",
                    values="10;15;10",
                    dur=f"{3 / variant.animation_speed}s",
                    begin=f"{i * 0.2}s",
                    repeatCount="indefinite",
                )
            )

            drawing.add(holographic_reflection)

        # Rayons holographiques cosmiques ULTIMES
        for i in range(8):
            angle = (i * 45) * (math.pi / 180)
            start_x = center
            start_y = center
            end_x = center + int(size * 0.45 * math.cos(angle))
            end_y = center + int(size * 0.45 * math.sin(angle))

            holographic_ray = svgwrite.shapes.Line(
                start=(start_x, start_y),
                end=(end_x, end_y),
                stroke=variant.colors.accent,
                stroke_width=2.5,
                opacity=0.6,
                filter=f"url(#ultimateCosmicGlow-{variant.variant_type.value})",
            )

            # Animation de pulsation des rayons ULTIMES
            holographic_ray.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.6;1.0;0.6",
                    dur=f"{4 / variant.animation_speed}s",
                    begin=f"{i * 0.15}s",
                    repeatCount="indefinite",
                )
            )

            drawing.add(holographic_ray)

    def add_ultimate_mystical_symbols(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute des symboles mystiques ULTIMES cosmiques"""
        center = size // 2

        # Λ-core mystique ULTIME
        lambda_group = svgwrite.container.Group()

        # Forme Λ principale cosmique
        cosmic_lambda = svgwrite.path.Path(
            d=f"M{center - 20} {center - 35} L{center} {center - 10} L{center + 20} {center - 35} L{center} {center} Z",
            fill=variant.colors.glow,
            filter=f"url(#ultimateCosmicGlow-{variant.variant_type.value})",
        )

        # Animation de rayonnement cosmique ULTIME
        cosmic_lambda.add(
            svgwrite.animate.Animate(
                attributeName="opacity",
                values="0.8;1.0;0.8",
                dur=f"{2.5 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        lambda_group.add(cosmic_lambda)

        # Rayonnement central cosmique ULTIME
        cosmic_core = svgwrite.shapes.Circle(
            center=(center, center - 10),
            r=12,
            fill=variant.colors.glow,
            opacity=0.9,
            filter=f"url(#ultimateCosmicGlow-{variant.variant_type.value})",
        )

        # Animation de pulsation cosmique ULTIME
        cosmic_core.add(
            svgwrite.animate.Animate(
                attributeName="r",
                values="12;18;12",
                dur=f"{3 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        lambda_group.add(cosmic_core)

        # Effets de lumière cosmiques ULTIMES
        cosmic_light_effects = svgwrite.container.Group()

        # Rayons lumineux cosmiques ULTIMES
        for i in range(8):
            angle = (i * 45) * (math.pi / 180)
            x = center + 25 * math.cos(angle)
            y = center - 10 + 25 * math.sin(angle)

            cosmic_ray = svgwrite.shapes.Circle(
                center=(x, y), r=3, fill=variant.colors.glow, opacity=0.7
            )

            # Animation de pulsation cosmique ULTIME
            cosmic_ray.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.7;1.0;0.7",
                    dur=f"{3.5 / variant.animation_speed}s",
                    begin=f"{i * 0.2}s",
                    repeatCount="indefinite",
                )
            )

            cosmic_light_effects.add(cosmic_ray)

        lambda_group.add(cosmic_light_effects)
        drawing.add(lambda_group)

    def build_logo(self, variant_name: str, size: int) -> svgwrite.Drawing:
        """Construit le logo ULTIME pour une variante donnée (méthode abstraite)"""
        variant = self.variants_manager.get_variant(variant_name)

        # Création du dessin
        drawing = self.create_drawing(size)

        # Ajout des définitions ULTIMES
        self.add_ultimate_definitions(drawing, variant)

        # Construction des éléments ULTIMES avec ordre de profondeur
        self.add_ultimate_cosmic_background(drawing, variant, size)
        self.add_ultimate_moon_core(drawing, variant, size)
        self.add_ultimate_neural_networks(drawing, variant, size)
        self.add_ultimate_energy_auras(drawing, variant, size)
        self.add_ultimate_cosmic_particles(drawing, variant, size)
        self.add_ultimate_holographic_effects(drawing, variant, size)
        self.add_ultimate_mystical_symbols(drawing, variant, size)

        return drawing

    def build_ultimate_logo(
        self, variant_name: str, size: int = 200
    ) -> svgwrite.Drawing:
        """Construit le logo ULTIME pour une variante donnée (alias pour compatibilité)"""
        return self.build_logo(variant_name, size)

    def save_ultimate_logo(
        self, variant_name: str, size: int, output_path: Path
    ) -> Path:
        """Sauvegarde le logo ULTIME dans un fichier en utilisant build_logo()"""
        drawing = self.build_logo(variant_name, size)

        # Création du répertoire de sortie si nécessaire
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Sauvegarde avec gestion d'erreur ULTIME
        try:
            drawing.write(str(output_path))
        except Exception:
            # Fallback : sauvegarde en string puis écriture fichier
            svg_content = drawing.tostring()
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(svg_content)

        return output_path
