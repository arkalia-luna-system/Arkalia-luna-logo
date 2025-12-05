"""
🏆 Quest Badge Generator Module
Générateur de badges de gamification pour Arkalia Quest
Missions, achievements, niveaux, émotions LUNA
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import cairosvg  # type: ignore[import-untyped,import-not-found]
except ImportError:
    cairosvg = None  # type: ignore[assignment]

try:
    from PIL import Image, ImageDraw, ImageFont  # type: ignore[import-untyped]
except ImportError:
    Image = None  # type: ignore[assignment]
    ImageDraw = None  # type: ignore[assignment]
    ImageFont = None  # type: ignore[assignment]

import svgwrite  # type: ignore[import-untyped]

from .variants import LogoVariants  # type: ignore[import-untyped]


class QuestBadgeGenerator:
    """
    Générateur de badges de gamification pour Arkalia Quest

    Types de badges :
    - Badge Mission (128×128, 256×256)
    - Badge Achievement (128×128, 256×256)
    - Badge Niveau (64×64, 128×128)
    - Badge Émotion LUNA (128×128, 256×256)
    """

    # Dimensions des badges
    BADGE_DIMENSIONS: Dict[str, List[int]] = {
        "mission": [128, 256],
        "achievement": [128, 256],
        "level": [64, 128],
        "emotion": [128, 256],
    }

    def __init__(self, output_dir: Optional[Path] = None) -> None:
        """
        Initialise le générateur de badges

        Args:
            output_dir: Répertoire de sortie
        """
        self.output_dir = output_dir or Path("exports") / "quest" / "badges"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.variants_manager = LogoVariants()

        # Configuration du logging
        import logging

        self.logger = logging.getLogger(__name__)
        self.logger.info("🏆 Quest Badge Generator initialisé")

    def generate_badge(
        self,
        badge_type: str,
        size: int,
        variant: str = "serenity",
        text: Optional[str] = None,
        level: Optional[int] = None,
        stars: int = 0,
    ) -> Path:
        """
        Génère un badge Quest

        Args:
            badge_type: Type de badge (mission, achievement, level, emotion)
            size: Taille du badge
            variant: Variante émotionnelle
            text: Texte personnalisé
            level: Niveau (pour badge niveau)
            stars: Nombre d'étoiles (pour badge achievement)

        Returns:
            Chemin du badge généré
        """
        if badge_type not in self.BADGE_DIMENSIONS:
            raise ValueError(
                f"Type de badge '{badge_type}' non reconnu. "
                f"Types disponibles: {list(self.BADGE_DIMENSIONS.keys())}"
            )

        if size not in self.BADGE_DIMENSIONS[badge_type]:
            raise ValueError(
                f"Taille {size} non valide pour badge '{badge_type}'. "
                f"Tailles disponibles: {self.BADGE_DIMENSIONS[badge_type]}"
            )

        self.logger.info(
            f"🏆 Génération badge '{badge_type}' ({size}×{size}) variante '{variant}'"
        )

        # Récupérer la variante
        variant_obj = self.variants_manager.get_variant(variant)

        # Créer le SVG
        drawing = svgwrite.Drawing(
            size=(size, size),
            profile="tiny",
        )

        # Ajouter les définitions (gradients, filtres)
        defs = drawing.defs
        self._add_badge_gradient(defs, variant_obj, size)

        # Générer selon le type
        if badge_type == "mission":
            self._draw_mission_badge(drawing, variant_obj, size, text or "Mission")
        elif badge_type == "achievement":
            self._draw_achievement_badge(
                drawing, variant_obj, size, text or "Achievement", stars
            )
        elif badge_type == "level":
            self._draw_level_badge(drawing, variant_obj, size, level or 1)
        elif badge_type == "emotion":
            self._draw_emotion_badge(drawing, variant_obj, size, variant)

        # Sauvegarder
        output_path = (
            self.output_dir / f"quest-badge-{badge_type}-{variant}-{size}x{size}.svg"
        )
        drawing.saveas(str(output_path))

        self.logger.info(f"✅ Badge généré : {output_path}")
        return output_path

    def _add_badge_gradient(self, defs: Any, variant: Any, size: int) -> None:
        """Ajoute le gradient pour le badge"""
        gradient_id = f"badgeGradient-{variant.variant_type.value}"

        gradient = svgwrite.gradients.LinearGradient(
            id=gradient_id,
            x1="0%",
            y1="0%",
            x2="0%",
            y2="100%",
        )

        gradient.add_stop_color(offset="0%", color=variant.colors.primary, opacity=1.0)
        gradient.add_stop_color(
            offset="50%", color=variant.colors.secondary, opacity=0.9
        )
        gradient.add_stop_color(offset="100%", color=variant.colors.accent, opacity=0.8)

        defs.add(gradient)

    def _draw_mission_badge(
        self, drawing: Any, variant: Any, size: int, text: str
    ) -> None:
        """Dessine un badge mission (forme écusson)"""
        center = size // 2

        # Fond en forme d'écusson
        points = [
            (center, size * 0.1),  # Haut
            (size * 0.15, size * 0.3),  # Gauche haut
            (size * 0.15, size * 0.7),  # Gauche bas
            (center, size * 0.9),  # Bas
            (size * 0.85, size * 0.7),  # Droite bas
            (size * 0.85, size * 0.3),  # Droite haut
        ]

        drawing.add(
            drawing.polygon(
                points,
                fill=f"url(#badgeGradient-{variant.variant_type.value})",
                stroke=variant.colors.glow,
                stroke_width=2,
            )
        )

        # Texte
        font_size = size // 8
        drawing.add(
            drawing.text(
                text,
                insert=(center, center + font_size // 3),
                font_size=font_size,
                fill=variant.colors.glow,
                text_anchor="middle",
                font_family="Arial, sans-serif",
                font_weight="bold",
            )
        )

    def _draw_achievement_badge(
        self, drawing: Any, variant: Any, size: int, text: str, stars: int
    ) -> None:
        """Dessine un badge achievement (forme étoile)"""
        center = size // 2
        radius = size // 3

        # Fond circulaire
        drawing.add(
            drawing.circle(
                center=(center, center),
                r=radius,
                fill=f"url(#badgeGradient-{variant.variant_type.value})",
                stroke=variant.colors.glow,
                stroke_width=3,
            )
        )

        # Étoiles
        star_size = size // 10
        for i in range(stars):
            angle = (i * 360 / stars) - 90
            x = center + int(
                radius * 0.7 * __import__("math").cos(__import__("math").radians(angle))
            )
            y = center + int(
                radius * 0.7 * __import__("math").sin(__import__("math").radians(angle))
            )
            self._draw_star(drawing, x, y, star_size, variant.colors.glow)

        # Texte
        font_size = size // 10
        drawing.add(
            drawing.text(
                text,
                insert=(center, center + radius // 2),
                font_size=font_size,
                fill=variant.colors.glow,
                text_anchor="middle",
                font_family="Arial, sans-serif",
            )
        )

    def _draw_level_badge(
        self, drawing: Any, variant: Any, size: int, level: int
    ) -> None:
        """Dessine un badge niveau (carré avec nombre)"""
        center = size // 2
        radius = size // 3

        # Fond carré arrondi
        corner_radius = size // 8
        drawing.add(
            drawing.rect(
                insert=(center - radius, center - radius),
                size=(radius * 2, radius * 2),
                rx=corner_radius,
                ry=corner_radius,
                fill=f"url(#badgeGradient-{variant.variant_type.value})",
                stroke=variant.colors.glow,
                stroke_width=2,
            )
        )

        # Nombre
        font_size = size // 3
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

    def _draw_emotion_badge(
        self, drawing: Any, variant: Any, size: int, emotion: str
    ) -> None:
        """Dessine un badge émotion LUNA (forme lune)"""
        center = size // 2
        radius = size // 3

        # Lune (cercle avec croissant)
        drawing.add(
            drawing.circle(
                center=(center, center),
                r=radius,
                fill=f"url(#badgeGradient-{variant.variant_type.value})",
                stroke=variant.colors.glow,
                stroke_width=3,
            )
        )

        # Croissant (masque)
        drawing.add(
            drawing.circle(
                center=(center - radius // 3, center),
                r=radius * 0.8,
                fill="#000000",
            )
        )

        # Texte émotion
        font_size = size // 8
        drawing.add(
            drawing.text(
                emotion.capitalize(),
                insert=(center, center + radius // 2),
                font_size=font_size,
                fill=variant.colors.glow,
                text_anchor="middle",
                font_family="Arial, sans-serif",
            )
        )

    def _draw_star(self, drawing: Any, x: int, y: int, size: int, color: str) -> None:
        """Dessine une étoile"""
        import math

        points = []
        for i in range(10):
            angle = i * math.pi / 5 - math.pi / 2
            r = size if i % 2 == 0 else size // 2
            px = x + int(r * math.cos(angle))
            py = y + int(r * math.sin(angle))
            points.append((px, py))

        drawing.add(drawing.polygon(points, fill=color))

    def generate_all_badges(
        self,
        variant: str = "serenity",
        badge_type: Optional[str] = None,
    ) -> List[Path]:
        """
        Génère tous les badges Quest

        Args:
            variant: Variante émotionnelle
            badge_type: Type de badge (None = tous)

        Returns:
            Liste des chemins des badges générés
        """
        self.logger.info(
            f"🏆 Génération de tous les badges Quest (variante: {variant})"
        )

        generated_badges = []
        types_to_generate = [badge_type] if badge_type else self.BADGE_DIMENSIONS.keys()

        for btype in types_to_generate:
            for size in self.BADGE_DIMENSIONS[btype]:
                try:
                    badge_path = self.generate_badge(
                        badge_type=btype,
                        size=size,
                        variant=variant,
                    )
                    generated_badges.append(badge_path)
                except Exception as e:
                    self.logger.error(f"Erreur génération badge '{btype}' {size}: {e}")

        self.logger.info(f"✅ {len(generated_badges)} badges générés")
        return generated_badges
