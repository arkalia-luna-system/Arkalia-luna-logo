"""
🌙 SVG Builder Module
Construction des logos SVG Arkalia-LUNA de base
"""

from abc import ABC, abstractmethod
from typing import Any

import svgwrite

# Types simplifiés pour éviter les conflits
LogoVariant = Any
LogoVariants = Any


class SVGBuilder(ABC):
    """Constructeur SVG professionnel pour les logos Arkalia-LUNA"""

    def __init__(self, variants_manager: LogoVariants):
        self.variants_manager = variants_manager
        self._validate_svgwrite()

    def _validate_svgwrite(self):
        """Valide que svgwrite est correctement installé"""
        if svgwrite is None:
            raise ImportError(
                "Module svgwrite requis. Installez-le avec: pip install svgwrite"
            )

        if not hasattr(svgwrite, "Drawing"):
            raise ImportError("Module svgwrite invalide")

    @abstractmethod
    def build_logo(self, variant_name: str, size: int) -> svgwrite.Drawing:
        """Méthode abstraite à implémenter par chaque builder spécialisé"""
        pass

    def save_logo(self, variant_name: str, size: int, output_path: Any) -> None:
        """Sauvegarde un logo SVG en utilisant build_logo()"""
        try:
            # Récupération de la variante
            variant = self.variants_manager.get_variant(variant_name)
            if not variant:
                raise ValueError(f"Variante '{variant_name}' non trouvée")

            # Construction du logo avec la méthode abstraite
            drawing = self.build_logo(variant_name, size)

            # Sauvegarde avec gestion des Path objects
            if hasattr(output_path, "open"):
                # C'est un Path object
                with output_path.open("w", encoding="utf-8") as f:
                    drawing.write(f, pretty=True)
            else:
                # C'est un objet fichier ou une chaîne
                drawing.write(output_path, pretty=True)

        except Exception as e:
            raise RuntimeError(f"Erreur lors de la sauvegarde du logo: {e}") from e

    def create_drawing(self, size: int) -> svgwrite.Drawing:
        """Crée un dessin SVG de base (méthode utilitaire)"""
        return svgwrite.Drawing(size=(size, size), viewBox=f"0 0 {size} {size}")
