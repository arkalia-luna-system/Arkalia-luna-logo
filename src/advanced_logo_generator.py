"""
🌙 Advanced Logo Generator Module
Générateur de logos avancés avec effets complexes
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from .logo_generator import ArkaliaLunaLogo
    from .svg_builder_advanced import AdvancedSVGBuilder
    from .variants import LogoVariants
except ImportError:
    # Fallback pour exécution directe
    from logo_generator import ArkaliaLunaLogo
    from svg_builder_advanced import AdvancedSVGBuilder


class AdvancedArkaliaLunaLogo(ArkaliaLunaLogo):
    """Générateur principal des logos Arkalia-LUNA avec rendu exceptionnel"""

    def __init__(self, output_dir: Optional[Path] = None):
        # Appel du constructeur parent avec répertoire spécialisé
        super().__init__(output_dir or Path("exports-advanced"))

        # Remplace le SVG builder par défaut par l'Advanced
        self.svg_builder = AdvancedSVGBuilder(self.variants_manager)
        self.logger.info("🎨 Advanced Generator initialisé avec succès")

        # Configuration avancée spécialisée
        self.advanced_effects = True
        self.complexity_level = 0.9
        self.quality_boost = True

    def generate_advanced_svg_logo(self, variant_name: str, size: int = 200) -> Path:
        """Génère un logo SVG ultra-avancé pour une variante donnée"""
        try:
            self.logger.info(
                f"🎨 Génération du logo SVG avancé '{variant_name}' "
                f"en taille {size}x{size}"
            )

            # Validation de la variante
            if not self.variants_manager.validate_variant(variant_name):
                raise ValueError(f"Variante '{variant_name}' non reconnue")

            # Construction du chemin de sortie
            output_path = (
                self.output_dir / f"arkalia-luna-advanced-{variant_name}-{size}.svg"
            )

            # Génération et sauvegarde avec le builder avancé
            self.svg_builder.save_advanced_logo(variant_name, size, output_path)

            self.logger.info(f"✨ Logo SVG avancé généré avec succès : {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(
                f"❌ Erreur lors de la génération du logo avancé '{variant_name}': {e}"
            )
            raise

    def generate_all_advanced_variants(self, size: int = 200) -> List[Path]:
        """Génère toutes les variantes du logo en version avancée"""
        try:
            self.logger.info(
                f"🚀 Génération de toutes les variantes avancées "
                f"en taille {size}x{size}"
            )

            generated_files = []
            variants = self.variants_manager.list_variants()

            for variant in variants:
                try:
                    output_path = self.generate_advanced_svg_logo(variant, size)
                    generated_files.append(output_path)
                    self.logger.info(f"✅ {variant} : {output_path.name}")
                except Exception as e:
                    self.logger.error(f"❌ {variant} : {e}")
                    continue

            self.logger.info(
                f"🎉 Génération avancée terminée : "
                f"{len(generated_files)}/{len(variants)} logos créés"
            )
            return generated_files

        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la génération avancée globale: {e}")
            raise

    def create_advanced_favicon(
        self, variant_name: str, size: int = 32, advanced_effects: bool = True
    ) -> Path:
        """Crée un favicon avancé avec effets complexes"""
        try:
            self.logger.info(
                f"🎨 Création favicon avancé '{variant_name}' "
                f"effets avancés: {advanced_effects}"
            )

            # Utilise la méthode parent mais avec le builder avancé
            return super().create_favicon(variant_name, size)

        except Exception as e:
            self.logger.error(
                f"❌ Erreur lors de la création du favicon avancé '{variant_name}': {e}"
            )
            raise

    def set_advanced_effects(self, enabled: bool = True) -> None:
        """Active/désactive les effets avancés"""
        self.advanced_effects = enabled
        self.logger.info(f"🎨 Effets avancés: {'activés' if enabled else 'désactivés'}")

    def set_complexity_level(self, level: float) -> None:
        """Configure le niveau de complexité (0.1 à 1.0)"""
        if 0.1 <= level <= 1.0:
            self.complexity_level = level
            self.logger.info(f"🎯 Complexité avancée: {level:.2f}")
        else:
            raise ValueError("Niveau de complexité doit être entre 0.1 et 1.0")

    def toggle_quality_boost(self, enabled: bool = True) -> None:
        """Active/désactive le boost de qualité"""
        self.quality_boost = enabled
        self.logger.info(f"🎨 Boost qualité: {'activé' if enabled else 'désactivé'}")

    def get_advanced_stats(self) -> Dict[str, Any]:
        """Retourne les statistiques avancées"""
        return {
            "advanced_effects": self.advanced_effects,
            "complexity_level": self.complexity_level,
            "quality_boost": self.quality_boost,
            "generator_type": "Advanced",
            "optimizations": [
                "Gradients complexes",
                "Filtres avancés",
                "Effets organiques",
            ],
        }
