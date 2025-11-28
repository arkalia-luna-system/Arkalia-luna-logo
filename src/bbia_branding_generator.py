"""
🤖 BBIA Branding Generator Module
Générateur de logos BBIA pour Reachy Mini
Intégration complète avec assets SVG sources et variantes émotionnelles
"""

import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Optional

try:
    import cairosvg  # type: ignore[import-untyped,import-not-found]
except ImportError:
    cairosvg = None  # type: ignore[assignment]

try:
    from PIL import Image  # type: ignore[import-untyped]
except ImportError:
    Image = None  # type: ignore[assignment]

from .bbia_palette import BBIA_PALETTE  # type: ignore[import-untyped]
from .bbia_variants import BBIA_VARIANTS, BBIAVariant  # type: ignore[import-untyped]
from .logo_generator import ArkaliaLunaLogo  # type: ignore[import-untyped]


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

    # SVG Master modulaires (nouvelle approche)
    MASTER_SVG_SOURCES: dict[str, str] = {
        "clean": "bbia_master_clean.svg",
        "wireframe": "bbia_master_wireframe.svg",
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
        Transforme un SVG pour une taille cible en conservant le cadrage

        Args:
            svg_content: Contenu SVG original
            target_size: Taille cible (carré)

        Returns:
            Contenu SVG transformé
        """
        try:
            root = ET.fromstring(svg_content)

            # Récupérer le viewBox original
            viewbox = root.get("viewBox")
            original_width = None
            original_height = None

            if viewbox:
                parts = viewbox.split()
                if len(parts) == 4:
                    original_width = float(parts[2])
                    original_height = float(parts[3])

            # Si pas de viewBox, essayer de récupérer depuis width/height
            if original_width is None:
                width_attr = root.get("width")
                height_attr = root.get("height")
                if width_attr and height_attr:
                    # Nettoyer les unités (px, etc.)
                    original_width = float(
                        width_attr.replace("px", "").replace("pt", "")
                    )
                    original_height = float(
                        height_attr.replace("px", "").replace("pt", "")
                    )

            # Si toujours pas de dimensions, utiliser 1024 par défaut (taille standard)
            if original_width is None:
                original_width = 1024.0
                original_height = 1024.0
                # Créer un viewBox si absent
                if not viewbox:
                    root.set(
                        "viewBox", f"0 0 {int(original_width)} {int(original_height)}"
                    )

            # IMPORTANT : Conserver le viewBox original pour garder le cadrage
            # On change seulement width/height, le SVG se redimensionne automatiquement
            root.set("width", str(target_size))
            root.set("height", str(target_size))

            # Le viewBox reste identique pour conserver le cadrage exact
            # Le navigateur/visualiseur SVG redimensionnera automatiquement

            # Convertir en string
            return ET.tostring(root, encoding="unicode")
        except ET.ParseError as e:
            self.logger.error(f"Erreur parsing SVG : {e}")
            # Retourner le contenu original si erreur
            return svg_content
        except Exception as e:
            self.logger.error(f"Erreur transformation SVG : {e}")
            return svg_content

    def _modify_master_svg(self, svg_content: str, emotion_variant: BBIAVariant) -> str:
        """
        Modifie le SVG Master via les IDs sémantiques (approche propre et modulaire)

        Modifications appliquées :
        - Couleur des pupilles (#pupil-left, #pupil-right) selon l'émotion
        - Rotation de la tête (#head-group) pour animation
        - Opacité de l'interface faciale pour état de veille
        - Couleur des antennes pour signal

        Args:
            svg_content: Contenu SVG Master (clean ou wireframe)
            emotion_variant: Variante émotionnelle BBIA

        Returns:
            Contenu SVG modifié
        """
        try:
            root = ET.fromstring(svg_content)

            # 1. Modifier les pupilles (couleur selon l'émotion)
            pupil_left = root.find(".//*[@id='pupil-left']")
            pupil_right = root.find(".//*[@id='pupil-right']")

            if pupil_left is not None:
                pupil_left.set("fill", emotion_variant.colors.glow)
            if pupil_right is not None:
                pupil_right.set("fill", emotion_variant.colors.glow)

            # 2. Ajouter animation de pulsation pour les yeux
            if pupil_left is not None:
                # Vérifier si animation existe déjà
                has_animate = any(child.tag.endswith("animate") for child in pupil_left)
                if not has_animate:
                    animate = ET.SubElement(pupil_left, "animate")
                    animate.set("attributeName", "opacity")
                    animate.set(
                        "values",
                        f"{0.7 * emotion_variant.glow_intensity};"
                        f"{1.0 * emotion_variant.glow_intensity};"
                        f"{0.7 * emotion_variant.glow_intensity}",
                    )
                    animate.set("dur", f"{2 / emotion_variant.animation_speed}s")
                    animate.set("repeatCount", "indefinite")

            if pupil_right is not None:
                has_animate = any(
                    child.tag.endswith("animate") for child in pupil_right
                )
                if not has_animate:
                    animate = ET.SubElement(pupil_right, "animate")
                    animate.set("attributeName", "opacity")
                    animate.set(
                        "values",
                        f"{0.7 * emotion_variant.glow_intensity};"
                        f"{1.0 * emotion_variant.glow_intensity};"
                        f"{0.7 * emotion_variant.glow_intensity}",
                    )
                    animate.set("dur", f"{2 / emotion_variant.animation_speed}s")
                    animate.set("repeatCount", "indefinite")

            # 3. Animation de rotation de la tête (curiosité)
            head_group = root.find(".//*[@id='head-group']")
            if head_group is not None:
                # Rotation de base
                base_rotation = -15

                # Ajouter animation de rotation
                animate_transform = ET.SubElement(head_group, "animateTransform")
                animate_transform.set("attributeName", "transform")
                animate_transform.set("type", "rotate")
                animate_transform.set(
                    "values",
                    f"{base_rotation} 250 250;{base_rotation + 10} 250 250;{base_rotation - 10} 250 250;{base_rotation} 250 250",
                )
                animate_transform.set("dur", f"{3 / emotion_variant.animation_speed}s")
                animate_transform.set("repeatCount", "indefinite")

            # 4. Modifier les antennes (signal actif)
            antenna_left_signal = root.find(".//*[@id='antenna-left-signal']")
            antenna_right_signal = root.find(".//*[@id='antenna-right-signal']")

            if antenna_left_signal is not None:
                antenna_left_signal.set("fill", emotion_variant.colors.accent)
            if antenna_right_signal is not None:
                antenna_right_signal.set("fill", emotion_variant.colors.accent)

            # 5. Ajouter animation aux antennes (pulsation)
            if antenna_left_signal is not None:
                animate_antenna = ET.SubElement(antenna_left_signal, "animate")
                animate_antenna.set("attributeName", "r")
                animate_antenna.set("values", "4;6;4")
                animate_antenna.set("dur", f"{1.5 / emotion_variant.animation_speed}s")
                animate_antenna.set("repeatCount", "indefinite")

            if antenna_right_signal is not None:
                animate_antenna = ET.SubElement(antenna_right_signal, "animate")
                animate_antenna.set("attributeName", "r")
                animate_antenna.set("values", "4;6;4")
                animate_antenna.set("dur", f"{1.5 / emotion_variant.animation_speed}s")
                animate_antenna.set("begin", "0.3s")  # Décalage pour effet alterné
                animate_antenna.set("repeatCount", "indefinite")

            return ET.tostring(root, encoding="unicode")

        except Exception as e:
            self.logger.error(f"Erreur modification SVG Master : {e}")
            import traceback

            self.logger.error(traceback.format_exc())
            return svg_content

    def _modify_logo_colors(
        self, svg_content: str, emotion_variant: BBIAVariant
    ) -> str:
        """
        Modifie le fond carré avec la couleur BBIA officielle
        Remplaçe TOUTES les occurrences de #008181 (fond turquoise original)

        Args:
            svg_content: Contenu SVG original
            emotion_variant: Variante émotionnelle BBIA

        Returns:
            Contenu SVG avec fond modifié
        """
        try:
            # Utiliser la couleur accent de la variante pour le fond
            bg_color = emotion_variant.colors.accent

            self.logger.debug(
                f"Modification fond: #008181 → {bg_color} "
                f"(variante: {emotion_variant.variant_type.value})"
            )

            # Remplacer TOUTES les occurrences de #008181
            # (dans style, fill, stop-color, etc.)
            # Utiliser un remplacement global et insensible à la casse
            modified_svg = re.sub(
                r"#008181", bg_color, svg_content, flags=re.IGNORECASE
            )

            # Vérifier que le remplacement a fonctionné
            if "#008181" in modified_svg:
                self.logger.warning(
                    "Certaines occurrences de #008181 n'ont pas été remplacées"
                )
            else:
                self.logger.debug(
                    f"✅ Toutes les occurrences de #008181 remplacées par {bg_color}"
                )

            return modified_svg
        except Exception as e:
            self.logger.error(f"Erreur modification couleurs SVG : {e}")
            import traceback

            self.logger.error(traceback.format_exc())
            return svg_content

    def _get_master_svg_path(self, master_type: str = "clean") -> Path:
        """
        Retourne le chemin vers un SVG Master

        Args:
            master_type: Type de master ('clean' ou 'wireframe')

        Returns:
            Chemin vers le fichier SVG Master
        """
        if master_type not in self.MASTER_SVG_SOURCES:
            raise ValueError(
                f"Type de master '{master_type}' non reconnu. "
                f"Types disponibles: {list(self.MASTER_SVG_SOURCES.keys())}"
            )

        source_filename = self.MASTER_SVG_SOURCES[master_type]
        source_path = self.bbia_assets_path / source_filename

        if not source_path.exists():
            raise FileNotFoundError(
                f"SVG Master introuvable : {source_path}\n"
                f"Vérifiez que les assets sont dans : {self.bbia_assets_path}"
            )

        return source_path

    def generate_svg_logo(
        self,
        variant_name: str,
        size: int = 200,
        emotion_variant: Optional[str] = None,
        use_master: bool = True,  # Nouveau paramètre pour utiliser les SVG Master
        master_type: str = "clean",  # 'clean' ou 'wireframe'
    ) -> Path:
        """
        Génère un logo SVG BBIA avec variante émotionnelle optionnelle

        Args:
            variant_name: Type de logo (mark_only, vertical, horizontal)
            size: Taille du logo
            emotion_variant: Variante émotionnelle (serenity, power, etc.) ou None

        Returns:
            Chemin du fichier généré
        """
        if emotion_variant:
            self.logger.info(
                f"🤖 Génération logo BBIA '{variant_name}' "
                f"variante '{emotion_variant}' en taille {size}x{size}"
            )
        else:
            self.logger.info(
                f"🤖 Génération logo BBIA '{variant_name}' en taille {size}x{size}"
            )

        # Utiliser les SVG Master si demandé
        if use_master:
            try:
                source_path = self._get_master_svg_path(master_type)
                svg_content = self._load_svg_content(source_path)

                # Transformer la taille
                transformed_svg = self._transform_svg_size(svg_content, size)

                # Modifier via IDs sémantiques si variante émotionnelle
                if emotion_variant:
                    try:
                        bbia_variant = BBIA_VARIANTS.get_variant(emotion_variant)
                        transformed_svg = self._modify_master_svg(
                            transformed_svg, bbia_variant
                        )
                    except ValueError as e:
                        self.logger.warning(f"Variante émotionnelle invalide : {e}")
                        self.logger.warning("Génération sans modification")
            except FileNotFoundError:
                # Fallback sur les anciens SVG sources
                self.logger.warning(
                    f"SVG Master '{master_type}' non trouvé, "
                    f"utilisation de l'ancien système"
                )
                use_master = False

        # Ancien système (fallback)
        if not use_master:
            source_path = self._get_source_svg_path(variant_name)
            svg_content = self._load_svg_content(source_path)

            # Transformer la taille
            transformed_svg = self._transform_svg_size(svg_content, size)

            # Modifier couleurs si variante émotionnelle spécifiée
            if emotion_variant:
                try:
                    bbia_variant = BBIA_VARIANTS.get_variant(emotion_variant)
                    transformed_svg = self._modify_logo_colors(
                        transformed_svg, bbia_variant
                    )
                except ValueError as e:
                    self.logger.warning(f"Variante émotionnelle invalide : {e}")
                    self.logger.warning("Génération sans modification")

        # Créer le chemin de sortie
        if use_master:
            master_suffix = f"-{master_type}"
        else:
            master_suffix = ""

        if emotion_variant:
            output_path = (
                self.output_dir
                / f"bbia-{variant_name}{master_suffix}-{emotion_variant}-{size}.svg"
            )
        else:
            output_path = (
                self.output_dir / f"bbia-{variant_name}{master_suffix}-{size}.svg"
            )
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Sauvegarder
        output_path.write_text(transformed_svg, encoding="utf-8")

        self.logger.info(f"✅ Logo BBIA généré : {output_path}")
        return output_path

    def generate_png_logo(
        self,
        variant_name: str,
        size: int = 512,
        emotion_variant: Optional[str] = None,
    ) -> Optional[Path]:
        """
        Génère un logo PNG BBIA depuis le SVG

        Args:
            variant_name: Type de logo (mark_only, vertical, horizontal)
            size: Taille du logo
            emotion_variant: Variante émotionnelle (serenity, power, etc.) ou None

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
        svg_path = self.generate_svg_logo(variant_name, size, emotion_variant)

        # Créer le chemin PNG
        if emotion_variant:
            png_path = (
                self.output_dir / f"bbia-{variant_name}-{emotion_variant}-{size}.png"
            )
        else:
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

    def generate_all_emotion_variants(
        self,
        variant_name: str,
        size: int = 512,
        formats: Optional[List[str]] = None,
    ) -> List[Path]:
        """
        Génère toutes les variantes émotionnelles pour un format de logo

        Args:
            variant_name: Type de logo (mark_only, vertical, horizontal)
            size: Taille du logo
            formats: Liste des formats ('svg', 'png') (défaut: ['svg'])

        Returns:
            Liste des fichiers générés
        """
        if formats is None:
            formats = ["svg"]

        generated_files = []
        emotion_variants = BBIA_VARIANTS.list_variant_names()

        for emotion in emotion_variants:
            try:
                if "svg" in formats:
                    output_path = self.generate_svg_logo(
                        variant_name, size, emotion_variant=emotion
                    )
                    generated_files.append(output_path)

                if "png" in formats:
                    png_path = self.generate_png_logo(
                        variant_name, size, emotion_variant=emotion
                    )
                    if png_path:
                        generated_files.append(png_path)
            except Exception as e:
                self.logger.error(
                    f"Erreur génération variante émotionnelle '{emotion}' "
                    f"pour '{variant_name}': {e}"
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

        emotion_variants = BBIA_VARIANTS.list_variant_names()

        return {
            "assets_available": assets_available,
            "assets_path": str(self.bbia_assets_path),
            "available_variants": available_variants,
            "emotion_variants": emotion_variants,
            "palette": self.palette.to_dict(),
            "status": "ready" if assets_available else "assets_missing",
            "cairosvg_available": cairosvg is not None,
        }
