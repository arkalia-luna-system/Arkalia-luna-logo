"""
Tests de couverture pour améliorer la couverture de generator_factory.py.
Objectif : 40% → 70%+
"""

from pathlib import Path

import pytest

from src.generator_factory import LogoGeneratorFactory


class TestGeneratorFactoryCoverage:
    """Tests pour améliorer la couverture de generator_factory.py."""

    def test_factory_import(self):
        """Test que la factory peut être importée."""
        assert LogoGeneratorFactory is not None
        assert hasattr(LogoGeneratorFactory, "create_generator")

    def test_factory_create_generator_default(self):
        """Test de création d'un générateur par défaut."""
        generator = LogoGeneratorFactory.create_generator("default")
        assert generator is not None
        assert hasattr(generator, "generate_svg_logo")

    def test_factory_create_generator_realism(self):
        """Test de création d'un générateur realism."""
        generator = LogoGeneratorFactory.create_generator("realism")
        assert generator is not None
        assert hasattr(generator, "generate_svg_logo")

    def test_factory_create_generator_ultra_max(self):
        """Test de création d'un générateur ultra max."""
        generator = LogoGeneratorFactory.create_generator("ultra_max")
        assert generator is not None
        assert hasattr(generator, "generate_svg_logo")

    def test_factory_create_generator_simple_advanced(self):
        """Test de création d'un générateur simple-advanced."""
        generator = LogoGeneratorFactory.create_generator("simple_advanced")
        assert generator is not None
        assert hasattr(generator, "generate_svg_logo")

    def test_factory_create_generator_dashboard(self):
        """Test de création d'un générateur dashboard."""
        generator = LogoGeneratorFactory.create_generator("dashboard")
        assert generator is not None
        assert hasattr(generator, "generate_svg_logo")

    def test_factory_create_generator_ai_moon(self):
        """Test de création d'un générateur AI Moon."""
        generator = LogoGeneratorFactory.create_generator("ai_moon")
        assert generator is not None
        assert hasattr(generator, "generate_svg_logo")

    def test_factory_create_generator_advanced(self):
        """Test de création d'un générateur avancé."""
        generator = LogoGeneratorFactory.create_generator("advanced")
        assert generator is not None
        assert hasattr(generator, "generate_svg_logo")

    def test_factory_create_generator_ultimate(self):
        """Test de création d'un générateur ultimate."""
        generator = LogoGeneratorFactory.create_generator("ultimate")
        assert generator is not None
        assert hasattr(generator, "generate_svg_logo")

    def test_factory_invalid_generator_type(self):
        """Test de gestion d'un type de générateur invalide."""
        with pytest.raises(ValueError) as exc_info:
            LogoGeneratorFactory.create_generator("invalid_type")

        assert "Type de générateur" in str(exc_info.value)

    def test_factory_none_generator_type(self):
        """Test de gestion d'un type de générateur None."""
        with pytest.raises(ValueError) as exc_info:
            LogoGeneratorFactory.create_generator(None)

        assert "Type de générateur" in str(exc_info.value)

    def test_factory_empty_generator_type(self):
        """Test de gestion d'un type de générateur vide."""
        with pytest.raises(ValueError) as exc_info:
            LogoGeneratorFactory.create_generator("")

        assert "Type de générateur" in str(exc_info.value)

    def test_factory_available_generators(self):
        """Test que tous les types de générateurs sont disponibles."""
        available_generators = LogoGeneratorFactory.get_available_generators()

        expected_types = [
            "default",
            "realism",
            "ultra_max",
            "simple_advanced",
            "dashboard",
            "ai_moon",
            "advanced",
            "ultimate",
        ]

        for expected_type in expected_types:
            assert (
                expected_type in available_generators
            ), f"Type {expected_type} manquant"

    def test_factory_generator_creation_with_output_dir(self):
        """Test de création de générateur avec répertoire de sortie."""
        output_dir = Path("test_output")
        generator = LogoGeneratorFactory.create_generator(
            "default", output_dir=output_dir
        )

        assert generator is not None
        assert hasattr(generator, "generate_svg_logo")

    def test_factory_generator_cache(self):
        """Test du cache des générateurs."""
        # Créer un premier générateur
        generator1 = LogoGeneratorFactory.create_generator("default")

        # Créer un second avec le même type (devrait utiliser le cache)
        generator2 = LogoGeneratorFactory.create_generator("default")

        assert generator1 is not None
        assert generator2 is not None

    def test_factory_clear_cache(self):
        """Test du nettoyage du cache."""
        # Créer un générateur pour remplir le cache
        LogoGeneratorFactory.create_generator("default")

        # Vider le cache
        LogoGeneratorFactory.clear_cache()

        # Le cache devrait être vide
        assert len(LogoGeneratorFactory._generators_cache) == 0

    def test_factory_generator_types_constant(self):
        """Test de la constante GENERATOR_TYPES."""
        assert hasattr(LogoGeneratorFactory, "GENERATOR_TYPES")
        assert isinstance(LogoGeneratorFactory.GENERATOR_TYPES, dict)
        assert len(LogoGeneratorFactory.GENERATOR_TYPES) > 0

    def test_factory_generator_inheritance(self):
        """Test que tous les générateurs héritent de la bonne classe."""
        from src.logo_generator import ArkaliaLunaLogo

        for generator_type in LogoGeneratorFactory.GENERATOR_TYPES:
            generator = LogoGeneratorFactory.create_generator(generator_type)
            assert isinstance(generator, ArkaliaLunaLogo)

    def test_factory_generator_methods_consistency(self):
        """Test de la cohérence des méthodes entre générateurs."""
        base_methods = ["generate_svg_logo", "generate_all_variants"]

        for generator_type in LogoGeneratorFactory.GENERATOR_TYPES:
            generator = LogoGeneratorFactory.create_generator(generator_type)

            for method_name in base_methods:
                assert hasattr(
                    generator, method_name
                ), f"Générateur {generator_type} manque {method_name}"

    def test_factory_generator_output_directory(self):
        """Test de la gestion du répertoire de sortie."""
        # Test sans répertoire spécifique
        generator1 = LogoGeneratorFactory.create_generator("default")
        assert generator1 is not None

        # Test avec répertoire spécifique
        test_dir = Path("test_output")
        generator2 = LogoGeneratorFactory.create_generator(
            "default", output_dir=test_dir
        )
        assert generator2 is not None

    def test_factory_generator_cache_key_uniqueness(self):
        """Test de l'unicité des clés de cache."""
        # Créer des générateurs avec différents répertoires
        generator1 = LogoGeneratorFactory.create_generator(
            "default", output_dir=Path("dir1")
        )
        generator2 = LogoGeneratorFactory.create_generator(
            "default", output_dir=Path("dir2")
        )

        assert generator1 is not None
        assert generator2 is not None
        # Ils devraient être différents car répertoires différents
        assert generator1 is not generator2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
