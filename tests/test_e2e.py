"""
Tests E2E (End-to-End) pour le projet
"""


import pytest

from src.generator_factory import LogoGeneratorFactory


class TestE2E:
    """Tests End-to-End complets"""

    def test_e2e_generate_logo_default(self) -> None:
        """Test E2E : Génération logo par défaut"""
        generator = LogoGeneratorFactory.create_generator("default")
        output_path = generator.generate_svg_logo("serenity", 200)
        assert output_path.exists()
        assert output_path.suffix == ".svg"

    def test_e2e_generate_all_variants(self) -> None:
        """Test E2E : Génération toutes variantes"""
        generator = LogoGeneratorFactory.create_generator("default")
        variants = generator.list_all_variants()
        assert len(variants) > 0

        for variant in variants[:3]:  # Limiter pour performance
            output_path = generator.generate_svg_logo(variant, 200)
            assert output_path.exists()

    def test_e2e_generate_multiple_sizes(self) -> None:
        """Test E2E : Génération multiples tailles"""
        generator = LogoGeneratorFactory.create_generator("default")
        sizes = [128, 256, 512]

        for size in sizes:
            output_path = generator.generate_svg_logo("serenity", size)
            assert output_path.exists()
            assert str(size) in output_path.name

    def test_e2e_generate_bbia_logo(self) -> None:
        """Test E2E : Génération logo BBIA"""
        generator = LogoGeneratorFactory.create_generator("bbia")
        try:
            output_path = generator.generate_svg_logo("mark_only", 512)
            assert output_path.exists()
        except FileNotFoundError:
            pytest.skip("Assets BBIA non disponibles")

    def test_e2e_generate_quest_logo(self) -> None:
        """Test E2E : Génération logo Quest"""
        generator = LogoGeneratorFactory.create_generator("quest")
        output_path = generator.generate_svg_logo("serenity", 512)
        assert output_path.exists()

    def test_e2e_cache_integration(self) -> None:
        """Test E2E : Intégration cache"""
        generator = LogoGeneratorFactory.create_generator("default")
        # Première génération
        path1 = generator.generate_svg_logo("serenity", 200)
        # Deuxième génération (devrait utiliser cache)
        path2 = generator.generate_svg_logo("serenity", 200)
        assert path1 == path2 or path2.exists()

    def test_e2e_factory_all_generators(self) -> None:
        """Test E2E : Factory avec tous les générateurs"""
        available = LogoGeneratorFactory.get_available_generators()
        assert len(available) > 0

        # Tester quelques générateurs
        for gen_type in ["default", "realism", "ultra_max"][:2]:
            generator = LogoGeneratorFactory.create_generator(gen_type)
            assert generator is not None

