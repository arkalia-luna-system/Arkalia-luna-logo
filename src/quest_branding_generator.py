"""
🎮 Quest Branding Generator Module
Générateur de logos Arkalia Quest
Intégration avec les générateurs existants et variantes émotionnelles
"""

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

from .logo_generator import ArkaliaLunaLogo
from .quest_palette import QUEST_PALETTE  # type: ignore[import-untyped]
from .variants import LogoVariants  # type: ignore[import-untyped]


class QuestBrandingGenerator(ArkaliaLunaLogo):
    """
    Générateur de logos Arkalia Quest

    Fonctionnalités :
    - Génération automatique des déclinaisons (mark_only, vertical, horizontal)
    - Intégration avec les générateurs existants (Ultimate, Dashboard, etc.)
    - Support des variantes émotionnelles (10 variantes)
    - Export multi-formats (SVG, PNG)
    - Support des tailles multiples (200, 512, 1024)
    """

    # Mapping des variantes vers les formats
    VARIANT_TO_FORMAT: dict[str, str] = {
        "mark_only": "mark_only",
        "vertical": "vertical",
        "horizontal": "horizontal",
    }

    # Styles recommandés pour Quest
    RECOMMENDED_STYLES: list[str] = [
        "ultimate",  # Logo principal
        "dashboard",  # Interface de jeu
        "ai_moon",  # Représentation LUNA
    ]

    def __init__(self, output_dir: Optional[Path] = None) -> None:
        # Appel du constructeur parent
        super().__init__(output_dir or Path("exports") / "quest")

        # Palette Quest
        self.palette = QUEST_PALETTE

        # Variants manager pour les variantes émotionnelles
        self.variants_manager = LogoVariants()

        # Configuration du logging
        self.logger.info("🎮 Quest Branding Generator initialisé")

    def _add_quest_text(
        self, svg_content: str, format_type: str, size: int, variant: str
    ) -> str:
        """
        Ajoute le texte "Arkalia Quest" au logo SVG avec style professionnel

        Args:
            svg_content: Contenu SVG original
            format_type: Type de format (mark_only, vertical, horizontal)
            size: Taille du logo
            variant: Variante émotionnelle

        Returns:
            Contenu SVG avec texte ajouté
        """
        try:
            root = ET.fromstring(svg_content)

            # Trouver ou créer l'élément <defs> pour les filtres et gradients
            defs = root.find(".//{http://www.w3.org/2000/svg}defs")
            if defs is None:
                defs = ET.Element("defs")
                # Insérer defs au début
                if len(root) > 0:
                    root.insert(0, defs)
                else:
                    root.append(defs)

            # Récupérer les couleurs de la variante
            try:
                variant_obj = self.variants_manager.get_variant(variant)
                text_color = variant_obj.colors.primary
                text_glow = variant_obj.colors.glow
                text_accent = variant_obj.colors.accent
            except Exception:
                # Fallback sur la palette Quest
                text_color = self.palette.PRIMARY
                text_glow = self.palette.SECONDARY
                text_accent = self.palette.INFO

            # Créer un filtre de lueur pour le texte
            filter_id = f"quest-text-glow-{variant}"
            text_filter = ET.Element("filter")
            text_filter.set("id", filter_id)
            text_filter.set("x", "-50%")
            text_filter.set("y", "-50%")
            text_filter.set("width", "200%")
            text_filter.set("height", "200%")

            # feGaussianBlur pour l'effet de lueur
            fe_gaussian = ET.SubElement(text_filter, "feGaussianBlur")
            fe_gaussian.set("stdDeviation", "2")
            fe_gaussian.set("result", "coloredBlur")

            # feFlood pour la couleur de lueur
            fe_flood = ET.SubElement(text_filter, "feFlood")
            fe_flood.set("flood-color", text_glow)
            fe_flood.set("flood-opacity", "0.6")
            fe_flood.set("result", "flood")

            # feComposite pour combiner
            fe_composite = ET.SubElement(text_filter, "feComposite")
            fe_composite.set("in", "flood")
            fe_composite.set("in2", "coloredBlur")
            fe_composite.set("operator", "in")

            defs.append(text_filter)

            # Créer un gradient pour le texte
            gradient_id = f"quest-text-gradient-{variant}"
            text_gradient = ET.Element("linearGradient")
            text_gradient.set("id", gradient_id)
            text_gradient.set("x1", "0%")
            text_gradient.set("y1", "0%")
            text_gradient.set("x2", "0%")
            text_gradient.set("y2", "100%")

            stop1 = ET.SubElement(text_gradient, "stop")
            stop1.set("offset", "0%")
            stop1.set("stop-color", text_color)
            stop1.set("stop-opacity", "1.0")

            stop2 = ET.SubElement(text_gradient, "stop")
            stop2.set("offset", "100%")
            stop2.set("stop-color", text_accent)
            stop2.set("stop-opacity", "0.9")

            defs.append(text_gradient)

            # Créer un groupe pour le texte avec effets
            text_group = ET.Element("g")
            text_group.set("id", "quest-text")
            text_group.set("filter", f"url(#{filter_id})")

            if format_type == "mark_only":
                # Pour mark_only, pas de texte (juste le logo)
                return svg_content

            elif format_type == "vertical":
                # Texte en dessous du logo avec meilleur espacement
                logo_bottom = size * 0.75  # Position du bas du logo
                text_start_y = logo_bottom + size * 0.08  # Espacement après le logo
                text_size = size * 0.11

                # Texte "Arkalia" avec ombre
                # Ombre portée
                shadow_arkalia = ET.Element("text")
                shadow_arkalia.set("x", str(size // 2))
                shadow_arkalia.set("y", str(text_start_y + 2))
                shadow_arkalia.set("font-family", "'Segoe UI', 'Helvetica Neue', Arial, sans-serif")
                shadow_arkalia.set("font-size", str(text_size))
                shadow_arkalia.set("font-weight", "700")
                shadow_arkalia.set("fill", "rgba(0,0,0,0.3)")
                shadow_arkalia.set("text-anchor", "middle")
                shadow_arkalia.set("dominant-baseline", "alphabetic")
                shadow_arkalia.text = "Arkalia"

                # Texte principal "Arkalia"
                text_arkalia = ET.Element("text")
                text_arkalia.set("x", str(size // 2))
                text_arkalia.set("y", str(text_start_y))
                text_arkalia.set("font-family", "'Segoe UI', 'Helvetica Neue', Arial, sans-serif")
                text_arkalia.set("font-size", str(text_size))
                text_arkalia.set("font-weight", "700")
                text_arkalia.set("fill", f"url(#{gradient_id})")
                text_arkalia.set("text-anchor", "middle")
                text_arkalia.set("dominant-baseline", "alphabetic")
                text_arkalia.text = "Arkalia"

                # Ombre portée pour "Quest"
                shadow_quest = ET.Element("text")
                shadow_quest.set("x", str(size // 2))
                shadow_quest.set("y", str(text_start_y + text_size * 1.15 + 2))
                shadow_quest.set("font-family", "'Segoe UI', 'Helvetica Neue', Arial, sans-serif")
                shadow_quest.set("font-size", str(text_size * 0.85))
                shadow_quest.set("font-weight", "600")
                shadow_quest.set("fill", "rgba(0,0,0,0.3)")
                shadow_quest.set("text-anchor", "middle")
                shadow_quest.set("dominant-baseline", "alphabetic")
                shadow_quest.text = "Quest"

                # Texte principal "Quest"
                text_quest = ET.Element("text")
                text_quest.set("x", str(size // 2))
                text_quest.set("y", str(text_start_y + text_size * 1.15))
                text_quest.set("font-family", "'Segoe UI', 'Helvetica Neue', Arial, sans-serif")
                text_quest.set("font-size", str(text_size * 0.85))
                text_quest.set("font-weight", "600")
                text_quest.set("fill", f"url(#{gradient_id})")
                text_quest.set("text-anchor", "middle")
                text_quest.set("dominant-baseline", "alphabetic")
                text_quest.text = "Quest"

                text_group.append(shadow_arkalia)
                text_group.append(text_arkalia)
                text_group.append(shadow_quest)
                text_group.append(text_quest)

            elif format_type == "horizontal":
                # Texte à droite du logo avec meilleur positionnement
                logo_right = size * 0.55  # Position du logo
                text_x = logo_right + size * 0.05  # Espacement après le logo
                text_y = size * 0.5
                text_size = size * 0.13

                # Ombre portée
                shadow = ET.Element("text")
                shadow.set("x", str(text_x + 2))
                shadow.set("y", str(text_y + 2))
                shadow.set("font-family", "'Segoe UI', 'Helvetica Neue', Arial, sans-serif")
                shadow.set("font-size", str(text_size))
                shadow.set("font-weight", "700")
                shadow.set("fill", "rgba(0,0,0,0.3)")
                shadow.set("text-anchor", "start")
                shadow.set("dominant-baseline", "middle")
                shadow.text = "Arkalia Quest"

                # Texte principal
                text = ET.Element("text")
                text.set("x", str(text_x))
                text.set("y", str(text_y))
                text.set("font-family", "'Segoe UI', 'Helvetica Neue', Arial, sans-serif")
                text.set("font-size", str(text_size))
                text.set("font-weight", "700")
                text.set("fill", f"url(#{gradient_id})")
                text.set("text-anchor", "start")
                text.set("dominant-baseline", "middle")
                text.text = "Arkalia Quest"

                text_group.append(shadow)
                text_group.append(text)

            # Ajouter le groupe texte au SVG (après le logo)
            root.append(text_group)

            return ET.tostring(root, encoding="unicode")
        except Exception as e:
            self.logger.error(f"Erreur ajout texte Quest : {e}")
            return svg_content

    def generate_svg_logo(
        self,
        variant_name: str,
        size: int = 200,
        emotion_variant: Optional[str] = None,
        style: Optional[str] = None,
    ) -> Path:
        """
        Génère un logo SVG Quest

        Args:
            variant_name: Type de logo (mark_only, vertical, horizontal)
            size: Taille du logo
            emotion_variant: Variante émotionnelle (serenity, power, etc.) ou None
            style: Style de générateur (ultimate, dashboard, etc.) ou None

        Returns:
            Chemin du fichier généré
        """
        # Utiliser la variante par défaut si non spécifiée
        if emotion_variant is None:
            emotion_variant = "serenity"

        # Utiliser le style par défaut si non spécifié
        if style is None:
            style = "ultimate"

        self.logger.info(
            f"🎮 Génération logo Quest '{variant_name}' "
            f"variante '{emotion_variant}' style '{style}' en taille {size}x{size}"
        )

        # Générer le logo de base avec le générateur approprié
        # Importation locale pour éviter import circulaire
        try:
            from .generator_factory import LogoGeneratorFactory

            base_generator = LogoGeneratorFactory.create_generator(
                style, self.output_dir
            )
            base_logo_path = base_generator.generate_svg_logo(emotion_variant, size)
        except Exception as e:
            self.logger.error(f"Erreur génération logo de base : {e}")
            # Fallback sur le générateur par défaut
            from .generator_factory import LogoGeneratorFactory

            base_generator = LogoGeneratorFactory.create_generator(
                "default", self.output_dir
            )
            base_logo_path = base_generator.generate_svg_logo(emotion_variant, size)

        # Charger le contenu SVG
        svg_content = base_logo_path.read_text(encoding="utf-8")

        # Ajouter le texte Quest si nécessaire
        if variant_name != "mark_only":
            svg_content = self._add_quest_text(
                svg_content, variant_name, size, emotion_variant
            )

        # Créer le chemin de sortie
        output_path = (
            self.output_dir
            / f"quest-{variant_name}-{emotion_variant}-{style}-{size}.svg"
        )
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Sauvegarder
        output_path.write_text(svg_content, encoding="utf-8")

        self.logger.info(f"✅ Logo Quest généré : {output_path}")
        return output_path

    def generate_png_logo(
        self,
        variant_name: str,
        size: int = 512,
        emotion_variant: Optional[str] = None,
        style: Optional[str] = None,
    ) -> Optional[Path]:
        """
        Génère un logo PNG Quest depuis le SVG

        Args:
            variant_name: Type de logo (mark_only, vertical, horizontal)
            size: Taille du logo
            emotion_variant: Variante émotionnelle (serenity, power, etc.) ou None
            style: Style de générateur (ultimate, dashboard, etc.) ou None

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
            f"🎮 Génération logo PNG Quest '{variant_name}' en taille {size}x{size}"
        )

        # Générer d'abord le SVG
        svg_path = self.generate_svg_logo(variant_name, size, emotion_variant, style)

        # Créer le chemin PNG
        if emotion_variant and style:
            png_path = (
                self.output_dir
                / f"quest-{variant_name}-{emotion_variant}-{style}-{size}.png"
            )
        else:
            png_path = self.output_dir / f"quest-{variant_name}-{size}.png"
        png_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            # Convertir SVG en PNG
            cairosvg.svg2png(
                url=str(svg_path),
                write_to=str(png_path),
                output_width=size,
                output_height=size,
            )
            self.logger.info(f"✅ Logo PNG Quest généré : {png_path}")
            return png_path
        except Exception as e:
            self.logger.error(f"Erreur conversion SVG→PNG : {e}")
            return None

    def generate_all_declinations(
        self,
        sizes: Optional[List[int]] = None,
        formats: Optional[List[str]] = None,
        emotion_variant: Optional[str] = None,
        style: Optional[str] = None,
    ) -> List[Path]:
        """
        Génère toutes les déclinaisons Quest

        Args:
            sizes: Liste des tailles à générer (défaut: [200, 512, 1024])
            formats: Liste des formats ('svg', 'png') (défaut: ['svg'])
            emotion_variant: Variante émotionnelle (défaut: 'serenity')
            style: Style de générateur (défaut: 'ultimate')

        Returns:
            Liste des fichiers générés
        """
        if sizes is None:
            sizes = [200, 512, 1024]
        if formats is None:
            formats = ["svg"]
        if emotion_variant is None:
            emotion_variant = "serenity"
        if style is None:
            style = "ultimate"

        declinations = ["mark_only", "vertical", "horizontal"]
        generated_files = []

        for declination in declinations:
            for size in sizes:
                try:
                    # Générer SVG
                    if "svg" in formats:
                        output_path = self.generate_svg_logo(
                            declination, size, emotion_variant, style
                        )
                        generated_files.append(output_path)

                    # Générer PNG si demandé
                    if "png" in formats:
                        png_path = self.generate_png_logo(
                            declination, size, emotion_variant, style
                        )
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
        style: Optional[str] = None,
    ) -> List[Path]:
        """
        Génère toutes les variantes émotionnelles pour un format de logo

        Args:
            variant_name: Type de logo (mark_only, vertical, horizontal)
            size: Taille du logo
            formats: Liste des formats ('svg', 'png') (défaut: ['svg'])
            style: Style de générateur (défaut: 'ultimate')

        Returns:
            Liste des fichiers générés
        """
        if formats is None:
            formats = ["svg"]
        if style is None:
            style = "ultimate"

        generated_files = []
        emotion_variants = self.variants_manager.list_variants()

        for emotion in emotion_variants:
            try:
                if "svg" in formats:
                    output_path = self.generate_svg_logo(
                        variant_name, size, emotion_variant=emotion, style=style
                    )
                    generated_files.append(output_path)

                if "png" in formats:
                    png_path = self.generate_png_logo(
                        variant_name, size, emotion_variant=emotion, style=style
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

    def get_quest_stats(self) -> dict:
        """Retourne les statistiques Quest"""
        available_variants = self.variants_manager.list_variants()
        available_styles = self.RECOMMENDED_STYLES

        return {
            "available_variants": available_variants,
            "available_formats": list(self.VARIANT_TO_FORMAT.keys()),
            "recommended_styles": available_styles,
            "palette": self.palette.to_dict(),
            "status": "ready",
            "cairosvg_available": cairosvg is not None,
        }
