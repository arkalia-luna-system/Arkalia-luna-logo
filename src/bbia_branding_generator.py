"""
🤖 BBIA Branding Generator Module
Générateur de logos BBIA pour Reachy Mini
Intégration complète avec assets SVG sources et variantes émotionnelles
"""

import math
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

    def _add_svg_effects(
        self, svg_content: str, emotion_variant: BBIAVariant, size: int
    ) -> str:
        """
        Ajoute les effets SVG (halos, particules) au logo BBIA

        Args:
            svg_content: Contenu SVG original
            emotion_variant: Variante émotionnelle BBIA
            size: Taille du logo

        Returns:
            Contenu SVG avec effets ajoutés
        """
        try:
            root = ET.fromstring(svg_content)
            center = size // 2

            # Trouver ou créer l'élément <defs> pour les filtres
            defs = root.find(".//{http://www.w3.org/2000/svg}defs")
            if defs is None:
                defs = ET.Element("defs")
                # Insérer defs après le premier élément (généralement après xmlns)
                root.insert(0, defs)

            # Ajouter filtre de lueur
            filter_id = f"glow-{emotion_variant.variant_type.value}"
            filter_elem = ET.Element("filter", id=filter_id)
            filter_elem.set("x", "-50%")
            filter_elem.set("y", "-50%")
            filter_elem.set("width", "200%")
            filter_elem.set("height", "200%")

            # feGaussianBlur pour l'effet de lueur
            fe_gaussian = ET.SubElement(filter_elem, "feGaussianBlur")
            fe_gaussian.set("stdDeviation", str(3 * emotion_variant.glow_intensity))
            fe_gaussian.set("result", "coloredBlur")

            # feOffset
            fe_offset = ET.SubElement(filter_elem, "feOffset")
            fe_offset.set("in", "coloredBlur")
            fe_offset.set("dx", "0")
            fe_offset.set("dy", "0")
            fe_offset.set("result", "offsetBlur")

            # feFlood pour la couleur
            fe_flood = ET.SubElement(filter_elem, "feFlood")
            fe_flood.set("flood-color", emotion_variant.colors.glow)
            fe_flood.set("flood-opacity", str(emotion_variant.glow_intensity))
            fe_flood.set("result", "flood")

            # feComposite
            fe_composite = ET.SubElement(filter_elem, "feComposite")
            fe_composite.set("in", "flood")
            fe_composite.set("in2", "offsetBlur")
            fe_composite.set("operator", "in")

            defs.append(filter_elem)

            # Créer un groupe pour les effets (derrière le logo)
            effects_group = ET.Element("g")
            effects_group.set("id", "bbia-effects")

            # Ajouter halo si activé
            if emotion_variant.halo_enabled:
                halo = ET.Element("circle")
                halo.set("cx", str(center))
                halo.set("cy", str(center))
                halo.set("r", str(size // 2 - 10))
                halo.set("fill", "none")
                halo.set("stroke", emotion_variant.colors.glow)
                halo.set("stroke-width", "2")
                halo.set("opacity", str(0.7 * emotion_variant.glow_intensity))
                halo.set("filter", f"url(#{filter_id})")

                # Animation de respiration
                animate = ET.SubElement(halo, "animate")
                animate.set("attributeName", "opacity")
                animate.set(
                    "values",
                    f"{0.7 * emotion_variant.glow_intensity};{0.3 * emotion_variant.glow_intensity};{0.7 * emotion_variant.glow_intensity}",
                )
                animate.set("dur", f"{3 / emotion_variant.animation_speed}s")
                animate.set("repeatCount", "indefinite")

                effects_group.append(halo)

            # Ajouter particules si activé
            if emotion_variant.particles_enabled:
                num_particles = 12
                for i in range(num_particles):
                    angle = (i * 360 / num_particles) * (math.pi / 180)
                    radius = size // 2 - 25
                    x = center + radius * math.cos(angle)
                    y = center + radius * math.sin(angle)

                    particle = ET.Element("circle")
                    particle.set("cx", str(x))
                    particle.set("cy", str(y))
                    particle.set("r", "2.5")
                    particle.set("fill", emotion_variant.colors.glow)
                    particle.set("opacity", "0.7")
                    particle.set("filter", f"url(#{filter_id})")

                    # Animation de scintillement
                    animate_opacity = ET.SubElement(particle, "animate")
                    animate_opacity.set("attributeName", "opacity")
                    animate_opacity.set("values", "0.7;1.0;0.7")
                    animate_opacity.set(
                        "dur", f"{2.5 / emotion_variant.animation_speed}s"
                    )
                    animate_opacity.set("begin", f"{i * 0.2}s")
                    animate_opacity.set("repeatCount", "indefinite")

                    effects_group.append(particle)

            # Insérer les effets au début du SVG (derrière le logo)
            if len(root) > 0:
                root.insert(0, effects_group)
            else:
                root.append(effects_group)

            return ET.tostring(root, encoding="unicode")
        except Exception as e:
            self.logger.error(f"Erreur ajout effets SVG : {e}")
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

        # Ajouter effets si variante émotionnelle spécifiée
        if emotion_variant:
            try:
                bbia_variant = BBIA_VARIANTS.get_variant(emotion_variant)
                transformed_svg = self._add_svg_effects(
                    transformed_svg, bbia_variant, size
                )
            except ValueError as e:
                self.logger.warning(f"Variante émotionnelle invalide : {e}")
                self.logger.warning("Génération sans effets")

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
