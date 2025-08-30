"""
🌙 Ultimate Logo Generator Module
Générateur de logos ULTIMES Arkalia-LUNA avec effets cosmiques extrêmes
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from .logo_generator import ArkaliaLunaLogo
    from .svg_builder_ultimate import UltimateSVGBuilder
except ImportError:
    # Fallback pour exécution directe
    from logo_generator import ArkaliaLunaLogo
    from svg_builder_ultimate import UltimateSVGBuilder


class UltimateLogoGenerator(ArkaliaLunaLogo):
    """Générateur de logos ULTIMES Arkalia-LUNA avec effets cosmiques extrêmes"""

    def __init__(self, output_dir: Optional[Path] = None):
        # Appel du constructeur parent avec répertoire spécialisé
        super().__init__(output_dir or Path("exports-ultimate"))

        # Remplace le SVG builder par défaut par l'Ultimate
        self.svg_builder = UltimateSVGBuilder(self.variants_manager)
        self.logger.info("🌟 Ultimate Generator initialisé avec succès")

        # Configuration ULTIME spécialisée
        self.cosmic_complexity = 0.98
        self.ultimate_effects = True
        self.holographic_mode = True

        # Statistiques ULTIMES avancées
        self.ultimate_stats = {
            "total_files": 0,
            "ultimate_svg_logos": 0,
            "ultimate_png_favicons": 0,
            "cosmic_complexity": self.cosmic_complexity,
            "ultimate_effects": self.ultimate_effects,
            "holographic_mode": self.holographic_mode,
        }

    def generate_ultimate_logo(
        self, variant_name: str, size: int = 200, cosmic_level: float = 0.98
    ) -> Path:
        """Génère un logo ULTIME avec niveau cosmique configurable"""
        try:
            self.logger.info(
                f"🌟 ULTIME : Génération du logo '{variant_name}' "
                f"niveau cosmique {cosmic_level:.2f}"
            )

            # Validation de la variante
            if not self.variants_manager.validate_variant(variant_name):
                raise ValueError(f"Variante '{variant_name}' non reconnue")

            # Mise à jour du niveau cosmique
            self.cosmic_complexity = max(0.1, min(1.0, cosmic_level))

            # Construction du chemin de sortie avec suffixe ultimate
            output_path = (
                self.output_dir / f"arkalia-luna-ultimate-{variant_name}-{size}.svg"
            )

            # Génération avec le builder ULTIME
            self.svg_builder.save_ultimate_logo(variant_name, size, output_path)

            # Mise à jour des statistiques
            self.ultimate_stats["ultimate_svg_logos"] += 1
            self.ultimate_stats["total_files"] += 1

            self.logger.info(f"✨ Logo ULTIME généré avec succès : {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(f"❌ Erreur génération ULTIME '{variant_name}': {e}")
            raise

    def generate_all_ultimate_variants(
        self, size: int = 200, cosmic_level: float = 0.98
    ) -> List[Path]:
        """Génère toutes les variantes en mode ULTIME"""
        try:
            self.logger.info(
                f"🌟 ULTIME : Génération de toutes les variantes "
                f"niveau cosmique {cosmic_level:.2f}"
            )

            generated_files = []
            variants = self.variants_manager.list_variants()

            for variant in variants:
                try:
                    output_path = self.generate_ultimate_logo(
                        variant, size, cosmic_level
                    )
                    generated_files.append(output_path)
                except Exception as e:
                    self.logger.error(f"❌ Échec variante ULTIME '{variant}': {e}")
                    continue

            self.logger.info(
                f"✅ Génération ULTIME terminée : "
                f"{len(generated_files)}/{len(variants)} logos créés"
            )
            return generated_files

        except Exception as e:
            self.logger.error(f"❌ Erreur génération ULTIME globale: {e}")
            raise

    def create_ultimate_favicon(
        self, variant_name: str, size: int = 32, cosmic_level: float = 0.98
    ) -> Path:
        """Crée un favicon ULTIME avec effets cosmiques"""
        try:
            self.logger.info(
                f"🌟 ULTIME : Création favicon '{variant_name}' "
                f"niveau cosmique {cosmic_level:.2f}"
            )

            # Utilise la méthode parent mais avec le builder ULTIME
            favicon_path = super().create_favicon(variant_name, size)

            # Mise à jour des statistiques
            self.ultimate_stats["ultimate_png_favicons"] += 1
            self.ultimate_stats["total_files"] += 1

            return favicon_path

        except Exception as e:
            self.logger.error(
                f"❌ Erreur création favicon ULTIME '{variant_name}': {e}"
            )
            raise

    def set_cosmic_complexity(self, complexity: float) -> None:
        """Configure la complexité cosmique (0.1 à 1.0)"""
        if 0.1 <= complexity <= 1.0:
            self.cosmic_complexity = complexity
            self.ultimate_stats["cosmic_complexity"] = complexity
            self.logger.info(f"🌟 Complexité cosmique configurée: {complexity:.2f}")
        else:
            raise ValueError("Complexité cosmique doit être entre 0.1 et 1.0")

    def toggle_ultimate_effects(self, enabled: bool = True) -> None:
        """Active/désactive les effets ULTIMES"""
        self.ultimate_effects = enabled
        self.ultimate_stats["ultimate_effects"] = enabled
        self.logger.info(f"🌟 Effets ULTIMES: {'activés' if enabled else 'désactivés'}")

    def toggle_holographic_mode(self, enabled: bool = True) -> None:
        """Active/désactive le mode holographique"""
        self.holographic_mode = enabled
        self.ultimate_stats["holographic_mode"] = enabled
        self.logger.info(
            f"🌟 Mode holographique: {'activé' if enabled else 'désactivé'}"
        )

    def get_ultimate_stats(self) -> Dict[str, Any]:
        """Retourne les statistiques ULTIMES détaillées"""
        return {
            **self.ultimate_stats,
            "generator_type": "Ultimate",
            "optimizations": [
                "100+ stops de gradients cosmiques",
                "Effets de turbulence cosmique",
                "Masques organiques complexes",
                "20 particules cosmiques animées",
                "Effets holographiques extrêmes",
                "Auras d'énergie cosmiques",
            ],
        }

    def compare_with_other_versions(self) -> Dict[str, Any]:
        """Compare les versions ULTIME avec toutes les précédentes"""
        try:
            # Répertoires des autres versions
            other_dirs = {
                "basic": Path("exports"),
                "simple_advanced": Path("exports-simple-advanced"),
                "dashboard": Path("exports-dashboard"),
                "ultra_max": Path("exports-ultra-max"),
                "ai_moon": Path("exports-ai-moon"),
                "advanced": Path("exports-advanced"),
                "realism": Path("exports-realism"),
                "ultimate": self.output_dir,
            }

            comparison = {}
            for version_name, version_dir in other_dirs.items():
                if version_dir.exists():
                    svg_files = list(version_dir.glob("arkalia-luna-*.svg"))
                    png_files = list(version_dir.glob("favicon-*.png"))
                    comparison[f"{version_name}_svg_count"] = len(svg_files)
                    comparison[f"{version_name}_png_count"] = len(png_files)
                    comparison[f"{version_name}_directory"] = str(version_dir)
                else:
                    comparison[f"{version_name}_svg_count"] = 0
                    comparison[f"{version_name}_png_count"] = 0
                    comparison[f"{version_name}_directory"] = "N/A"

            return comparison

        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la comparaison : {e}")
            raise

    def cleanup_ultimate_files(self) -> int:
        """Nettoie tous les fichiers ULTIME générés"""
        try:
            count = 0
            for file_path in self.output_dir.glob("arkalia-luna-ultimate-*"):
                file_path.unlink()
                count += 1

            for file_path in self.output_dir.glob("favicon-*"):
                file_path.unlink()
                count += 1

            # Réinitialisation des statistiques
            self.ultimate_stats["total_files"] = 0
            self.ultimate_stats["ultimate_svg_logos"] = 0
            self.ultimate_stats["ultimate_png_favicons"] = 0

            self.logger.info(
                f"🧹 Nettoyage ULTIME terminé : {count} fichiers supprimés"
            )
            return count

        except Exception as e:
            self.logger.error(f"❌ Erreur lors du nettoyage ULTIME : {e}")
            raise
