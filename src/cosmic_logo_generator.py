"""
🌌 Cosmic Logo Generator
Générateur spécialisé pour les logos avec sphères cosmiques lumineuses
"""

from pathlib import Path
from typing import Optional

from .cosmic_sphere_builder import CosmicSphereBuilder
from .logo_generator import ArkaliaLunaLogo


class CosmicLogoGenerator(ArkaliaLunaLogo):
    """Générateur de logos avec sphères cosmiques et réseaux neuronaux"""

    def __init__(self, output_dir: Optional[Path] = None):
        # Appel du constructeur parent avec répertoire spécialisé
        super().__init__(output_dir or Path("exports-cosmic"))

        self.logger.info("🌌 Cosmic Logo Generator initialisé avec succès")

        # Remplacement du SVG builder par le builder cosmique
        self.svg_builder = CosmicSphereBuilder()

    def get_generator_stats(self) -> dict:
        """Retourne les statistiques du générateur cosmique"""
        return {
            "generator_type": "Cosmic Sphere",
            "features": [
                "Sphères cosmiques lumineuses",
                "Réseaux neuronaux internes",
                "Cristaux centraux brillants",
                "Dégradés fluides bleu/violet/cyan",
                "Particules cosmiques flottantes",
                "Halo lumineux",
                "Texture de surface réaliste",
                "Filtres de glow avancés",
            ],
            "inspiration": "Images d'inspiration utilisateur - esthétique cosmique moderne",
            "quality": "Haute qualité - reproduction fidèle de l'inspiration",
        }
