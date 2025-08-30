"""
🌙 AI Moon Generator Module
Générateur de logos LUNE IA ultra-réaliste
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from .logo_generator import ArkaliaLunaLogo
    from .svg_builder_ai_moon import AIMoonSVGBuilder
except ImportError:
    # Fallback pour exécution directe
    from logo_generator import ArkaliaLunaLogo
    from svg_builder_ai_moon import AIMoonSVGBuilder


class AIMoonLogoGenerator(ArkaliaLunaLogo):
    """Générateur de la LUNE IA VIVANTE ultra-réaliste et organique"""

    def __init__(self, output_dir: Optional[Path] = None):
        # Appel du constructeur parent avec répertoire spécialisé
        super().__init__(output_dir or Path("exports-ai-moon"))

        # Remplace le SVG builder par défaut par l'AI Moon
        self.svg_builder = AIMoonSVGBuilder(self.variants_manager)
        self.logger.info("🌙 AI Moon Generator initialisé avec succès")

        # Configuration IA spécialisée
        self.ai_complexity = 0.95
        self.neural_layers = 8
        self.organic_effects = True

    def generate_ai_moon_logo(self, variant_name: str, size: int = 200) -> Path:
        """Génère un logo SVG LUNE IA pour une variante donnée"""
        try:
            self.logger.info(
                f"🌙 LUNE IA : Génération du logo '{variant_name}' "
                f"en taille {size}x{size}"
            )

            # Validation de la variante
            if not self.variants_manager.validate_variant(variant_name):
                raise ValueError(f"Variante '{variant_name}' non reconnue")

            # Construction du chemin de sortie
            output_path = (
                self.output_dir / f"arkalia-luna-ai-moon-{variant_name}-{size}.svg"
            )

            # Génération et sauvegarde avec le builder LUNE IA
            self.svg_builder.save_ai_moon_logo(variant_name, size, output_path)

            self.logger.info(f"✨ Logo LUNE IA généré avec succès : {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(
                f"❌ Erreur lors de la génération LUNE IA '{variant_name}': {e}"
            )
            raise

    def generate_all_ai_moon_variants(self, size: int = 200) -> List[Path]:
        """Génère toutes les variantes du logo en style LUNE IA"""
        try:
            self.logger.info(
                f"🌙 LUNE IA : Génération de toutes les variantes "
                f"en taille {size}x{size}"
            )

            generated_files = []
            variants = self.variants_manager.list_variants()

            for variant in variants:
                try:
                    output_path = self.generate_ai_moon_logo(variant, size)
                    generated_files.append(output_path)
                    self.logger.info(f"✅ {variant} : {output_path.name}")
                except Exception as e:
                    self.logger.error(f"❌ {variant} : {e}")
                    continue

            self.logger.info(
                f"🎉 Génération LUNE IA terminée : "
                f"{len(generated_files)}/{len(variants)} logos créés"
            )
            return generated_files

        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la génération LUNE IA globale: {e}")
            raise

    def create_ai_moon_favicon(
        self, variant_name: str, size: int = 32, ai_enhanced: bool = True
    ) -> Path:
        """Crée un favicon LUNE IA avec effets IA"""
        try:
            self.logger.info(
                f"🌙 LUNE IA : Création favicon '{variant_name}' "
                f"effets IA: {ai_enhanced}"
            )

            # Utilise la méthode parent mais avec le builder AI Moon
            return super().create_favicon(variant_name, size)

        except Exception as e:
            self.logger.error(
                f"❌ Erreur création favicon LUNE IA '{variant_name}': {e}"
            )
            raise

    def set_ai_complexity(self, complexity: float) -> None:
        """Configure la complexité IA (0.1 à 1.0)"""
        if 0.1 <= complexity <= 1.0:
            self.ai_complexity = complexity
            self.logger.info(f"🧠 Complexité IA configurée: {complexity:.2f}")
        else:
            raise ValueError("Complexité IA doit être entre 0.1 et 1.0")

    def set_neural_layers(self, layers: int) -> None:
        """Configure le nombre de couches neuronales (1 à 16)"""
        if 1 <= layers <= 16:
            self.neural_layers = layers
            self.logger.info(f"🕸️ Couches neuronales configurées: {layers}")
        else:
            raise ValueError("Couches neuronales doit être entre 1 et 16")

    def toggle_organic_effects(self, enabled: bool = True) -> None:
        """Active/désactive les effets organiques"""
        self.organic_effects = enabled
        self.logger.info(
            f"🌱 Effets organiques: {'activés' if enabled else 'désactivés'}"
        )

    def get_ai_stats(self) -> Dict[str, Any]:
        """Retourne les statistiques IA"""
        return {
            "ai_complexity": self.ai_complexity,
            "neural_layers": self.neural_layers,
            "organic_effects": self.organic_effects,
            "generator_type": "AIMoon",
            "optimizations": [
                "Gradients IA optimisés",
                "Filtres organiques",
                "Réseaux neuronaux",
            ],
        }
