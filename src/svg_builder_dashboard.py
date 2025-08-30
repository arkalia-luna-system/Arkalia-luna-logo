"""
🌙 Dashboard SVG Builder Module
Construction d'icônes dashboard/networking synthétiques selon le cahier des charges
"""

import math
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


class DashboardSVGBuilder(SVGBuilder):
    """Constructeur SVG dashboard pour des logos Arkalia-LUNA synthétiques"""

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
        """Crée un nouveau dessin SVG avec configuration dashboard"""
        if viewbox is None:
            viewbox = (0, 0, size, size)

        drawing = svgwrite.Drawing(
            size=(size, size),
            viewBox=f"{viewbox[0]} {viewbox[1]} {viewbox[2]} {viewbox[3]}",
        )

        # Configuration dashboard
        drawing.set_desc("Logo Arkalia-LUNA - Style Dashboard")
        # drawing.set_title("Arkalia-LUNA Dashboard Logo")  # Commenté car non supporté

        return drawing

    def add_dashboard_definitions(
        self, drawing: svgwrite.Drawing, variant: LogoVariant
    ) -> None:
        """Ajoute des définitions dashboard (gradients, filtres)"""
        defs = drawing.defs

        # Gradient principal
        self._add_main_gradient(defs, variant)

        # Gradient du halo
        self._add_halo_gradient(defs, variant)

        # Gradient du centre
        self._add_core_gradient(defs, variant)

        # Filtre de lueur
        self._add_glow_filter(defs, variant)

    def _add_main_gradient(self, defs, variant: LogoVariant) -> None:
        """Crée le gradient principal dashboard"""
        gradient_id = f"mainGradient-{variant.variant_type.value}"

        # Gradient radial avec 3-4 stops pour un effet synthétique
        gradient = svgwrite.gradients.RadialGradient(
            id=gradient_id, cx="50%", cy="50%", r="50%"
        )

        # Stops synthétiques (pas de textures réalistes)
        stops = [
            (0, variant.colors.primary),
            (60, variant.colors.secondary),
            (100, variant.colors.primary),
        ]

        for offset, color in stops:
            try:
                # Utilise add_stop_color directement
                gradient.add_stop_color(offset=f"{offset}%", color=color)
            except Exception:
                # Fallback sans offset
                gradient.add_stop_color(color=color)

        defs.add(gradient)

    def _add_halo_gradient(self, defs, variant: LogoVariant) -> None:
        """Crée un gradient pour le halo lumineux synthétique"""
        halo_gradient_id = f"haloGradient-{variant.variant_type.value}"
        halo_gradient = svgwrite.gradients.RadialGradient(
            id=halo_gradient_id, cx="50%", cy="50%", r="50%"
        )

        # Halo gradient avec 3 stops
        halo_gradient.add_stop_color(
            offset="0%", color=variant.colors.glow, opacity=0.8
        )
        halo_gradient.add_stop_color(
            offset="50%", color=variant.colors.glow, opacity=0.4
        )
        halo_gradient.add_stop_color(
            offset="100%", color=variant.colors.glow, opacity=0.0
        )

        defs.add(halo_gradient)

    def _add_core_gradient(self, defs, variant: LogoVariant) -> None:
        """Crée un gradient pour le centre/A-core lumineux"""
        core_gradient_id = f"coreGradient-{variant.variant_type.value}"
        core_gradient = svgwrite.gradients.RadialGradient(
            id=core_gradient_id, cx="50%", cy="50%", r="50%"
        )

        # Core gradient avec 3 stops
        core_gradient.add_stop_color(
            offset="0%", color=variant.colors.primary, opacity=1.0
        )
        core_gradient.add_stop_color(
            offset="70%", color=variant.colors.accent, opacity=0.8
        )
        core_gradient.add_stop_color(
            offset="100%", color=variant.colors.glow, opacity=0.6
        )

        defs.add(core_gradient)

    def _add_glow_filter(self, defs, variant: LogoVariant) -> None:
        """Crée un filtre de lueur dashboard"""
        filter_id = f"glow-{variant.variant_type.value}"
        glow_filter = svgwrite.filters.Filter(id=filter_id)

        # Effet de flou gaussien simple
        fe_gaussian_blur = svgwrite.filters._feGaussianBlur(
            stdDeviation=str(variant.glow_intensity * 2)
        )
        glow_filter.add(fe_gaussian_blur)

        defs.add(glow_filter)

    def add_dashboard_main_circle(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute le cercle principal avec style dashboard"""
        center = size // 2
        radius = size // 2 - 20

        # Cercle principal avec gradient
        main_circle = svgwrite.shapes.Circle(
            cx=center,
            cy=center,
            r=str(radius),
            fill=f"url(#mainGradient-{variant.variant_type.value})",
            filter=f"url(#glow-{variant.variant_type.value})",
        )

        drawing.add(main_circle)

    def add_dashboard_halo(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute le halo lumineux synthétique"""
        center = size // 2
        radius = size // 2 - 10

        # Halo principal
        main_halo = svgwrite.shapes.Circle(
            cx=center,
            cy=center,
            r=str(radius),
            fill="none",
            stroke=variant.colors.glow,
            stroke_width="2",
            opacity=0.7,
            filter=f"url(#glow-{variant.variant_type.value})",
        )

        # Animation de respiration
        main_halo.add(
            svgwrite.animate.Animate(
                attributeName="opacity",
                values="0.7;0.3;0.7",
                dur=f"{3 / variant.animation_speed}s",
                repeatCount="indefinite",
            )
        )

        drawing.add(main_halo)

        # Halo secondaire plus large
        secondary_halo = svgwrite.shapes.Circle(
            center=(center, center),
            r=radius + 10,
            fill="none",
            stroke=variant.colors.accent,
            stroke_width=1,
            opacity=0.4,
        )

        drawing.add(secondary_halo)

    def add_dashboard_core(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute le centre/A-core lumineux synthétique"""
        center = size // 2
        core_radius = size // 6

        # Centre principal avec gradient
        core = svgwrite.shapes.Circle(
            center=(center, center),
            r=core_radius,
            fill=f"url(#coreGradient-{variant.variant_type.value})",
            filter=f"url(#glow-{variant.variant_type.value})",
        )

        drawing.add(core)

        # Bordure du centre
        core_border = svgwrite.shapes.Circle(
            center=(center, center),
            r=core_radius + 1,
            fill="none",
            stroke=variant.colors.glow,
            stroke_width=1,
            opacity=0.8,
        )

        drawing.add(core_border)

    def add_dashboard_network_pattern(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute un motif réseau géométrique stylisé"""
        center = size // 2

        # Groupe pour le réseau
        network_group = svgwrite.container.Group(
            fill="none", stroke=variant.colors.accent, stroke_width=1.5, opacity=0.8
        )

        # Chemins du réseau
        network_paths = self._create_network_paths(center, size)

        for path_data in network_paths:
            path = svgwrite.path.Path(d=path_data)
            network_group.add(path)

        drawing.add(network_group)

        # Nœuds de connexion
        self._add_simple_connection_nodes(drawing, variant, center, size)

    def _create_network_paths(self, center: int, size: int) -> list:
        """Crée les chemins du réseau dashboard"""
        paths = []

        # Réseau horizontal simple
        paths.append(f"M{center - size//3} {center} L{center + size//3} {center}")
        paths.append(
            f"M{center - size//3} {center - 15} L{center + size//3} {center - 15}"
        )
        paths.append(
            f"M{center - size//3} {center + 15} L{center + size//3} {center + 15}"
        )

        # Réseau vertical simple
        paths.append(f"M{center} {center - size//3} L{center} {center + size//3}")
        paths.append(
            f"M{center - 15} {center - size//3} L{center - 15} {center + size//3}"
        )
        paths.append(
            f"M{center + 15} {center - size//3} L{center + 15} {center + size//3}"
        )

        # Réseau diagonal simple
        paths.append(
            f"M{center - size//4} {center - size//4} "
            f"L{center + size//4} {center + size//4}"
        )
        paths.append(
            f"M{center - size//4} {center + size//4} "
            f"L{center + size//4} {center - size//4}"
        )

        return paths

    def _add_simple_connection_nodes(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, center: int, size: int
    ) -> None:
        """Ajoute des nœuds de connexion simples"""
        # Nœuds principaux aux intersections
        node_positions = [
            (center, center),
            (center - size // 3, center),
            (center + size // 3, center),
            (center, center - size // 3),
            (center, center + size // 3),
            (center - size // 4, center - size // 4),
            (center + size // 4, center + size // 4),
            (center - size // 4, center + size // 4),
            (center + size // 4, center - size // 4),
        ]

        for i, (x, y) in enumerate(node_positions):
            node = svgwrite.shapes.Circle(
                center=(x, y), r=2, fill=variant.colors.glow, opacity=0.9
            )

            # Animation de scintillement simple
            node.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.9;0.3;0.9",
                    dur=f"{2 / variant.animation_speed}s",
                    begin=f"{i * 0.1}s",
                    repeatCount="indefinite",
                )
            )

            drawing.add(node)

    def add_dashboard_rays(
        self, drawing: svgwrite.Drawing, variant: LogoVariant, size: int
    ) -> None:
        """Ajoute des rayons dynamiques synthétiques"""
        center = size // 2

        # 8 rayons principaux
        for i in range(8):
            angle = (i * 45) * (math.pi / 180)
            x = center + int((size // 2 - 30) * math.cos(angle))
            y = center + int((size // 2 - 30) * math.sin(angle))

            # Rayon simple
            ray = svgwrite.shapes.Line(
                start=(center, center),
                end=(x, y),
                stroke=variant.colors.accent,
                stroke_width=1.5,
                opacity=0.6,
            )

            # Animation de pulsation
            ray.add(
                svgwrite.animate.Animate(
                    attributeName="opacity",
                    values="0.6;1.0;0.6",
                    dur=f"{3 / variant.animation_speed}s",
                    begin=f"{i * 0.2}s",
                    repeatCount="indefinite",
                )
            )

            drawing.add(ray)

    def build_logo(self, variant_name: str, size: int) -> svgwrite.Drawing:
        """Construit le logo dashboard pour une variante donnée (méthode abstraite)"""
        variant = self.variants_manager.get_variant(variant_name)

        # Création du dessin
        drawing = self.create_drawing(size)

        # Ajout des définitions
        self.add_dashboard_definitions(drawing, variant)

        # Construction des éléments
        self.add_dashboard_main_circle(drawing, variant, size)
        self.add_dashboard_halo(drawing, variant, size)
        self.add_dashboard_core(drawing, variant, size)
        self.add_dashboard_network_pattern(drawing, variant, size)
        self.add_dashboard_rays(drawing, variant, size)

        return drawing

    def build_dashboard_logo(
        self, variant_name: str, size: int = 200
    ) -> svgwrite.Drawing:
        """Construit le logo dashboard pour une variante donnée (alias pour compatibilité)"""
        return self.build_logo(variant_name, size)

    def save_dashboard_logo(
        self, variant_name: str, size: int, output_path: Path
    ) -> Path:
        """Sauvegarde le logo dashboard dans un fichier"""
        drawing = self.build_dashboard_logo(variant_name, size)

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
