"""🌙 Realism Max Logo Generator Module
Générateur de logos ultra-réalistes avec effets organiques et IA
"""

from pathlib import Path
from typing import List, Optional

try:
    from .logo_generator import ArkaliaLunaLogo
    from .svg_builder_realism_max import RealismMaxSVGBuilder
except ImportError:
    # Fallback pour exécution directe
    from logo_generator import ArkaliaLunaLogo
    from svg_builder_realism_max import RealismMaxSVGBuilder


class RealismMaxLogoGenerator(ArkaliaLunaLogo):
    """Générateur de logos ultra-réalistes avec effets organiques"""

    def __init__(self, output_dir: Optional[Path] = None):
        super().__init__(output_dir)
        # Remplace le SVG builder par défaut par le Realism Max
        self.svg_builder = RealismMaxSVGBuilder(self.variants_manager)
        self.logger.info("🌙 Realism Max Generator initialisé avec succès")

    def generate_realistic_logo(
        self,
        variant_name: str,
        size: int = 200,
        realism_level: float = 0.95,
    ) -> Path:
        """Génère un logo ultra-réaliste avec niveau de réalisme configurable"""
        try:
            self.logger.info(
                f"🎨 Génération logo ultra-réaliste '{variant_name}' "
                f"niveau {realism_level:.2f}",
            )

            # Validation de la variante
            if not self.variants_manager.validate_variant(variant_name):
                raise ValueError(f"Variante '{variant_name}' non reconnue")

            # Construction du chemin de sortie avec suffixe réalisme
            output_path = (
                self.output_dir / f"arkalia-luna-realism-{variant_name}-{size}.svg"
            )

            # Génération avec le builder Realism Max
            self.svg_builder.save_logo(variant_name, size, output_path)

            self.logger.info(f"✅ Logo ultra-réaliste généré : {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(f"❌ Erreur génération réaliste '{variant_name}': {e}")
            raise

    def generate_all_realistic_variants(
        self,
        size: int = 200,
        realism_level: float = 0.95,
    ) -> List[Path]:
        """Génère toutes les variantes en mode ultra-réaliste"""
        try:
            self.logger.info(
                f"🎨 Génération de toutes les variantes ultra-réalistes "
                f"niveau {realism_level:.2f}",
            )

            generated_files = []
            variants = self.variants_manager.list_variants()

            for variant in variants:
                try:
                    output_path = self.generate_realistic_logo(
                        variant,
                        size,
                        realism_level,
                    )
                    generated_files.append(output_path)
                except Exception as e:
                    self.logger.error(f"❌ Échec variante réaliste '{variant}': {e}")
                    continue

            self.logger.info(
                f"✅ Génération réaliste terminée : "
                f"{len(generated_files)}/{len(variants)} logos créés",
            )
            return generated_files

        except Exception as e:
            self.logger.error(f"❌ Erreur génération réaliste globale: {e}")
            raise

    def create_realistic_favicon(
        self,
        variant_name: str,
        size: int = 32,
        realism_level: float = 0.95,
    ) -> Path:
        """Crée un favicon ultra-réaliste avec effets organiques"""
        try:
            self.logger.info(
                f"🎨 Création favicon ultra-réaliste '{variant_name}' "
                f"niveau {realism_level:.2f}",
            )

            # Utilise la méthode parent mais avec le builder réaliste
            return super().create_favicon(variant_name, size)

        except Exception as e:
            self.logger.error(
                f"❌ Erreur création favicon réaliste '{variant_name}': {e}",
            )
            raise
