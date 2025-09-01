"""
Tests pour améliorer la couverture du module generator_factory.py
Objectif : 57% → 80% de couverture
"""

import shutil
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from src.generator_factory import (
    LogoGeneratorFactory,
    benchmark_all_generators,
    create_logo_generator,
)
from src.logo_generator import ArkaliaLunaLogo


class TestLogoGeneratorFactory:
    """Tests pour LogoGeneratorFactory"""

    @pytest.fixture
    def temp_output_dir(self):
        """Répertoire temporaire pour les tests"""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def mock_generator(self):
        """Générateur mock pour les tests"""
        generator = Mock(spec=ArkaliaLunaLogo)
        generator.generate_svg_logo.return_value = Path("test.svg")
        return generator

    def test_clear_cache(self):
        """Test de vidage du cache"""
        # Ajouter un élément au cache
        LogoGeneratorFactory._generators_cache["test"] = "test_value"
        assert "test" in LogoGeneratorFactory._generators_cache

        # Vider le cache
        LogoGeneratorFactory.clear_cache()
        assert len(LogoGeneratorFactory._generators_cache) == 0

    def test_get_cache_stats_empty_cache(self):
        """Test des statistiques du cache vide"""
        # Vider le cache d'abord
        LogoGeneratorFactory.clear_cache()

        stats = LogoGeneratorFactory.get_cache_stats()

        assert stats["cached_generators"] == 0
        assert stats["cache_keys"] == []
        assert "Optimisé avec pattern Singleton" in stats["memory_usage"]

    def test_get_cache_stats_with_cache(self):
        """Test des statistiques du cache avec éléments"""
        # Ajouter des éléments au cache
        LogoGeneratorFactory._generators_cache["test1"] = "value1"
        LogoGeneratorFactory._generators_cache["test2"] = "value2"

        stats = LogoGeneratorFactory.get_cache_stats()

        assert stats["cached_generators"] == 2
        assert "test1" in stats["cache_keys"]
        assert "test2" in stats["cache_keys"]
        assert "Optimisé avec pattern Singleton" in stats["memory_usage"]

        # Nettoyer
        LogoGeneratorFactory.clear_cache()

    def test_create_all_generators_success(self, temp_output_dir):
        """Test de création de tous les générateurs avec succès"""
        with patch(
            "src.generator_factory.LogoGeneratorFactory.create_generator"
        ) as mock_create:
            mock_create.return_value = Mock(spec=ArkaliaLunaLogo)

            generators = LogoGeneratorFactory.create_all_generators(temp_output_dir)

            # Vérifier que tous les types de générateurs ont été créés
            expected_types = LogoGeneratorFactory.GENERATOR_TYPES
            assert len(generators) == len(expected_types)

            for generator_type in expected_types:
                assert generator_type in generators

    def test_create_all_generators_with_errors(self, temp_output_dir):
        """Test de création de tous les générateurs avec erreurs"""
        with patch(
            "src.generator_factory.LogoGeneratorFactory.create_generator"
        ) as mock_create:
            # Simuler des erreurs pour certains générateurs
            def side_effect(generator_type, output_dir, use_cache=False):
                if generator_type in ["realism", "ultra_max"]:
                    raise Exception(f"Erreur pour {generator_type}")
                return Mock(spec=ArkaliaLunaLogo)

            mock_create.side_effect = side_effect

            generators = LogoGeneratorFactory.create_all_generators(temp_output_dir)

            # Les générateurs avec erreurs ne devraient pas être dans le résultat
            assert "realism" not in generators
            assert "ultra_max" not in generators
            # Mais les autres devraient être présents
            assert "default" in generators
            assert "simple_advanced" in generators

    def test_benchmark_generators_success(self, temp_output_dir):
        """Test de benchmark des générateurs avec succès"""
        with patch(
            "src.generator_factory.LogoGeneratorFactory.create_all_generators"
        ) as mock_create_all:
            # Créer des générateurs mock avec méthodes de génération
            mock_generators = {}
            for generator_type in ["default", "simple_advanced"]:
                mock_gen = Mock(spec=ArkaliaLunaLogo)
                mock_gen.generate_svg_logo.return_value = Path("test.svg")
                mock_generators[generator_type] = mock_gen

            mock_create_all.return_value = mock_generators

            results = LogoGeneratorFactory.benchmark_generators(
                temp_output_dir, "serenity", 200
            )

            # Vérifier que les résultats contiennent des temps
            assert "default" in results
            assert "simple_advanced" in results
            assert isinstance(results["default"], float)
            assert isinstance(results["simple_advanced"], float)

    def test_benchmark_generators_with_errors(self, temp_output_dir):
        """Test de benchmark des générateurs avec erreurs"""
        with patch(
            "src.generator_factory.LogoGeneratorFactory.create_all_generators"
        ) as mock_create_all:
            # Créer des générateurs mock avec erreurs
            mock_generators = {}
            for generator_type in ["default", "realism"]:
                mock_gen = Mock(spec=ArkaliaLunaLogo)
                if generator_type == "realism":
                    mock_gen.generate_svg_logo.side_effect = Exception(
                        "Erreur de génération"
                    )
                else:
                    mock_gen.generate_svg_logo.return_value = Path("test.svg")
                mock_generators[generator_type] = mock_gen

            mock_create_all.return_value = mock_generators

            results = LogoGeneratorFactory.benchmark_generators(
                temp_output_dir, "serenity", 200
            )

            # Vérifier que les erreurs sont gérées
            assert "default" in results
            assert "realism" in results
            assert isinstance(results["default"], float)
            assert "Erreur:" in str(results["realism"])

    def test_benchmark_generators_method_detection(self, temp_output_dir):
        """Test de détection automatique des méthodes de génération"""
        with patch(
            "src.generator_factory.LogoGeneratorFactory.create_all_generators"
        ) as mock_create_all:
            # Créer un générateur avec méthode spécifique
            mock_gen = Mock(spec=ArkaliaLunaLogo)
            # Ajouter la méthode spécifique au mock
            mock_gen.generate_realism_logo = Mock(return_value=Path("test.svg"))
            mock_generators = {"realism": mock_gen}

            mock_create_all.return_value = mock_generators

            results = LogoGeneratorFactory.benchmark_generators(
                temp_output_dir, "serenity", 200
            )

            assert "realism" in results
            assert isinstance(results["realism"], float)

    def test_benchmark_generators_fallback_method(self, temp_output_dir):
        """Test de fallback sur la méthode standard"""
        with patch(
            "src.generator_factory.LogoGeneratorFactory.create_all_generators"
        ) as mock_create_all:
            # Créer un générateur sans méthode spécifique
            mock_gen = Mock(spec=ArkaliaLunaLogo)
            mock_gen.generate_svg_logo.return_value = Path("test.svg")
            mock_generators = {"custom": mock_gen}

            mock_create_all.return_value = mock_generators

            results = LogoGeneratorFactory.benchmark_generators(
                temp_output_dir, "serenity", 200
            )

            assert "custom" in results
            assert isinstance(results["custom"], float)

    def test_benchmark_generators_different_variants(self, temp_output_dir):
        """Test de benchmark avec différentes variantes"""
        with patch(
            "src.generator_factory.LogoGeneratorFactory.create_all_generators"
        ) as mock_create_all:
            mock_gen = Mock(spec=ArkaliaLunaLogo)
            mock_gen.generate_svg_logo.return_value = Path("test.svg")
            mock_generators = {"default": mock_gen}

            mock_create_all.return_value = mock_generators

            # Test avec différentes variantes
            variants = ["serenity", "power", "creative"]
            for variant in variants:
                results = LogoGeneratorFactory.benchmark_generators(
                    temp_output_dir, variant, 200
                )
                assert "default" in results
                assert isinstance(results["default"], float)

    def test_benchmark_generators_different_sizes(self, temp_output_dir):
        """Test de benchmark avec différentes tailles"""
        with patch(
            "src.generator_factory.LogoGeneratorFactory.create_all_generators"
        ) as mock_create_all:
            mock_gen = Mock(spec=ArkaliaLunaLogo)
            mock_gen.generate_svg_logo.return_value = Path("test.svg")
            mock_generators = {"default": mock_gen}

            mock_create_all.return_value = mock_generators

            # Test avec différentes tailles
            sizes = [100, 200, 500, 1000]
            for size in sizes:
                results = LogoGeneratorFactory.benchmark_generators(
                    temp_output_dir, "serenity", size
                )
                assert "default" in results
                assert isinstance(results["default"], float)

    def test_create_generator_with_cache(self, temp_output_dir):
        """Test de création de générateur avec cache"""
        # Vider le cache d'abord
        LogoGeneratorFactory.clear_cache()

        # Créer un générateur avec cache
        generator1 = LogoGeneratorFactory.create_generator(
            "default", temp_output_dir, use_cache=True
        )
        generator2 = LogoGeneratorFactory.create_generator(
            "default", temp_output_dir, use_cache=True
        )

        # Les deux devraient être la même instance (cache)
        assert generator1 is generator2

        # Vérifier que le cache contient l'élément (clé avec répertoire)
        cache_key = f"default_{temp_output_dir}"
        assert cache_key in LogoGeneratorFactory._generators_cache

        # Nettoyer
        LogoGeneratorFactory.clear_cache()

    def test_create_generator_without_cache(self, temp_output_dir):
        """Test de création de générateur sans cache"""
        # Vider le cache d'abord
        LogoGeneratorFactory.clear_cache()

        # Créer des générateurs sans cache
        generator1 = LogoGeneratorFactory.create_generator(
            "default", temp_output_dir, use_cache=False
        )
        generator2 = LogoGeneratorFactory.create_generator(
            "default", temp_output_dir, use_cache=False
        )

        # Les deux devraient être des instances différentes
        assert generator1 is not generator2

        # Le cache ne devrait pas être utilisé
        assert len(LogoGeneratorFactory._generators_cache) == 0

    def test_create_generator_invalid_type(self, temp_output_dir):
        """Test de création de générateur avec type invalide"""
        with pytest.raises(
            ValueError, match="Type de générateur 'invalid_type' non reconnu"
        ):
            LogoGeneratorFactory.create_generator("invalid_type", temp_output_dir)

    def test_create_generator_all_types(self, temp_output_dir):
        """Test de création de tous les types de générateurs"""
        for generator_type in LogoGeneratorFactory.GENERATOR_TYPES:
            generator = LogoGeneratorFactory.create_generator(
                generator_type, temp_output_dir
            )
            assert generator is not None
            assert hasattr(generator, "generate_svg_logo")

    def test_get_generator_info(self):
        """Test de récupération des informations sur les générateurs"""
        # Vérifier que la méthode existe
        assert hasattr(LogoGeneratorFactory, "get_available_generators")

        info = LogoGeneratorFactory.get_available_generators()

        # Vérifier que toutes les informations sont présentes
        expected_keys = LogoGeneratorFactory.GENERATOR_TYPES
        for key in expected_keys:
            assert key in info
            assert isinstance(info[key], str)
            assert len(info[key]) > 0

    def test_singleton_pattern(self):
        """Test du pattern Singleton"""
        # Créer deux instances de la factory
        factory1 = LogoGeneratorFactory
        factory2 = LogoGeneratorFactory

        # Elles devraient être la même classe
        assert factory1 is factory2

        # Le cache devrait être partagé
        factory1._generators_cache["test"] = "value"
        assert "test" in factory2._generators_cache

        # Nettoyer
        LogoGeneratorFactory.clear_cache()


