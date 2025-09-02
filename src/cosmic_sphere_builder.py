"""
🌌 Cosmic Sphere SVG Builder
Builder spécialisé pour créer des logos avec sphères cosmiques lumineuses
Inspiré des images d'inspiration de l'utilisateur
"""

import math
from pathlib import Path
from typing import Dict

import svgwrite

from .svg_builder_base import SVGBuilder


class CosmicSphereBuilder(SVGBuilder):
    """Builder pour logos avec sphères cosmiques et réseaux neuronaux"""

    def __init__(self):
        super().__init__()
        self.builder_type = "cosmic_sphere"

    def build_logo(
        self, variant_name: str, size: int = 200, output_dir: Path = None
    ) -> str:
        """Construit un logo avec sphère cosmique lumineuse"""
        try:
            # Validation et optimisation des paramètres
            size = self._validate_size_parameters(size)

            # Configuration de base
            center_x, center_y = size // 2, size // 2
            sphere_radius = size * 0.35

            # Création du SVG
            dwg = svgwrite.Drawing(
                size=(f"{size}px", f"{size}px"),
                viewBox=f"0 0 {size} {size}",
                profile="full",
            )

            # Définition des gradients et filtres
            self._add_cosmic_gradients(dwg, size, variant_name)
            self._add_glow_filters(dwg)

            # Fond cosmique
            self._add_cosmic_background(dwg, size, variant_name)

            # Sphère principale
            self._add_cosmic_sphere(
                dwg, center_x, center_y, sphere_radius, variant_name
            )

            # Réseau neuronal interne
            self._add_neural_network(
                dwg, center_x, center_y, sphere_radius, variant_name
            )

            # Cristal central
            self._add_central_crystal(
                dwg, center_x, center_y, sphere_radius * 0.3, variant_name
            )

            # Particules cosmiques
            self._add_cosmic_particles(dwg, size, variant_name)

            # Halo lumineux
            self._add_luminous_halo(
                dwg, center_x, center_y, sphere_radius * 1.4, variant_name
            )

            return dwg.tostring()

        except Exception as e:
            self.logger.error(f"Erreur construction sphère cosmique: {e}")
            raise

    def _add_cosmic_gradients(
        self, dwg: svgwrite.Drawing, size: int, variant_name: str
    ):
        """Ajoute les gradients cosmiques"""

        # Gradient principal de la sphère
        sphere_gradient = dwg.defs.add(
            dwg.radialGradient(id="sphere_gradient", cx="50%", cy="30%", r="70%")
        )

        # Couleurs selon la variante
        colors = self._get_variant_colors(variant_name)

        sphere_gradient.add_stop_color(0, colors["center"], opacity=0.9)
        sphere_gradient.add_stop_color(0.4, colors["mid"], opacity=0.8)
        sphere_gradient.add_stop_color(0.7, colors["edge"], opacity=0.6)
        sphere_gradient.add_stop_color(1, colors["outer"], opacity=0.3)

        # Gradient du cristal central
        crystal_gradient = dwg.defs.add(
            dwg.linearGradient(
                id="crystal_gradient", x1="0%", y1="0%", x2="100%", y2="100%"
            )
        )
        crystal_gradient.add_stop_color(0, "#ffffff", opacity=1.0)
        crystal_gradient.add_stop_color(0.5, colors["center"], opacity=0.9)
        crystal_gradient.add_stop_color(1, colors["accent"], opacity=0.8)

    def _add_glow_filters(self, dwg: svgwrite.Drawing):
        """Ajoute les filtres de glow simplifiés"""

        # Filtre de glow principal (simplifié)
        dwg.defs.add(dwg.filter(id="glow"))

        # Filtre de glow intense (simplifié)
        dwg.defs.add(dwg.filter(id="intense_glow"))

    def _add_cosmic_background(
        self, dwg: svgwrite.Drawing, size: int, variant_name: str
    ):
        """Ajoute le fond cosmique avec étoiles"""

        # Fond dégradé cosmique
        bg_gradient = dwg.defs.add(
            dwg.radialGradient(id="cosmic_bg", cx="50%", cy="50%", r="80%")
        )
        bg_gradient.add_stop_color(0, "#000011", opacity=0.8)
        bg_gradient.add_stop_color(0.7, "#000033", opacity=0.6)
        bg_gradient.add_stop_color(1, "#000000", opacity=1.0)

        dwg.add(
            dwg.rect(
                insert=(0, 0), size=(f"{size}px", f"{size}px"), fill="url(#cosmic_bg)"
            )
        )

        # Étoiles cosmiques (optimisé pour performance)
        star_count = min(50, max(20, int(size / 8)))
        for _ in range(star_count):
            x = self._random_float(0, size)
            y = self._random_float(0, size)
            star_size = self._random_float(0.5, 2)
            opacity = self._random_float(0.3, 0.8)

            dwg.add(
                dwg.circle(center=(x, y), r=star_size, fill="#ffffff", opacity=opacity)
            )

    def _add_cosmic_sphere(
        self, dwg: svgwrite.Drawing, cx: int, cy: int, radius: float, variant_name: str
    ):
        """Ajoute la sphère cosmique principale"""

        # Sphère principale
        dwg.add(
            dwg.circle(
                center=(cx, cy), r=radius, fill="url(#sphere_gradient)", opacity=0.9
            )
        )

        # Texture de surface
        self._add_sphere_texture(dwg, cx, cy, radius, variant_name)

    def _add_sphere_texture(
        self, dwg: svgwrite.Drawing, cx: int, cy: int, radius: float, variant_name: str
    ):
        """Ajoute la texture de surface de la sphère"""

        # Crateres et reliefs (optimisé pour performance)
        crater_count = min(8, max(4, int(radius / 20)))  # Adaptatif selon la taille
        for _ in range(crater_count):
            angle = self._random_float(0, 2 * math.pi)
            distance = self._random_float(0.3, 0.8) * radius
            crater_x = cx + distance * math.cos(angle)
            crater_y = cy + distance * math.sin(angle)
            crater_size = self._random_float(radius * 0.05, radius * 0.15)

            dwg.add(
                dwg.ellipse(
                    center=(crater_x, crater_y),
                    r=(crater_size, crater_size * 0.7),
                    fill="#000000",
                    opacity=0.2,
                )
            )

    def _add_neural_network(
        self, dwg: svgwrite.Drawing, cx: int, cy: int, radius: float, variant_name: str
    ):
        """Ajoute le réseau neuronal interne"""

        colors = self._get_variant_colors(variant_name)

        # Nœuds du réseau (optimisé pour performance)
        nodes = []
        node_count = min(15, max(8, int(radius / 15)))  # Adaptatif selon la taille
        for _ in range(node_count):
            angle = self._random_float(0, 2 * math.pi)
            distance = self._random_float(0.2, 0.9) * radius
            node_x = cx + distance * math.cos(angle)
            node_y = cy + distance * math.sin(angle)
            nodes.append((node_x, node_y))

        # Connexions entre nœuds
        for i, (x1, y1) in enumerate(nodes):
            for _j, (x2, y2) in enumerate(nodes[i + 1 :], i + 1):
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if distance < radius * 0.8:  # Connexion si assez proche
                    opacity = max(0.1, 1.0 - distance / (radius * 0.8))
                    dwg.add(
                        dwg.line(
                            start=(x1, y1),
                            end=(x2, y2),
                            stroke=colors["neural"],
                            stroke_width=1.5,
                            opacity=opacity * 0.6,
                        )
                    )

        # Nœuds lumineux
        for x, y in nodes:
            node_size = self._random_float(1, 3)
            dwg.add(
                dwg.circle(
                    center=(x, y), r=node_size, fill=colors["neural"], opacity=0.8
                )
            )

    def _add_central_crystal(
        self, dwg: svgwrite.Drawing, cx: int, cy: int, size: float, variant_name: str
    ):
        """Ajoute le cristal central brillant"""

        # Cristal en forme de diamant
        crystal_points = [
            (cx, cy - size),  # Haut
            (cx + size * 0.6, cy),  # Droite
            (cx, cy + size),  # Bas
            (cx - size * 0.6, cy),  # Gauche
        ]

        dwg.add(
            dwg.polygon(
                points=crystal_points, fill="url(#crystal_gradient)", opacity=0.95
            )
        )

        # Facettes du cristal
        for i, (x, y) in enumerate(crystal_points):
            next_i = (i + 1) % len(crystal_points)
            next_x, next_y = crystal_points[next_i]

            # Ligne de facette
            dwg.add(
                dwg.line(
                    start=(cx, cy),
                    end=(x, y),
                    stroke="#ffffff",
                    stroke_width=1,
                    opacity=0.7,
                )
            )

    def _add_cosmic_particles(
        self, dwg: svgwrite.Drawing, size: int, variant_name: str
    ):
        """Ajoute les particules cosmiques flottantes"""

        colors = self._get_variant_colors(variant_name)

        # Particules adaptatives selon la taille
        particle_count = min(30, max(15, int(size / 10)))
        for _ in range(particle_count):
            x = self._random_float(0, size)
            y = self._random_float(0, size)
            particle_size = self._random_float(0.5, 2)
            opacity = self._random_float(0.2, 0.6)

            dwg.add(
                dwg.circle(
                    center=(x, y),
                    r=particle_size,
                    fill=colors["particles"],
                    opacity=opacity,
                )
            )

    def _add_luminous_halo(
        self, dwg: svgwrite.Drawing, cx: int, cy: int, radius: float, variant_name: str
    ):
        """Ajoute le halo lumineux autour de la sphère"""

        colors = self._get_variant_colors(variant_name)

        # Halo principal
        dwg.add(
            dwg.circle(
                center=(cx, cy),
                r=radius,
                fill="none",
                stroke=colors["halo"],
                stroke_width=2,
                opacity=0.4,
            )
        )

        # Halo secondaire
        dwg.add(
            dwg.circle(
                center=(cx, cy),
                r=radius * 0.7,
                fill="none",
                stroke=colors["halo"],
                stroke_width=1,
                opacity=0.6,
            )
        )

    def _get_variant_colors(self, variant_name: str) -> Dict[str, str]:
        """Retourne les couleurs selon la variante émotionnelle"""

        color_schemes = {
            "serenity": {
                "center": "#4A90E2",  # Bleu clair
                "mid": "#357ABD",  # Bleu moyen
                "edge": "#2E5A87",  # Bleu foncé
                "outer": "#1A365D",  # Bleu très foncé
                "neural": "#87CEEB",  # Bleu ciel
                "particles": "#B0E0E6",  # Bleu poudre
                "halo": "#4A90E2",  # Bleu clair
                "accent": "#E6F3FF",  # Bleu très clair
            },
            "power": {
                "center": "#FF6B6B",  # Rouge vif
                "mid": "#E74C3C",  # Rouge
                "edge": "#C0392B",  # Rouge foncé
                "outer": "#8B0000",  # Rouge très foncé
                "neural": "#FFB6C1",  # Rose clair
                "particles": "#FFE4E1",  # Rose poudre
                "halo": "#FF6B6B",  # Rouge vif
                "accent": "#FFF0F0",  # Rouge très clair
            },
            "mystery": {
                "center": "#9B59B6",  # Violet
                "mid": "#8E44AD",  # Violet foncé
                "edge": "#6A1B9A",  # Violet très foncé
                "outer": "#4A148C",  # Violet profond
                "neural": "#DDA0DD",  # Prune
                "particles": "#E6E6FA",  # Lavande
                "halo": "#9B59B6",  # Violet
                "accent": "#F3E5F5",  # Violet très clair
            },
            "awakening": {
                "center": "#F39C12",  # Orange
                "mid": "#E67E22",  # Orange foncé
                "edge": "#D35400",  # Orange très foncé
                "outer": "#A0522D",  # Orange profond
                "neural": "#FFD700",  # Or
                "particles": "#FFF8DC",  # Beige
                "halo": "#F39C12",  # Orange
                "accent": "#FFF5E6",  # Orange très clair
            },
            "creative": {
                "center": "#E91E63",  # Rose vif
                "mid": "#C2185B",  # Rose foncé
                "edge": "#880E4F",  # Rose très foncé
                "outer": "#4A148C",  # Rose profond
                "neural": "#FF69B4",  # Rose chaud
                "particles": "#FFB6C1",  # Rose clair
                "halo": "#E91E63",  # Rose vif
                "accent": "#FCE4EC",  # Rose très clair
            },
        }

        return color_schemes.get(variant_name, color_schemes["serenity"])

    def _random_float(self, min_val: float, max_val: float) -> float:
        """Génère un nombre aléatoire entre min et max"""
        import random

        return random.uniform(min_val, max_val)

    def _validate_size_parameters(self, size: int) -> int:
        """Valide et optimise les paramètres de taille"""
        # Limites de performance
        min_size, max_size = 50, 2000
        if size < min_size:
            self.logger.warning(f"Taille {size} trop petite, utilisation de {min_size}")
            return min_size
        elif size > max_size:
            self.logger.warning(f"Taille {size} trop grande, utilisation de {max_size}")
            return max_size
        return size

    def save_logo(
        self, svg_content: str, output_path: Path, variant_name: str = ""
    ) -> None:
        """Sauvegarde le contenu SVG dans un fichier"""
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(svg_content)
            self.logger.info(f"Logo cosmique sauvegardé : {output_path}")
        except Exception as e:
            self.logger.error(f"Erreur sauvegarde logo cosmique : {e}")
            raise
