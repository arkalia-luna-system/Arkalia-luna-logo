"""
🤖 BBIA Branding Generator Module
Générateur de logos BBIA pour Reachy Mini
Intégration complète avec assets SVG sources
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Optional

try:
    import cairosvg
except ImportError:
    cairosvg = None

try:
    from PIL import Image
except ImportError:
    Image = None

try:
    from .bbia_palette import BBIA_PALETTE
    from .logo_generator import ArkaliaLunaLogo
except ImportError:
    from bbia_palette import BBIA_PALETTE
    from logo_generator import ArkaliaLunaLogo


class BBIABrandingGenerator(ArkaliaLunaLogo):
    """
    Générateur de logos BBIA pour Reachy Mini

    Fonctionnalités :
    - Génération automatique des déclinaisons (mark_only, vertical, horizontal)
    - Export multi-formats (SVG, PNG 32px, 512px, 1024px)
    - Transformation et redimensionnement des SVG sources
    - Respect du style guide BBIA
    """

    # Mapping des variantes vers les fichiers SVG sources
    VARIANT_TO_SOURCE: dict[str, str] = {
        "mark_only": "bbia_mark_only_v2_SOURCE.svg",
        "vertical": "bbia_logo_vertical_v2_SOURCE.svg",
        "horizontal": "bbia_logo_horizontal_SOURCE.svg",
    }

    def __init__(self, output_dir: Optional[Path] = None) -> None:
        # Appel du constructeur parent
        super().__init__(output_dir or Path("exports") / "bbia")

        # Chemin vers les assets BBIA (dans le projet actuel)
        project_root = Path(__file__).parent.parent
        self.bbia_assets_path = project_root / "assets" / "bbia"

        # Palette BBIA
        self.palette = BBIA_PALETTE

        # Configuration du logging
        self.logger.info("🤖 BBIA Branding Generator initialisé")

    def _get_source_svg_path(self, variant_name: str) -> Path:
        """
        Retourne le chemin vers le SVG source pour une variante

        Args:
            variant_name: Type de logo (mark_only, vertical, horizontal)

        Returns:
            Chemin vers le fichier SVG source

        Raises:
            ValueError: Si la variante n'est pas reconnue
            FileNotFoundError: Si le fichier source n'existe pas
        """
        if variant_name not in self.VARIANT_TO_SOURCE:
            raise ValueError(
                f"Variante '{variant_name}' non reconnue. "
                f"Variantes disponibles: {list(self.VARIANT_TO_SOURCE.keys())}"
            )

        source_filename = self.VARIANT_TO_SOURCE[variant_name]
        source_path = self.bbia_assets_path / source_filename

        if not source_path.exists():
            raise FileNotFoundError(
                f"Fichier source BBIA introuvable : {source_path}\n"
                f"Vérifiez que les assets sont dans : {self.bbia_assets_path}"
            )

        return source_path

    def _load_svg_content(self, svg_path: Path) -> str:
        """
        Charge le contenu d'un fichier SVG

        Args:
            svg_path: Chemin vers le fichier SVG

        Returns:
            Contenu SVG en string
        """
        return svg_path.read_text(encoding="utf-8")

    def _transform_svg_size(self, svg_content: str, target_size: int) -> str:
        """
        Transforme un SVG pour une taille cible

        Args:
            svg_content: Contenu SVG original
            target_size: Taille cible (carré)

        Returns:
            Contenu SVG transformé
        """
        try:
            root = ET.fromstring(svg_content)

            # Mettre à jour les attributs width et height
            root.set("width", str(target_size))
            root.set("height", str(target_size))

            # Mettre à jour le viewBox si présent
            viewbox = root.get("viewBox")
            if viewbox:
                # Conserver les proportions du viewBox original
                parts = viewbox.split()
                if len(parts) == 4:
                    # viewBox="0 0 width height" -> garder les proportions
                    original_width = float(parts[2])
                    original_height = float(parts[3])

                    # Calculer le viewBox pour garder les proportions
                    if original_width > original_height:
                        scale = target_size / original_width
                        new_height = original_height * scale
                        root.set("viewBox", f"0 0 {target_size} {new_height}")
                    else:
                        scale = target_size / original_height
                        new_width = original_width * scale
                        root.set("viewBox", f"0 0 {new_width} {target_size}")

            # Convertir en string
            return ET.tostring(root, encoding="unicode")
        except ET.ParseError as e:
            self.logger.error(f"Erreur parsing SVG : {e}")
            # Retourner le contenu original si erreur
            return svg_content

    def generate_svg_logo(self, variant_name: str, size: int = 200) -> Path:
        """
        Génère un logo SVG BBIA

        Args:
            variant_name: Type de logo (mark_only, vertical, horizontal)
            size: Taille du logo

        Returns:
            Chemin du fichier généré
        """
        self.logger.info(
            f"🤖 Génération logo BBIA '{variant_name}' en taille {size}x{size}"
        )

        # Charger le SVG source
        source_path = self._get_source_svg_path(variant_name)
        svg_content = self._load_svg_content(source_path)

        # Transformer la taille
        transformed_svg = self._transform_svg_size(svg_content, size)

        # Créer le chemin de sortie
        output_path = self.output_dir / f"bbia-{variant_name}-{size}.svg"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Sauvegarder
        output_path.write_text(transformed_svg, encoding="utf-8")

        self.logger.info(f"✅ Logo BBIA généré : {output_path}")
        return output_path

    def generate_png_logo(self, variant_name: str, size: int = 512) -> Optional[Path]:
        """
        Génère un logo PNG BBIA depuis le SVG

        Args:
            variant_name: Type de logo (mark_only, vertical, horizontal)
            size: Taille du logo

        Returns:
            Chemin du fichier généré ou None si cairosvg indisponible
        """
        if cairosvg is None:
            self.logger.warning(
                "cairosvg non disponible. "
                "Installez avec: pip install cairosvg pour générer des PNG"
            )
            return None

        self.logger.info(
            f"🤖 Génération logo PNG BBIA '{variant_name}' en taille {size}x{size}"
        )

        # Générer d'abord le SVG
        svg_path = self.generate_svg_logo(variant_name, size)

        # Créer le chemin PNG
        png_path = self.output_dir / f"bbia-{variant_name}-{size}.png"
        png_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            # Convertir SVG en PNG
            cairosvg.svg2png(
                url=str(svg_path),
                write_to=str(png_path),
                output_width=size,
                output_height=size,
            )
            self.logger.info(f"✅ Logo PNG BBIA généré : {png_path}")
            return png_path
        except Exception as e:
            self.logger.error(f"Erreur conversion SVG→PNG : {e}")
            return None

    def generate_all_declinations(
        self, sizes: Optional[List[int]] = None, formats: Optional[List[str]] = None
    ) -> List[Path]:
        """
        Génère toutes les déclinaisons BBIA

        Args:
            sizes: Liste des tailles à générer (défaut: [32, 512, 1024])
            formats: Liste des formats ('svg', 'png') (défaut: ['svg'])

        Returns:
            Liste des fichiers générés
        """
        if sizes is None:
            sizes = [32, 512, 1024]
        if formats is None:
            formats = ["svg"]

        declinations = ["mark_only", "vertical", "horizontal"]
        generated_files = []

        for declination in declinations:
            for size in sizes:
                try:
                    # Générer SVG
                    if "svg" in formats:
                        output_path = self.generate_svg_logo(declination, size)
                        generated_files.append(output_path)

                    # Générer PNG si demandé
                    if "png" in formats:
                        png_path = self.generate_png_logo(declination, size)
                        if png_path:
                            generated_files.append(png_path)
                except Exception as e:
                    self.logger.error(
                        f"Erreur génération déclinaison '{declination}' "
                        f"taille {size}: {e}"
                    )
                    continue

        return generated_files

    def get_bbia_stats(self) -> dict:
        """Retourne les statistiques BBIA"""
        assets_available = self.bbia_assets_path.exists()
        available_variants = []

        if assets_available:
            for variant, source_file in self.VARIANT_TO_SOURCE.items():
                source_path = self.bbia_assets_path / source_file
                if source_path.exists():
                    available_variants.append(variant)

        return {
            "assets_available": assets_available,
            "assets_path": str(self.bbia_assets_path),
            "available_variants": available_variants,
            "palette": self.palette.to_dict(),
            "status": "ready" if assets_available else "assets_missing",
            "cairosvg_available": cairosvg is not None,
        }
