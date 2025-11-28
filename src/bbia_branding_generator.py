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

    def _modify_logo_colors(
        self, svg_content: str, emotion_variant: BBIAVariant
    ) -> str:
        """
        Modifie directement les couleurs du logo BBIA selon la variante émotionnelle

        Args:
            svg_content: Contenu SVG original
            emotion_variant: Variante émotionnelle BBIA

        Returns:
            Contenu SVG avec couleurs modifiées
        """
        try:
            # STRATÉGIE : Modifier directement dans le contenu texte avec regex
            # Plus fiable que de modifier le XML avec namespaces
            eye_color = emotion_variant.colors.glow
            # Utiliser accent pour le fond (plus visible que primary qui est #008181)
            bg_color = emotion_variant.colors.accent

            # 1. Remplacer toutes les occurrences de #008181 par la couleur accent de la variante
            modified_svg = re.sub(r"#008181", bg_color, svg_content)

            # 2. NE PAS modifier les yeux transparents (#cccccc) - ils restent gris transparents
            # Les yeux sont identifiés par leur label "cou" et leur couleur #cccccc
            # On les préserve pour garder l'identité visuelle du robot

            # 3. Maintenant parser pour ajouter les filtres et animations
            root = ET.fromstring(modified_svg)

            # Trouver ou créer defs
            defs = root.find(".//{http://www.w3.org/2000/svg}defs")
            if defs is None:
                defs = ET.Element("defs")
                root.insert(0, defs)

            # Ajouter filtre de lueur pour les yeux
            filter_id = f"eye-glow-{emotion_variant.variant_type.value}"
            filter_elem = ET.Element("filter", id=filter_id)
            filter_elem.set("x", "-50%")
            filter_elem.set("y", "-50%")
            filter_elem.set("width", "200%")
            filter_elem.set("height", "200%")

            fe_gaussian = ET.SubElement(filter_elem, "feGaussianBlur")
            fe_gaussian.set("stdDeviation", "3")
            fe_gaussian.set("result", "coloredBlur")

            fe_flood = ET.SubElement(filter_elem, "feFlood")
            fe_flood.set("flood-color", eye_color)
            fe_flood.set("flood-opacity", str(emotion_variant.glow_intensity))
            fe_flood.set("result", "flood")

            fe_composite = ET.SubElement(filter_elem, "feComposite")
            fe_composite.set("in", "flood")
            fe_composite.set("in2", "coloredBlur")
            fe_composite.set("operator", "in")

            defs.append(filter_elem)

            # 4. Ajouter effets uniques : ondes de parole (comme ChatGPT)
            # Créer des ondes sonores animées AUTOUR du robot (en dehors du fond carré)
            viewbox = root.get("viewBox", "0 0 1024 1024")
            center = 512  # Taille par défaut
            if viewbox:
                try:
                    parts = viewbox.split()
                    if len(parts) == 4:
                        center = int((float(parts[2]) + float(parts[3])) / 4)
                except (ValueError, IndexError):
                    pass

            # Groupe pour les ondes de parole (AU-DESSUS de tout)
            speech_waves_group = ET.Element("g")
            speech_waves_group.set(
                "id", f"speech-waves-{emotion_variant.variant_type.value}"
            )
            # Style pour s'assurer que les ondes sont visibles
            speech_waves_group.set("style", "pointer-events: none;")

            # Créer 8-10 ondes concentriques animées (effet "parole")
            # Les ondes partent de l'extérieur du fond carré et sont TRÈS visibles
            num_waves = 10
            # Le fond carré fait environ 456x456, donc rayon ~228, on commence après
            base_radius = center * 0.48  # Commencer juste après le fond carré
            for i in range(num_waves):
                wave = ET.Element("circle")
                wave.set("cx", str(center))
                wave.set("cy", str(center))
                wave.set("r", str(base_radius + i * 20))
                wave.set("fill", "none")
                wave.set("stroke", emotion_variant.colors.accent)
                wave.set("stroke-width", "4")  # Plus épais pour être visible
                wave.set("opacity", str(0.6 - i * 0.05))  # Plus opaque

                # Animation de pulsation (onde qui s'étend vers l'extérieur)
                animate_radius = ET.SubElement(wave, "animate")
                animate_radius.set("attributeName", "r")
                animate_radius.set(
                    "values",
                    f"{base_radius + i * 25};{base_radius + i * 25 + 30};{base_radius + i * 25}",
                )
                animate_radius.set("dur", f"{2.0 / emotion_variant.animation_speed}s")
                animate_radius.set("begin", f"{i * 0.15}s")
                animate_radius.set("repeatCount", "indefinite")

                # Animation d'opacité (fade in/out)
                animate_opacity = ET.SubElement(wave, "animate")
                animate_opacity.set("attributeName", "opacity")
                animate_opacity.set(
                    "values",
                    f"{0.1 + i * 0.02};{0.5 - i * 0.03};{0.1 + i * 0.02}",
                )
                animate_opacity.set("dur", f"{2.0 / emotion_variant.animation_speed}s")
                animate_opacity.set("begin", f"{i * 0.15}s")
                animate_opacity.set("repeatCount", "indefinite")

                speech_waves_group.append(wave)

            # Insérer les ondes de parole À LA FIN (au-dessus de tout le contenu)
            # pour qu'elles soient visibles même avec le fond opaque
            root.append(speech_waves_group)

            return ET.tostring(root, encoding="unicode")
        except Exception as e:
            self.logger.error(f"Erreur modification couleurs SVG : {e}")
            return svg_content

    def generate_svg_logo(
        self,
        variant_name: str,
        size: int = 200,
        emotion_variant: Optional[str] = None,
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

        # Charger le SVG source
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
        if emotion_variant:
            output_path = (
                self.output_dir / f"bbia-{variant_name}-{emotion_variant}-{size}.svg"
            )
        else:
            output_path = self.output_dir / f"bbia-{variant_name}-{size}.svg"
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
