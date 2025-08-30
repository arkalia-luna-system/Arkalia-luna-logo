"""
🌙 Logo Generator Module
Générateur principal des logos Arkalia-LUNA
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

from PIL import Image, ImageDraw

try:
    from .svg_builder_advanced import AdvancedSVGBuilder
    from .variants import LogoVariants
except ImportError:
    # Fallback pour exécution directe
    from svg_builder_advanced import AdvancedSVGBuilder
    from variants import LogoVariants


class ArkaliaLunaLogo:
    """Générateur principal des logos Arkalia-LUNA"""

    def __init__(self, output_dir: Optional[Path] = None):
        self.variants_manager = LogoVariants()
        self.svg_builder = AdvancedSVGBuilder(self.variants_manager)
        self.output_dir = output_dir or Path("exports")
        self.output_dir.mkdir(exist_ok=True)

        # Configuration du logging
        self._setup_logging()

    def _setup_logging(self):
        """Configure le système de logging"""
        import logging

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(self.output_dir / "arkalia-luna-logo.log"),
                logging.StreamHandler(),
            ],
        )
        self.logger = logging.getLogger(__name__)

    def generate_svg_logo(self, variant_name: str, size: int = 200) -> Path:
        """Génère un logo SVG pour une variante donnée"""
        try:
            self.logger.info(
                f"Génération du logo SVG '{variant_name}' en taille {size}x{size}"
            )

            # Validation de la variante
            if not self.variants_manager.validate_variant(variant_name):
                raise ValueError(f"Variante '{variant_name}' non reconnue")

            # Construction du chemin de sortie
            output_path = self.output_dir / f"arkalia-luna-{variant_name}-{size}.svg"

            # Génération et sauvegarde
            self.svg_builder.save_logo(variant_name, size, output_path)

            self.logger.info(f"Logo SVG généré avec succès : {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(
                f"Erreur lors de la génération du logo '{variant_name}': {e}"
            )
            raise

    def generate_all_variants(self, size: int = 200) -> List[Path]:
        """Génère toutes les variantes du logo"""
        try:
            self.logger.info(
                f"Génération de toutes les variantes en taille {size}x{size}"
            )

            generated_files = []
            variants = self.variants_manager.list_variants()

            for variant in variants:
                try:
                    output_path = self.generate_svg_logo(variant, size)
                    generated_files.append(output_path)
                except Exception as e:
                    self.logger.error(f"Échec de la génération pour '{variant}': {e}")
                    continue

            self.logger.info(
                f"Génération terminée : "
                f"{len(generated_files)}/{len(variants)} logos créés"
            )
            return generated_files

        except Exception as e:
            self.logger.error(
                f"Erreur lors de la génération de toutes les variantes: {e}"
            )
            raise

    def create_favicon(self, variant_name: str, size: int = 32) -> Path:
        """Crée un favicon PNG pour une variante donnée"""
        try:
            self.logger.info(
                f"Création du favicon '{variant_name}' en taille {size}x{size}"
            )

            # Validation de la variante
            variant = self.variants_manager.get_variant(variant_name)

            # Création de l'image PIL
            img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)

            # Calcul des dimensions
            center = size // 2
            radius = size // 3

            # Lune principale avec couleur primaire
            draw.ellipse(
                [center - radius, center - radius, center + radius, center + radius],
                fill=variant.colors.primary,
            )

            # Λ-core simplifié
            lambda_points = [
                (center - 3, center - 5),
                (center, center + 3),
                (center + 3, center - 5),
            ]
            draw.polygon(lambda_points, fill=variant.colors.glow)

            # Sauvegarde
            output_path = self.output_dir / f"favicon-{variant_name}-{size}.png"
            img.save(output_path, "PNG")

            self.logger.info(f"Favicon généré avec succès : {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(
                f"Erreur lors de la création du favicon '{variant_name}': {e}"
            )
            raise

    def create_favicon_all_variants(self, size: int = 32) -> List[Path]:
        """Crée des favicons pour toutes les variantes"""
        try:
            self.logger.info(
                f"Création des favicons pour toutes les variantes "
                f"en taille {size}x{size}"
            )

            generated_files = []
            variants = self.variants_manager.list_variants()

            for variant in variants:
                try:
                    output_path = self.create_favicon(variant, size)
                    generated_files.append(output_path)
                except Exception as e:
                    self.logger.error(
                        f"Échec de la création du favicon pour '{variant}': {e}"
                    )
                    continue

            self.logger.info(
                f"Création des favicons terminée : "
                f"{len(generated_files)}/{len(variants)} créés"
            )
            return generated_files

        except Exception as e:
            self.logger.error(f"Erreur lors de la création de tous les favicons: {e}")
            raise

    def get_variant_info(self, variant_name: str) -> Dict[str, Any]:
        """Récupère les informations d'une variante"""
        try:
            return self.variants_manager.get_variant_info(variant_name)
        except Exception as e:
            self.logger.error(
                f"Erreur lors de la récupération des infos de '{variant_name}': {e}"
            )
            raise

    def list_all_variants(self) -> List[str]:
        """Liste toutes les variantes disponibles"""
        return self.variants_manager.list_variants()

    def validate_variant(self, variant_name: str) -> bool:
        """Valide qu'une variante existe"""
        return self.variants_manager.validate_variant(variant_name)

    def get_output_directory(self) -> Path:
        """Récupère le répertoire de sortie"""
        return self.output_dir

    def set_output_directory(self, new_path: Path) -> None:
        """Définit un nouveau répertoire de sortie"""
        self.output_dir = Path(new_path)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.logger.info(f"Répertoire de sortie changé vers : {self.output_dir}")

    def cleanup_generated_files(self) -> int:
        """Nettoie tous les fichiers générés"""
        try:
            count = 0
            for file_path in self.output_dir.glob("arkalia-luna-*"):
                file_path.unlink()
                count += 1

            for file_path in self.output_dir.glob("favicon-*"):
                file_path.unlink()
                count += 1

            self.logger.info(f"Nettoyage terminé : {count} fichiers supprimés")
            return count

        except Exception as e:
            self.logger.error(f"Erreur lors du nettoyage : {e}")
            raise

    def get_generation_stats(self) -> Dict[str, Any]:
        """Récupère les statistiques de génération"""
        try:
            svg_files = list(self.output_dir.glob("arkalia-luna-*.svg"))
            png_files = list(self.output_dir.glob("favicon-*.png"))

            stats = {
                "total_files": len(svg_files) + len(png_files),
                "svg_logos": len(svg_files),
                "png_favicons": len(png_files),
                "output_directory": str(self.output_dir),
                "available_variants": len(self.variants_manager.list_variants()),
                "generated_variants": len(
                    {
                        f.stem.split("-")[2]
                        for f in svg_files
                        if f.stem.split("-")[2].isdigit()
                    }
                ),
            }

            return stats

        except Exception as e:
            self.logger.error(f"Erreur lors de la récupération des stats : {e}")
            raise