class TestUtilityFunctions:
    """Tests pour les fonctions utilitaires"""

    @pytest.fixture
    def temp_output_dir(self):
        """Répertoire temporaire pour les tests"""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    def test_create_logo_generator_default(self, temp_output_dir):
        """Test de la fonction utilitaire create_logo_generator avec type par défaut"""
        generator = create_logo_generator(output_dir=temp_output_dir)
        assert generator is not None
        assert hasattr(generator, "generate_svg_logo")

    def test_create_logo_generator_specific_type(self, temp_output_dir):
        """Test de la fonction utilitaire create_logo_generator avec type spécifique"""
        generator = create_logo_generator("simple_advanced", temp_output_dir)
        assert generator is not None
        assert hasattr(generator, "generate_svg_logo")

    def test_benchmark_all_generators(self, temp_output_dir):
        """Test de la fonction utilitaire benchmark_all_generators"""
        with patch(
            "src.generator_factory.LogoGeneratorFactory.benchmark_generators"
        ) as mock_benchmark:
            mock_benchmark.return_value = {"default": 0.001, "simple_advanced": 0.002}

            results = benchmark_all_generators(temp_output_dir)

            assert "default" in results
            assert "simple_advanced" in results
            assert results["default"] == 0.001
            assert results["simple_advanced"] == 0.002

    def test_utility_functions_integration(self, temp_output_dir):
        """Test d'intégration des fonctions utilitaires"""
        # Créer un générateur
        generator = create_logo_generator("default", temp_output_dir)
        assert generator is not None

        # Faire un benchmark
        with patch(
            "src.generator_factory.LogoGeneratorFactory.benchmark_generators"
        ) as mock_benchmark:
            mock_benchmark.return_value = {"default": 0.001}

            results = benchmark_all_generators(temp_output_dir)
            assert "default" in results
            assert results["default"] == 0.001
