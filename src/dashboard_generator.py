"""
🌙 Dashboard Logo Generator Module
Générateur de logos dashboard/networking synthétiques avec optimisations
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from .logo_generator import ArkaliaLunaLogo
    from .svg_builder_dashboard import DashboardSVGBuilder
except ImportError:
    # Fallback pour exécution directe
    from logo_generator import ArkaliaLunaLogo
    from svg_builder_dashboard import DashboardSVGBuilder


class DashboardLogoGenerator(ArkaliaLunaLogo):
    """Générateur dashboard optimisé pour les interfaces et réseaux"""

    def __init__(self, output_dir: Optional[Path] = None):
        super().__init__(output_dir)
        # Remplace le SVG builder par défaut par le Dashboard
        self.svg_builder = DashboardSVGBuilder(self.variants_manager)
        self.logger.info("📊 Dashboard Generator initialisé avec succès")

        # Configuration dashboard
        self.network_mode = True
        self.synthetic_style = True
        self.interface_optimized = True

    def generate_dashboard_logo(
        self, variant_name: str, size: int = 200, network_style: bool = True
    ) -> Path:
        """Génère un logo dashboard avec style réseau configurable"""
        try:
            self.logger.info(
                f"📊 Génération logo dashboard '{variant_name}' "
                f"style réseau: {network_style}"
            )

            # Validation de la variante
            if not self.variants_manager.validate_variant(variant_name):
                raise ValueError(f"Variante '{variant_name}' non reconnue")

            # Construction du chemin de sortie avec suffixe dashboard
            output_path = (
                self.output_dir / f"arkalia-luna-dashboard-{variant_name}-{size}.svg"
            )

            # Génération avec le builder Dashboard
            self.svg_builder.save_logo(variant_name, size, output_path)

            self.logger.info(f"✅ Logo dashboard généré : {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(f"❌ Erreur génération dashboard '{variant_name}': {e}")
            raise

    def generate_all_dashboard_variants(
        self, size: int = 200, network_style: bool = True
    ) -> List[Path]:
        """Génère toutes les variantes en mode dashboard"""
        try:
            self.logger.info(
                f"📊 Génération de toutes les variantes dashboard "
                f"style réseau: {network_style}"
            )

            generated_files = []
            variants = self.variants_manager.list_variants()

            for variant in variants:
                try:
                    output_path = self.generate_dashboard_logo(
                        variant, size, network_style
                    )
                    generated_files.append(output_path)
                except Exception as e:
                    self.logger.error(f"❌ Échec variante dashboard '{variant}': {e}")
                    continue

            self.logger.info(
                f"✅ Génération dashboard terminée : "
                f"{len(generated_files)}/{len(variants)} logos créés"
            )
            return generated_files

        except Exception as e:
            self.logger.error(f"❌ Erreur génération dashboard globale: {e}")
            raise

    def create_dashboard_favicon(
        self, variant_name: str, size: int = 32, network_style: bool = True
    ) -> Path:
        """Crée un favicon dashboard optimisé interface"""
        try:
            self.logger.info(
                f"📊 Création favicon dashboard '{variant_name}' "
                f"style réseau: {network_style}"
            )

            # Utilise la méthode parent mais avec le builder dashboard
            return super().create_favicon(variant_name, size)

        except Exception as e:
            self.logger.error(
                f"❌ Erreur création favicon dashboard '{variant_name}': {e}"
            )
            raise

    def toggle_network_mode(self, enabled: bool = True) -> None:
        """Active/désactive le mode réseau"""
        self.network_mode = enabled
        self.logger.info(f"📊 Mode réseau: {'activé' if enabled else 'désactivé'}")

    def toggle_synthetic_style(self, enabled: bool = True) -> None:
        """Active/désactive le style synthétique"""
        self.synthetic_style = enabled
        self.logger.info(
            f"📊 Style synthétique: {'activé' if enabled else 'désactivé'}"
        )

    def toggle_interface_optimization(self, enabled: bool = True) -> None:
        """Active/désactive l'optimisation interface"""
        self.interface_optimized = enabled
        self.logger.info(
            f"📊 Optimisation interface: {'activée' if enabled else 'désactivée'}"
        )

    def get_dashboard_stats(self) -> Dict[str, Any]:
        """Retourne les statistiques dashboard"""
        return {
            "network_mode": self.network_mode,
            "synthetic_style": self.synthetic_style,
            "interface_optimized": self.interface_optimized,
            "generator_type": "Dashboard",
            "optimizations": [
                "Style synthétique",
                "Interface optimisée",
                "Réseau simplifié",
            ],
        }
