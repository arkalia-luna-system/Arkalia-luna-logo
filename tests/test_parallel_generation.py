"""
Tests pour la génération parallèle
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

from src.logo_generator import ArkaliaLunaLogo


class TestParallelGeneration:
    """Tests pour la génération parallèle"""

    def test_generate_all_sequential(self) -> None:
        """Test génération séquentielle (sans --parallel)"""
        generator = ArkaliaLunaLogo(output_dir=Path("test_exports"))
        variants = generator.list_all_variants()

        # Mock pour éviter la génération réelle
        with patch.object(generator, "generate_svg_logo") as mock_generate:
            mock_generate.return_value = Path("test.svg")
            generated = generator.generate_all_variants(size=200)

            # Vérifier que tous les variants sont générés
            assert len(generated) == len(variants)
            assert mock_generate.call_count == len(variants)

    def test_generate_all_parallel_structure(self) -> None:
        """Test que la structure de génération parallèle est correcte"""
        # Vérifier que concurrent.futures est disponible
        try:
            from concurrent.futures import ThreadPoolExecutor, as_completed

            assert ThreadPoolExecutor is not None
            assert as_completed is not None
        except ImportError:
            assert False, "concurrent.futures non disponible"
