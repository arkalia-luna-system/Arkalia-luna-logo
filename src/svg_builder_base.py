"""
Base SVG Builder
Classe de base pour tous les builders SVG
"""

import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional


class SVGBuilder(ABC):
    """Classe de base abstraite pour tous les builders SVG"""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.builder_type = "base"

    @abstractmethod
    def build_logo(
        self, variant_name: str, size: int = 200, output_dir: Optional[Path] = None
    ) -> str:
        """Construit un logo SVG pour une variante donnée"""
        pass

    def get_builder_stats(self) -> dict:
        """Retourne les statistiques du builder"""
        return {
            "builder_type": self.builder_type,
            "features": [],
            "quality": "standard",
        }
