"""🌙 Simple Advanced Logo Generator Module
Générateur de logos simple-advanced avec animations et optimisations
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from .logo_generator import ArkaliaLunaLogo
    from .svg_builder_simple_advanced import SimpleAdvancedSVGBuilder
except ImportError:
    # Fallback pour exécution directe
    from logo_generator import ArkaliaLunaLogo
    from svg_builder_simple_advanced import SimpleAdvancedSVGBuilder


class SimpleAdvancedLogoGenerator(ArkaliaLunaLogo):
    """Générateur simple-advanced avec équilibre performance/qualité"""

    def __init__(self, output_dir: Optional[Path] = None) -> None:
        super().__init__(output_dir)
        # Remplace le SVG builder par défaut par le Simple Advanced
        self.svg_builder = SimpleAdvancedSVGBuilder(self.variants_manager)
        self.logger.info("⚡ Simple Advanced Generator initialisé avec succès")

        # Configuration optimisée
        self.animation_enabled = True
        self.complexity_level = 0.7
        self.performance_boost = True

    def generate_simple_advanced_logo(
        self,
        variant_name: str,
        size: int = 200,
        complexity: float = 0.7,
    ) -> Path:
        """Génère un logo simple-advanced avec niveau de complexité configurable"""
        try:
            self.logger.info(
                f"⚡ Génération logo simple-advanced '{variant_name}' "
                f"complexité {complexity:.2f}",
            )

            # Validation de la variante
            if not self.variants_manager.validate_variant(variant_name):
                raise ValueError(f"Variante '{variant_name}' non reconnue")

            # Construction du chemin de sortie avec suffixe simple-advanced
            output_path = (
                self.output_dir
                / f"arkalia-luna-simple-advanced-{variant_name}-{size}.svg"
            )

            # Génération avec le builder Simple Advanced
            self.svg_builder.save_logo(variant_name, size, output_path)

            self.logger.info(f"✅ Logo simple-advanced généré : {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(
                f"❌ Erreur génération simple-advanced '{variant_name}': {e}",
            )
            raise

    def generate_all_simple_advanced_variants(
        self,
        size: int = 200,
        complexity: float = 0.7,
    ) -> List[Path]:
        """Génère toutes les variantes en mode simple-advanced"""
        try:
            self.logger.info(
                f"⚡ Génération de toutes les variantes simple-advanced "
                f"complexité {complexity:.2f}",
            )

            generated_files = []
            variants = self.variants_manager.list_variants()

            for variant in variants:
                try:
                    output_path = self.generate_simple_advanced_logo(
                        variant,
                        size,
                        complexity,
                    )
                    generated_files.append(output_path)
                except Exception as e:
                    self.logger.error(
                        f"❌ Échec variante simple-advanced '{variant}': {e}",
                    )
                    continue

            self.logger.info(
                f"✅ Génération simple-advanced terminée : "
                f"{len(generated_files)}/{len(variants)} logos créés",
            )
            return generated_files

        except Exception as e:
            self.logger.error(f"❌ Erreur génération simple-advanced globale: {e}")
            raise

    def create_simple_advanced_favicon(
        self,
        variant_name: str,
        size: int = 32,
        complexity: float = 0.7,
    ) -> Path:
        """Crée un favicon simple-advanced avec animations"""
        try:
            self.logger.info(
                f"⚡ Création favicon simple-advanced '{variant_name}' "
                f"complexité {complexity:.2f}",
            )

            # Utilise la méthode parent mais avec le builder simple-advanced
            return super().create_favicon(variant_name, size)

        except Exception as e:
            self.logger.error(
                f"❌ Erreur création favicon simple-advanced '{variant_name}': {e}",
            )
            raise

    def toggle_animations(self, enabled: bool = True) -> None:
        """Active/désactive les animations"""
        self.animation_enabled = enabled
        self.logger.info(f"⚡ Animations: {'activées' if enabled else 'désactivées'}")

    def set_complexity_level(self, level: float) -> None:
        """Configure le niveau de complexité (0.1 à 1.0)"""
        if 0.1 <= level <= 1.0:
            self.complexity_level = level
            self.logger.info(f"🎯 Complexité simple-advanced: {level:.2f}")
        else:
            raise ValueError("Niveau de complexité doit être entre 0.1 et 1.0")

    def toggle_performance_boost(self, enabled: bool = True) -> None:
        """Active/désactive le boost de performance"""
        self.performance_boost = enabled
        self.logger.info(
            f"⚡ Boost performance: {'activé' if enabled else 'désactivé'}",
        )

    def get_optimization_stats(self) -> Dict[str, Any]:
        """Retourne les statistiques d'optimisation"""
        return {
            "animation_enabled": self.animation_enabled,
            "complexity_level": self.complexity_level,
            "performance_boost": self.performance_boost,
            "generator_type": "SimpleAdvanced",
            "optimizations": [
                "Gradients simplifiés",
                "Filtres optimisés",
                "Cache mémoire",
            ],
        }
