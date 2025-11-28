"""📱 Play Store Assets Generator Module
Générateur automatique des assets nécessaires pour la publication sur Play Store
"""

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    from PIL import Image, ImageDraw, ImageFont
    from PIL.Image import Resampling
except ImportError as e:
    raise ImportError(
        "Pillow est requis pour la génération d'assets Play Store. "
        "Installez avec: pip install pillow"
    ) from e

try:
    import cairosvg  # type: ignore[import-untyped,import-not-found]
except ImportError:
    cairosvg = None


class PlayStoreAssetsGenerator:
    """Générateur d'assets pour Google Play Store"""

    # Couleurs Arkalia CIA
    ARKALIA_BLUE = "#0175C2"
    ARKALIA_WHITE = "#FFFFFF"

    # Dimensions Play Store
    FEATURE_GRAPHIC_SIZE = (1024, 500)  # Largeur x Hauteur
    PHONE_SCREENSHOT_MAX_SIZE = (3840, 2160)  # Max pour téléphone
    PHONE_SCREENSHOT_RECOMMENDED = (1080, 1920)  # Portrait recommandé

    def __init__(
        self,
        output_dir: Optional[Path] = None,
        logo_path: Optional[Path] = None,
        screenshots_dir: Optional[Path] = None,
    ) -> None:
        """
        Initialise le générateur d'assets Play Store

        Args:
            output_dir: Répertoire de sortie pour les assets générés
            logo_path: Chemin vers le logo SVG/PNG Arkalia CIA
            screenshots_dir: Répertoire contenant les screenshots source
        """
        self.output_dir = output_dir or Path("playstore-assets")
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.logo_path = logo_path
        self.screenshots_dir = screenshots_dir or Path("docs/screenshots/android")

        # Configuration du logging
        self._setup_logging()

    def _setup_logging(self) -> None:
        """Configure le système de logging"""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        self.logger = logging.getLogger(__name__)

    def _load_logo(self, size: Tuple[int, int]) -> Optional[Image.Image]:
        """
        Charge le logo et le redimensionne

        Args:
            size: Taille cible (width, height)

        Returns:
            Image PIL ou None si le logo n'est pas trouvé
        """
        if not self.logo_path or not self.logo_path.exists():
            self.logger.warning(
                "Logo non trouvé, création d'un logo par défaut pour la feature graphic"
            )
            return self._create_default_logo(size)

        try:
            if self.logo_path.suffix.lower() == ".svg":
                # Convertir SVG en PNG
                if cairosvg is None:
                    self.logger.warning(
                        "cairosvg non disponible pour convertir SVG. "
                        "Utilisation d'un logo par défaut. "
                        "Installez avec: pip install cairosvg pour utiliser le logo SVG"
                    )
                    return self._create_default_logo(size)

                # Convertir SVG en PNG temporaire
                import tempfile

                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
                    cairosvg.svg2png(
                        url=str(self.logo_path),
                        write_to=tmp.name,
                        output_width=size[0],
                        output_height=size[1],
                    )
                    logo_img = Image.open(tmp.name)
                    Path(tmp.name).unlink()  # Nettoyer le fichier temporaire
                    return logo_img
            else:
                # Charger directement PNG/JPG
                logo_img = Image.open(self.logo_path)
                # Redimensionner en gardant le ratio
                logo_img.thumbnail(size, Resampling.LANCZOS)
                return logo_img
        except Exception as e:
            self.logger.error(f"Erreur lors du chargement du logo: {e}")
            return self._create_default_logo(size)

    def _create_default_logo(self, size: Tuple[int, int]) -> Image.Image:
        """
        Crée un logo par défaut avec le texte "Arkalia CIA"

        Args:
            size: Taille du logo (width, height)

        Returns:
            Image PIL avec le logo par défaut
        """
        img = Image.new("RGBA", size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Essayer de charger une police, sinon utiliser la police par défaut
        try:
            # Essayer différentes polices système
            font_size = min(size) // 8
            try:
                font = ImageFont.truetype(  # type: ignore[assignment]
                    "/System/Library/Fonts/Helvetica.ttc", font_size
                )
            except Exception:
                try:
                    font = ImageFont.truetype(  # type: ignore[assignment]
                        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                        font_size,
                    )
                except Exception:
                    font = ImageFont.load_default()  # type: ignore[assignment]
        except Exception:
            font = ImageFont.load_default()  # type: ignore[assignment]

        # Texte "Arkalia CIA"
        text = "Arkalia CIA"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Centrer le texte
        x = (size[0] - text_width) // 2
        y = (size[1] - text_height) // 2

        # Dessiner le texte en bleu Arkalia
        draw.text((x, y), text, fill=self.ARKALIA_BLUE, font=font)

        return img

    def generate_feature_graphic(
        self,
        output_filename: str = "feature-graphic.png",
        background_color: Optional[str] = None,
    ) -> Path:
        """
        Génère la Feature Graphic (bannière) pour Play Store (1024x500 pixels)

        Args:
            output_filename: Nom du fichier de sortie
            background_color: Couleur de fond (hex), par défaut blanc

        Returns:
            Chemin vers le fichier généré
        """
        self.logger.info("🎨 Génération de la Feature Graphic (1024x500)...")

        # Créer l'image avec un fond dégradé moderne rouge/rose
        img = Image.new("RGB", self.FEATURE_GRAPHIC_SIZE, (255, 255, 255))
        draw = ImageDraw.Draw(img)

        # Fond dégradé rouge/rose élégant pour app santé (dégradé plus prononcé)
        if background_color and background_color.upper() not in (
            "#FFFFFF",
            "#FFF",
            "WHITE",
        ):
            # Convertir hex en RGB
            hex_color = background_color.lstrip("#")
            bg_color = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
            img = Image.new("RGB", self.FEATURE_GRAPHIC_SIZE, bg_color)
            draw = ImageDraw.Draw(img)
        else:
            # Dégradé plus prononcé :
            # du rouge très foncé (#991B1B) au rose très clair (#FEE2E2)
            for y in range(self.FEATURE_GRAPHIC_SIZE[1]):
                ratio = y / self.FEATURE_GRAPHIC_SIZE[1]
                # Dégradé plus marqué avec courbe exponentielle pour effet plus doux
                eased_ratio = (
                    ratio * ratio
                )  # Courbe quadratique pour dégradé plus naturel
                r = int(153 + (254 - 153) * eased_ratio)  # 153 (#99) -> 254 (#FE)
                g = int(27 + (226 - 27) * eased_ratio)  # 27 (#1B) -> 226 (#E2)
                b = int(27 + (226 - 27) * eased_ratio)  # 27 (#1B) -> 226 (#E2)
                draw.line([(0, y), (self.FEATURE_GRAPHIC_SIZE[0], y)], fill=(r, g, b))

        # Charger le logo (taille adaptée pour la bannière)
        logo_size = (400, 400)  # Logo centré, taille raisonnable
        logo_img = self._load_logo(logo_size)

        if logo_img:
            # Centrer le logo horizontalement et verticalement (remonté)
            logo_x = (self.FEATURE_GRAPHIC_SIZE[0] - logo_img.width) // 2
            logo_y = (self.FEATURE_GRAPHIC_SIZE[1] - logo_img.height) // 2 - 60

            # Coller le logo
            if logo_img.mode == "RGBA":
                img.paste(logo_img, (logo_x, logo_y), logo_img)
            else:
                img.paste(logo_img, (logo_x, logo_y))

        # Ajouter le texte "Assistant Santé Personnel" avec style amélioré
        try:
            font_size = 56  # Texte plus grand
            try:
                font = ImageFont.truetype(
                    "/System/Library/Fonts/Helvetica.ttc", font_size
                )
            except Exception:
                try:
                    font = ImageFont.truetype(
                        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                        font_size,
                    )
                except Exception:
                    font = ImageFont.load_default()  # type: ignore[assignment]
        except Exception:
            font = ImageFont.load_default()  # type: ignore[assignment]

        text = "Assistant Santé Personnel"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Positionner le texte sous le logo (remonté pour éviter d'être coupé)
        text_x = (self.FEATURE_GRAPHIC_SIZE[0] - text_width) // 2
        if logo_img:
            # Positionner le texte plus haut, en laissant de la marge en bas
            text_y = logo_y + logo_img.height + 20  # 20px d'espacement après le logo
            # S'assurer que le texte n'est pas coupé en bas (marge de sécurité)
            max_y = self.FEATURE_GRAPHIC_SIZE[1] - text_height - 20
            text_y = int(min(text_y, max_y))
        else:
            text_y = int((self.FEATURE_GRAPHIC_SIZE[1] - text_height) // 2)

        # Ombre portée pour le texte (effet moderne et lisible)
        shadow_offset = 3
        # Dessiner l'ombre en gris foncé
        draw.text(
            (text_x + shadow_offset, text_y + shadow_offset),
            text,
            fill=(50, 50, 50),  # Gris foncé pour ombre
            font=font,
        )

        # Texte principal en blanc pour contraste avec fond rouge
        text_color = (255, 255, 255)  # Blanc pour contraste maximal
        draw.text((text_x, text_y), text, fill=text_color, font=font)

        # Sauvegarder
        output_path = self.output_dir / output_filename
        img.save(output_path, "PNG", optimize=True)
        self.logger.info(f"✅ Feature Graphic générée : {output_path}")

        return output_path

    def optimize_screenshot(
        self,
        screenshot_path: Path,
        max_width: int = 1080,
        max_height: int = 1920,
        output_filename: Optional[str] = None,
    ) -> Path:
        """
        Optimise et redimensionne un screenshot pour Play Store

        Args:
            screenshot_path: Chemin vers le screenshot source
            max_width: Largeur maximale
            max_height: Hauteur maximale
            output_filename: Nom du fichier de sortie (optionnel)

        Returns:
            Chemin vers le screenshot optimisé
        """
        if not screenshot_path.exists():
            raise FileNotFoundError(f"Screenshot non trouvé : {screenshot_path}")

        self.logger.info(f"📱 Optimisation du screenshot : {screenshot_path.name}")

        # Charger l'image
        img = Image.open(screenshot_path)

        # Convertir en RGB si nécessaire (pour JPEG)
        if img.mode in ("RGBA", "LA", "P"):
            # Créer un fond blanc pour les images transparentes
            background = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")  # type: ignore[assignment]
            background.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
            img = background  # type: ignore[assignment]
        elif img.mode != "RGB":
            img = img.convert("RGB")  # type: ignore[assignment]

        # Redimensionner si nécessaire (en gardant le ratio)
        original_width, original_height = img.size

        # Calculer les nouvelles dimensions
        ratio = min(max_width / original_width, max_height / original_height)

        if ratio < 1.0:
            # L'image est trop grande, redimensionner
            new_width = int(original_width * ratio)
            new_height = int(original_height * ratio)
            img = img.resize((new_width, new_height), Resampling.LANCZOS)  # type: ignore[assignment]
            self.logger.info(
                f"  Redimensionné de {original_width}x{original_height} "
                f"à {new_width}x{new_height}"
            )
        else:
            self.logger.info(
                f"  Taille OK : {original_width}x{original_height} "
                f"(max: {max_width}x{max_height})"
            )

        # Déterminer le nom de sortie
        if output_filename:
            output_path = self.output_dir / output_filename
        else:
            # Garder le nom original avec préfixe
            output_path = self.output_dir / f"playstore-{screenshot_path.name}"

        # Sauvegarder en JPEG (format recommandé pour Play Store)
        if output_path.suffix.lower() not in (".jpg", ".jpeg"):
            output_path = output_path.with_suffix(".jpg")

        # Qualité JPEG optimale
        img.save(output_path, "JPEG", quality=92, optimize=True)
        self.logger.info(f"✅ Screenshot optimisé : {output_path}")

        return output_path

    def generate_all_screenshots(
        self,
        max_width: int = 1080,
        max_height: int = 1920,
    ) -> List[Path]:
        """
        Optimise tous les screenshots trouvés dans le répertoire source

        Args:
            max_width: Largeur maximale
            max_height: Hauteur maximale

        Returns:
            Liste des chemins des screenshots optimisés
        """
        if not self.screenshots_dir.exists():
            self.logger.warning(
                f"Répertoire de screenshots non trouvé : {self.screenshots_dir}"
            )
            return []

        self.logger.info(
            f"📱 Optimisation de tous les screenshots dans {self.screenshots_dir}"
        )

        # Formats d'image supportés
        image_extensions = {".jpg", ".jpeg", ".png", ".webp"}

        # Trouver tous les fichiers image
        screenshot_files = [
            f
            for f in self.screenshots_dir.iterdir()
            if f.is_file() and f.suffix.lower() in image_extensions
        ]

        if not screenshot_files:
            self.logger.warning("Aucun screenshot trouvé")
            return []

        self.logger.info(f"  {len(screenshot_files)} screenshot(s) trouvé(s)")

        optimized_screenshots = []
        for screenshot_file in screenshot_files:
            try:
                optimized_path = self.optimize_screenshot(
                    screenshot_file, max_width, max_height
                )
                optimized_screenshots.append(optimized_path)
            except Exception as e:
                self.logger.error(
                    f"Erreur lors de l'optimisation de {screenshot_file}: {e}"
                )

        self.logger.info(
            f"✅ {len(optimized_screenshots)}/{len(screenshot_files)} "
            f"screenshot(s) optimisé(s)"
        )

        return optimized_screenshots

    def generate_all_assets(
        self,
        feature_graphic: bool = True,
        screenshots: bool = True,
        background_color: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Génère tous les assets Play Store nécessaires

        Args:
            feature_graphic: Générer la feature graphic
            screenshots: Optimiser les screenshots
            background_color: Couleur de fond pour la feature graphic

        Returns:
            Dictionnaire avec les chemins des assets générés
        """
        self.logger.info("🚀 Génération de tous les assets Play Store...")

        assets: Dict[str, Any] = {
            "feature_graphic": None,
            "screenshots": [],
            "output_dir": str(self.output_dir),
        }

        if feature_graphic:
            try:
                assets["feature_graphic"] = str(
                    self.generate_feature_graphic(background_color=background_color)
                )
            except Exception as e:
                self.logger.error(
                    f"Erreur lors de la génération de la feature graphic: {e}"
                )

        if screenshots:
            try:
                optimized = self.generate_all_screenshots()
                assets["screenshots"] = [str(p) for p in optimized]
            except Exception as e:
                self.logger.error(f"Erreur lors de l'optimisation des screenshots: {e}")

        self.logger.info("✅ Génération des assets terminée")
        return assets
