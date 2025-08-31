"""
Configuration pytest pour les tests Arkalia-LUNA Logo
"""

import sys
from pathlib import Path

# Ajouter le répertoire src au PYTHONPATH
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))
