"""
🤖 BBIA Identity Assets Generator
Générateur pour les assets d'identité BBIA (HUD, App Icon, Speaking, Banners)
Design System complet pour l'écosystème BBIA
"""

from pathlib import Path
from typing import Optional

try:
    import cairosvg  # type: ignore[import-untyped,import-not-found]
except ImportError:
    cairosvg = None  # type: ignore[assignment]

from .logo_generator import ArkaliaLunaLogo  # type: ignore[import-untyped]


class BBIAIdentityGenerator(ArkaliaLunaLogo):
    """
    Générateur d'assets d'identité BBIA

    Génère :
    - Wireframe HUD (style hologramme Cyber-HUD)
    - Icône d'application (App Store / Play Store)
    - Interface vocale (mode Speaking avec animations)
    - Bannières GitHub / LinkedIn / Social Media
    """

    # Mapping des types d'assets vers les fichiers SVG sources
    IDENTITY_ASSETS: dict[str, str] = {
        "hud": "bbia_hud.svg",
        "app_icon": "bbia_app_icon.svg",
        "speaking": "bbia_speaking.svg",
        "github_banner": "bbia_github_banner.svg",
    }

    def __init__(self, output_dir: Optional[Path] = None) -> None:
        """Initialise le générateur d'identité BBIA"""
        super().__init__(output_dir or Path("exports") / "bbia" / "identity")

        # Chemin vers les assets d'identité
        project_root = Path(__file__).parent.parent
        self.identity_assets_path = project_root / "assets" / "identity"

        # Configuration du logging
        self.logger.info("🎨 BBIA Identity Generator initialisé")

    def _get_identity_asset_path(self, asset_type: str) -> Path:
        """
        Retourne le chemin vers un asset d'identité

        Args:
            asset_type: Type d'asset (hud, app_icon, speaking, github_banner)

        Returns:
            Chemin vers le fichier SVG source

        Raises:
            ValueError: Si le type d'asset n'est pas reconnu
            FileNotFoundError: Si le fichier source n'existe pas
        """
        if asset_type not in self.IDENTITY_ASSETS:
            raise ValueError(
                f"Type d'asset '{asset_type}' non reconnu. "
                f"Types disponibles: {list(self.IDENTITY_ASSETS.keys())}"
            )

        source_filename = self.IDENTITY_ASSETS[asset_type]
        source_path = self.identity_assets_path / source_filename

        if not source_path.exists():
            raise FileNotFoundError(
                f"Asset d'identité introuvable : {source_path}\n"
                f"Vérifiez que les assets sont dans : {self.identity_assets_path}"
            )

        return source_path

    def _load_svg_content(self, svg_path: Path) -> str:
        """Charge le contenu d'un fichier SVG"""
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
        import xml.etree.ElementTree as ET

        try:
            root = ET.fromstring(svg_content)

            # Récupérer le viewBox original
            viewbox = root.get("viewBox")
            if viewbox:
                parts = viewbox.split()
                if len(parts) == 4:
                    # Conserver le viewBox original pour le cadrage
                    root.set("width", str(target_size))
                    root.set("height", str(target_size))
            else:
                # Créer un viewBox si absent
                root.set("viewBox", f"0 0 {target_size} {target_size}")
                root.set("width", str(target_size))
                root.set("height", str(target_size))

            return ET.tostring(root, encoding="unicode")
        except Exception as e:
            self.logger.error(f"Erreur transformation SVG : {e}")
            return svg_content

    def generate_identity_asset(
        self,
        asset_type: str,
        size: Optional[int] = None,
        output_format: str = "svg",
    ) -> Path:
        """
        Génère un asset d'identité BBIA

        Args:
            asset_type: Type d'asset (hud, app_icon, speaking, github_banner)
            size: Taille cible (optionnel, utilise la taille originale si None)
            output_format: Format de sortie ('svg' ou 'png')

        Returns:
            Chemin du fichier généré
        """
        if asset_type not in self.IDENTITY_ASSETS:
            raise ValueError(
                f"Type d'asset '{asset_type}' non reconnu. "
                f"Types disponibles: {list(self.IDENTITY_ASSETS.keys())}"
            )

        self.logger.info(f"🎨 Génération asset BBIA '{asset_type}'...")

        # Charger le SVG source
        source_path = self._get_identity_asset_path(asset_type)
        svg_content = self._load_svg_content(source_path)

        # Transformer la taille si spécifiée
        if size:
            svg_content = self._transform_svg_size(svg_content, size)

        # Créer le chemin de sortie
        if size:
            output_filename = f"bbia-{asset_type}-{size}.{output_format}"
        else:
            output_filename = f"bbia-{asset_type}.{output_format}"

        output_path = self.output_dir / output_filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Sauvegarder selon le format
        if output_format == "svg":
            output_path.write_text(svg_content, encoding="utf-8")
        elif output_format == "png":
            if cairosvg is None:
                raise ImportError(
                    "cairosvg requis pour générer des PNG. "
                    "Installez avec: pip install cairosvg"
                )
            if not size:
                # Taille par défaut pour PNG
                size = 512
            # Sauvegarder temporairement le SVG transformé
            import tempfile

            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".svg", delete=False
            ) as tmp:
                tmp.write(svg_content)
                tmp_path = tmp.name
            try:
                cairosvg.svg2png(
                    url=tmp_path,
                    write_to=str(output_path),
                    output_width=size,
                    output_height=size,
                )
            finally:
                import os

                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
        else:
            raise ValueError(
                f"Format '{output_format}' non supporté. Utilisez 'svg' ou 'png'"
            )

        self.logger.info(f"✅ Asset BBIA généré : {output_path}")
        return output_path

    def generate_all_identity_assets(
        self, sizes: Optional[list[int]] = None, formats: Optional[list[str]] = None
    ) -> list[Path]:
        """
        Génère tous les assets d'identité BBIA

        Args:
            sizes: Liste des tailles à générer (défaut: [512, 1024])
            formats: Liste des formats ('svg', 'png') (défaut: ['svg'])

        Returns:
            Liste des fichiers générés
        """
        if sizes is None:
            sizes = [512, 1024]
        if formats is None:
            formats = ["svg"]

        generated_files = []

        for asset_type in self.IDENTITY_ASSETS.keys():
            for size in sizes:
                for fmt in formats:
                    try:
                        output_path = self.generate_identity_asset(
                            asset_type, size=size, output_format=fmt
                        )
                        generated_files.append(output_path)
                    except Exception as e:
                        self.logger.error(
                            f"Erreur génération asset '{asset_type}' "
                            f"taille {size} format {fmt}: {e}"
                        )
                        continue

        return generated_files

    def get_identity_stats(self) -> dict:
        """Retourne les statistiques des assets d'identité"""
        assets_available = self.identity_assets_path.exists()
        available_assets = []

        if assets_available:
            for asset_type, source_file in self.IDENTITY_ASSETS.items():
                source_path = self.identity_assets_path / source_file
                if source_path.exists():
                    available_assets.append(asset_type)

        return {
            "assets_available": assets_available,
            "assets_path": str(self.identity_assets_path),
            "available_assets": available_assets,
            "cairosvg_available": cairosvg is not None,
            "status": "ready" if assets_available else "assets_missing",
        }
