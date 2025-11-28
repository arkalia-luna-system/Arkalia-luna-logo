"""
🎮 Quest Banner Generator Module
Générateur de bannières pour Arkalia Quest
GitHub, social media, documentation
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from PIL import Image, ImageDraw, ImageFont  # type: ignore[import-untyped]
except ImportError:
    Image = None  # type: ignore[assignment]
    ImageDraw = None  # type: ignore[assignment]
    ImageFont = None  # type: ignore[assignment]

from .quest_branding_generator import QuestBrandingGenerator
from .quest_palette import QUEST_PALETTE  # type: ignore[import-untyped]


class QuestBannerGenerator:
    """
    Générateur de bannières pour Arkalia Quest

    Formats supportés :
    - GitHub header (1280×640)
    - Social preview (1200×630)
    - Twitter header (1500×500)
    - Facebook cover (1200×630)
    - LinkedIn banner (1584×396)
    - README banner (variable)
    """

    # Dimensions des bannières
    BANNER_DIMENSIONS: Dict[str, tuple[int, int]] = {
        "github": (1280, 640),
        "social": (1200, 630),
        "twitter": (1500, 500),
        "facebook": (1200, 630),
        "linkedin": (1584, 396),
        "readme": (1200, 400),
    }

    def __init__(self, output_dir: Optional[Path] = None) -> None:
        """
        Initialise le générateur de bannières

        Args:
            output_dir: Répertoire de sortie
        """
        self.output_dir = output_dir or Path("exports") / "quest" / "banners"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Générateur Quest pour les logos
        self.quest_generator = QuestBrandingGenerator(
            output_dir=self.output_dir.parent / "logos"
        )

        # Configuration du logging
        import logging

        self.logger = logging.getLogger(__name__)
        self.logger.info("🎮 Quest Banner Generator initialisé")

    def generate_banner(
        self,
        banner_type: str,
        variant: str = "serenity",
        style: str = "ultimate",
        title: Optional[str] = None,
        subtitle: Optional[str] = None,
    ) -> Path:
        """
        Génère une bannière Quest

        Args:
            banner_type: Type de bannière (github, social, twitter, etc.)
            variant: Variante émotionnelle
            style: Style de générateur
            title: Titre personnalisé
            subtitle: Sous-titre personnalisé

        Returns:
            Chemin de la bannière générée
        """
        if Image is None:
            raise ImportError(
                "PIL (Pillow) requis pour générer des bannières. "
                "Installez avec: pip install Pillow"
            )

        if banner_type not in self.BANNER_DIMENSIONS:
            raise ValueError(
                f"Type de bannière '{banner_type}' non reconnu. "
                f"Types disponibles: {list(self.BANNER_DIMENSIONS.keys())}"
            )

        width, height = self.BANNER_DIMENSIONS[banner_type]
        self.logger.info(
            f"🎮 Génération bannière '{banner_type}' "
            f"({width}×{height}) variante '{variant}'"
        )

        # Créer l'image de base
        img = Image.new("RGB", (width, height), color=QUEST_PALETTE.PRIMARY)
        draw = ImageDraw.Draw(img)

        # Dégradé de fond
        self._draw_gradient_background(draw, width, height, variant)

        # Générer le logo Quest
        logo_size = min(width, height) // 3
        logo_path = self.quest_generator.generate_svg_logo(
            variant="mark_only",
            size=logo_size,
            emotion_variant=variant,
            style=style,
        )

        # Charger et positionner le logo
        if logo_path.exists():
            # Convertir SVG en PNG temporairement
            try:
                import cairosvg  # type: ignore[import-untyped,import-not-found]

                temp_png = self.output_dir / f"temp_logo_{variant}_{logo_size}.png"
                cairosvg.svg2png(
                    url=str(logo_path),
                    write_to=str(temp_png),
                    output_width=logo_size,
                    output_height=logo_size,
                )

                logo_img = Image.open(temp_png)
                logo_x = (width - logo_size) // 2
                logo_y = height // 4
                img.paste(
                    logo_img,
                    (logo_x, logo_y),
                    logo_img if logo_img.mode == "RGBA" else None,
                )

                # Nettoyer le fichier temporaire
                temp_png.unlink()
            except Exception as e:
                self.logger.warning(f"Impossible de charger le logo : {e}")

        # Ajouter texte
        title_text = title or "Arkalia Quest"
        subtitle_text = subtitle or "Jeu éducatif intelligent pour adolescents"

        self._draw_text(
            draw,
            title_text,
            width // 2,
            height // 2 + logo_size // 2 + 20,
            size=min(width, height) // 15,
            color=QUEST_PALETTE.TEXT_PRIMARY,
        )

        self._draw_text(
            draw,
            subtitle_text,
            width // 2,
            height // 2 + logo_size // 2 + 60,
            size=min(width, height) // 25,
            color=QUEST_PALETTE.TEXT_SECONDARY,
        )

        # Sauvegarder
        output_path = (
            self.output_dir
            / f"quest-banner-{banner_type}-{variant}-{style}-{width}x{height}.png"
        )
        img.save(output_path, "PNG", optimize=True)

        self.logger.info(f"✅ Bannière générée : {output_path}")
        return output_path

    def _draw_gradient_background(
        self, draw: Any, width: int, height: int, variant: str
    ) -> None:
        """Dessine un dégradé de fond"""
        from .variants import LogoVariants

        variants_manager = LogoVariants()
        variant_obj = variants_manager.get_variant(variant)

        # Dégradé simple de haut en bas
        for y in range(height):
            ratio = y / height
            r1, g1, b1 = self._hex_to_rgb(variant_obj.colors.primary)
            r2, g2, b2 = self._hex_to_rgb(variant_obj.colors.secondary)

            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)

            draw.line([(0, y), (width, y)], fill=(r, g, b))

    def _draw_text(
        self, draw: Any, text: str, x: int, y: int, size: int, color: str
    ) -> None:
        """Dessine du texte centré"""
        try:
            # Essayer de charger une police
            if ImageFont:
                try:
                    font = ImageFont.truetype(
                        "/System/Library/Fonts/Helvetica.ttc", size
                    )
                except Exception:
                    font = ImageFont.load_default()
            else:
                font = None

            # Calculer la taille du texte
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            # Positionner centré
            text_x = x - text_width // 2
            text_y = y - text_height // 2

            # Dessiner
            rgb_color = self._hex_to_rgb(color)
            draw.text((text_x, text_y), text, fill=rgb_color, font=font)
        except Exception as e:
            self.logger.warning(f"Erreur dessin texte : {e}")

    def _hex_to_rgb(self, hex_color: str) -> tuple[int, int, int]:
        """Convertit une couleur hex en RGB"""
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    def generate_all_banners(
        self,
        variant: str = "serenity",
        style: str = "ultimate",
    ) -> List[Path]:
        """
        Génère toutes les bannières Quest

        Args:
            variant: Variante émotionnelle
            style: Style de générateur

        Returns:
            Liste des chemins des bannières générées
        """
        self.logger.info(
            f"🎮 Génération de toutes les bannières Quest "
            f"(variante: {variant}, style: {style})"
        )

        generated_banners = []
        for banner_type in self.BANNER_DIMENSIONS.keys():
            try:
                banner_path = self.generate_banner(
                    banner_type=banner_type,
                    variant=variant,
                    style=style,
                )
                generated_banners.append(banner_path)
            except Exception as e:
                self.logger.error(f"Erreur génération bannière '{banner_type}': {e}")

        self.logger.info(
            f"✅ {len(generated_banners)}/{len(self.BANNER_DIMENSIONS)} "
            f"bannières générées"
        )
        return generated_banners
