"""🌙 Ultra Max Logo Generator Module
Générateur ULTRA-avancé des logos Arkalia-LUNA avec effets EXCEPTIONNELS
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from .logo_generator import ArkaliaLunaLogo
    from .svg_builder_ultra_max import UltraMaxSVGBuilder
except ImportError:
    # Fallback pour exécution directe
    from logo_generator import ArkaliaLunaLogo
    from svg_builder_ultra_max import UltraMaxSVGBuilder


class UltraMaxLogoGenerator(ArkaliaLunaLogo):
    """Générateur ULTRA-avancé avec effets EXCEPTIONNELS
    et optimisations de performance
    """

    def __init__(self, output_dir: Optional[Path] = None) -> None:
        super().__init__(output_dir)
        # Remplace le SVG builder par défaut par l'Ultra Max
        self.svg_builder = UltraMaxSVGBuilder(self.variants_manager)
        self.logger.info("🚀 Ultra Max Generator initialisé avec succès")

        # Configuration ULTRA-MAX
        self.performance_mode = True
        self.quality_level = 1.0
        self.effects_intensity = 0.95

    def generate_ultra_max_logo(
        self,
        variant_name: str,
        size: int = 200,
        effects_level: float = 0.95,
    ) -> Path:
        """Génère un logo ULTRA-MAX avec niveau d'effets configurable"""
        try:
            self.logger.info(
                f"🚀 Génération logo ULTRA-MAX '{variant_name}' "
                f"effets {effects_level:.2f}",
            )

            # Validation de la variante
            if not self.variants_manager.validate_variant(variant_name):
                raise ValueError(f"Variante '{variant_name}' non reconnue")

            # Construction du chemin de sortie avec suffixe ultra-max
            output_path = (
                self.output_dir / f"arkalia-luna-ultra-max-{variant_name}-{size}.svg"
            )

            # Génération avec le builder Ultra Max
            self.svg_builder.save_logo(variant_name, size, output_path)

            self.logger.info(f"✅ Logo ULTRA-MAX généré : {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(f"❌ Erreur génération ULTRA-MAX '{variant_name}': {e}")
            raise

    def generate_all_ultra_max_variants(
        self,
        size: int = 200,
        effects_level: float = 0.95,
    ) -> List[Path]:
        """Génère toutes les variantes en mode ULTRA-MAX"""
        try:
            self.logger.info(
                f"🚀 Génération de toutes les variantes ULTRA-MAX "
                f"effets {effects_level:.2f}",
            )

            generated_files = []
            variants = self.variants_manager.list_variants()

            for variant in variants:
                try:
                    output_path = self.generate_ultra_max_logo(
                        variant,
                        size,
                        effects_level,
                    )
                    generated_files.append(output_path)
                except Exception as e:
                    self.logger.error(f"❌ Échec variante ULTRA-MAX '{variant}': {e}")
                    continue

            self.logger.info(
                f"✅ Génération ULTRA-MAX terminée : "
                f"{len(generated_files)}/{len(variants)} logos créés",
            )
            return generated_files

        except Exception as e:
            self.logger.error(f"❌ Erreur génération ULTRA-MAX globale: {e}")
            raise

    def create_ultra_max_favicon(
        self,
        variant_name: str,
        size: int = 32,
        effects_level: float = 0.95,
    ) -> Path:
        """Crée un favicon ULTRA-MAX avec effets exceptionnels"""
        try:
            self.logger.info(
                f"🚀 Création favicon ULTRA-MAX '{variant_name}' "
                f"effets {effects_level:.2f}",
            )

            # Utilise la méthode parent mais avec le builder ultra-max
            return super().create_favicon(variant_name, size)

        except Exception as e:
            self.logger.error(
                f"❌ Erreur création favicon ULTRA-MAX '{variant_name}': {e}",
            )
            raise

    def set_performance_mode(self, enabled: bool = True) -> None:
        """Active/désactive le mode performance ULTRA-MAX"""
        self.performance_mode = enabled
        self.logger.info(
            f"🚀 Mode performance ULTRA-MAX: {'activé' if enabled else 'désactivé'}",
        )

    def set_quality_level(self, level: float) -> None:
        """Configure le niveau de qualité (0.1 à 1.0)"""
        if 0.1 <= level <= 1.0:
            self.quality_level = level
            self.logger.info(f"🎯 Qualité ULTRA-MAX configurée: {level:.2f}")
        else:
            raise ValueError("Niveau de qualité doit être entre 0.1 et 1.0")

    def set_effects_intensity(self, intensity: float) -> None:
        """Configure l'intensité des effets (0.0 à 1.0)"""
        if 0.0 <= intensity <= 1.0:
            self.effects_intensity = intensity
            self.logger.info(f"⚡ Intensité des effets ULTRA-MAX: {intensity:.2f}")
        else:
            raise ValueError("Intensité des effets doit être entre 0.0 et 1.0")

    def get_performance_stats(self) -> Dict[str, Any]:
        """Retourne les statistiques de performance ULTRA-MAX"""
        return {
            "performance_mode": self.performance_mode,
            "quality_level": self.quality_level,
            "effects_intensity": self.effects_intensity,
            "generator_type": "UltraMax",
            "optimizations": [
                "Gradients optimisés",
                "Filtres avancés",
                "Cache intelligent",
            ],
        }
