"""
Tests de couverture pour améliorer la couverture de ultimate_generator.py.
Objectif : 22% → 70%+
Tests basés sur l'analyse du vrai code pour performance et précision.
"""

from pathlib import Path
from unittest.mock import patch

import pytest

from src.ultimate_generator import UltimateLogoGenerator


class TestUltimateGeneratorCoverage:
    """Tests pour améliorer la couverture de ultimate_generator.py."""

    @pytest.fixture
    def output_dir(self, tmp_path):
        """Fixture pour le répertoire de sortie temporaire."""
        return tmp_path / "exports-ultimate"

    @pytest.fixture
    def ultimate_generator(self, output_dir):
        """Fixture pour le générateur ultimate."""
        return UltimateLogoGenerator(output_dir)

    def test_ultimate_generator_import(self):
        """Test que le générateur ultimate peut être importé."""
        assert UltimateLogoGenerator is not None
        assert hasattr(UltimateLogoGenerator, "generate_ultimate_logo")

    def test_ultimate_generator_initialization(self, output_dir):
        """Test de l'initialisation du générateur ultimate."""
        generator = UltimateLogoGenerator(output_dir)

        assert generator is not None
        assert hasattr(generator, "cosmic_complexity")
        assert hasattr(generator, "ultimate_effects")
        assert hasattr(generator, "holographic_mode")
        assert hasattr(generator, "ultimate_stats")

        # Vérifier les valeurs par défaut
        assert generator.cosmic_complexity == 0.98
        assert generator.ultimate_effects is True
        assert generator.holographic_mode is True

    def test_ultimate_generator_default_output_dir(self):
        """Test de l'initialisation avec répertoire par défaut."""
        generator = UltimateLogoGenerator()

        assert generator is not None
        assert generator.output_dir == Path("exports-ultimate")

    def test_ultimate_generator_svg_builder_replacement(self, ultimate_generator):
        """Test que le SVG builder a été remplacé par l'Ultimate."""
        assert ultimate_generator.svg_builder is not None
        assert hasattr(ultimate_generator.svg_builder, "build_ultimate_logo")

    def test_ultimate_generator_ultimate_stats_initialization(self, ultimate_generator):
        """Test de l'initialisation des statistiques ultimate."""
        stats = ultimate_generator.ultimate_stats

        assert stats["total_files"] == 0
        assert stats["ultimate_svg_logos"] == 0
        assert stats["ultimate_png_favicons"] == 0
        assert stats["cosmic_complexity"] == 0.98
        assert stats["ultimate_effects"] is True
        assert stats["holographic_mode"] is True

    def test_ultimate_generator_generate_ultimate_logo(self, ultimate_generator):
        """Test de la génération d'un logo ultimate."""
        # Mock de la validation et du builder
        with patch.object(
            ultimate_generator.variants_manager, "validate_variant", return_value=True
        ):
            with patch.object(
                ultimate_generator.svg_builder, "save_ultimate_logo"
            ) as mock_save:
                mock_save.return_value = Path("test-logo.svg")

                # Test de la génération
                result = ultimate_generator.generate_ultimate_logo(
                    "serenity", 200, 0.95
                )

                # Vérifier que le résultat est un Path et contient le bon nom de fichier
                assert isinstance(result, Path)
                assert "arkalia-luna-ultimate-serenity-200.svg" in str(result)
                mock_save.assert_called_once()

    def test_ultimate_generator_generate_ultimate_logo_invalid_variant(
        self, ultimate_generator
    ):
        """Test de la gestion d'erreur pour variante invalide."""
        # Mock de la validation qui échoue
        with patch.object(
            ultimate_generator.variants_manager, "validate_variant", return_value=False
        ):
            with pytest.raises(ValueError) as exc_info:
                ultimate_generator.generate_ultimate_logo("invalid_variant", 200)

            assert "Variante 'invalid_variant' non reconnue" in str(exc_info.value)

    def test_ultimate_generator_generate_ultimate_logo_cosmic_level_validation(
        self, ultimate_generator
    ):
        """Test de la validation du niveau cosmique."""
        # Mock de la validation
        with patch.object(
            ultimate_generator.variants_manager, "validate_variant", return_value=True
        ):
            with patch.object(
                ultimate_generator.svg_builder, "save_ultimate_logo"
            ) as mock_save:
                mock_save.return_value = Path("test-logo.svg")

                # Test avec niveau cosmique extrême
                result = ultimate_generator.generate_ultimate_logo("serenity", 200, 1.5)

                # Le niveau devrait être limité à 1.0
                assert ultimate_generator.cosmic_complexity == 1.0
                # Vérifier que le résultat est un Path et contient le bon nom de fichier
                assert isinstance(result, Path)
                assert "arkalia-luna-ultimate-serenity-200.svg" in str(result)

    def test_ultimate_generator_generate_ultimate_logo_cosmic_level_minimum(
        self, ultimate_generator
    ):
        """Test avec niveau cosmique minimum."""
        # Mock de la validation
        with patch.object(
            ultimate_generator.variants_manager, "validate_variant", return_value=True
        ):
            with patch.object(
                ultimate_generator.svg_builder, "save_ultimate_logo"
            ) as mock_save:
                mock_save.return_value = Path("test-logo.svg")

                # Test avec niveau cosmique très bas
                result = ultimate_generator.generate_ultimate_logo(
                    "serenity", 200, -0.5
                )

                # Le niveau devrait être limité à 0.1
                assert ultimate_generator.cosmic_complexity == 0.1
                # Vérifier que le résultat est un Path et contient le bon nom de fichier
                assert isinstance(result, Path)
                assert "arkalia-luna-ultimate-serenity-200.svg" in str(result)

    def test_ultimate_generator_generate_all_ultimate_variants(
        self, ultimate_generator
    ):
        """Test de la génération de toutes les variantes ultimate."""
        # Mock de la liste des variantes et de la génération
        with patch.object(
            ultimate_generator.variants_manager,
            "list_variants",
            return_value=["serenity", "power"],
        ):
            with patch.object(
                ultimate_generator, "generate_ultimate_logo"
            ) as mock_generate:
                mock_generate.return_value = Path("test-logo.svg")

                # Test de la génération de toutes les variantes
                results = ultimate_generator.generate_all_ultimate_variants(200, 0.95)

                assert len(results) == 2
                assert all(result == Path("test-logo.svg") for result in results)
                assert mock_generate.call_count == 2

    def test_ultimate_generator_generate_all_ultimate_variants_with_errors(
        self, ultimate_generator
    ):
        """Test de la gestion d'erreur lors de la génération de toutes les variantes."""
        # Mock de la liste des variantes et de la génération avec erreur
        with patch.object(
            ultimate_generator.variants_manager,
            "list_variants",
            return_value=["serenity", "power"],
        ):
            with patch.object(
                ultimate_generator, "generate_ultimate_logo"
            ) as mock_generate:
                mock_generate.side_effect = [
                    Path("test1.svg"),
                    Exception("Erreur génération"),
                ]

                # Test de la gestion d'erreur
                results = ultimate_generator.generate_all_ultimate_variants(200, 0.95)

                # Seule la première variante devrait réussir
                assert len(results) == 1
                assert results[0] == Path("test1.svg")

    def test_ultimate_generator_set_cosmic_complexity_valid(self, ultimate_generator):
        """Test de la configuration de la complexité cosmique avec valeur valide."""
        # Test avec valeur valide
        ultimate_generator.set_cosmic_complexity(0.75)

        assert ultimate_generator.cosmic_complexity == 0.75
        assert ultimate_generator.ultimate_stats["cosmic_complexity"] == 0.75

    def test_ultimate_generator_set_cosmic_complexity_invalid_high(
        self, ultimate_generator
    ):
        """Test de la configuration de la complexité cosmique avec valeur trop élevée."""
        with pytest.raises(ValueError) as exc_info:
            ultimate_generator.set_cosmic_complexity(1.5)

        assert "Complexité cosmique doit être entre 0.1 et 1.0" in str(exc_info.value)

    def test_ultimate_generator_set_cosmic_complexity_invalid_low(
        self, ultimate_generator
    ):
        """Test de la configuration de la complexité cosmique avec valeur trop basse."""
        with pytest.raises(ValueError) as exc_info:
            ultimate_generator.set_cosmic_complexity(0.05)

        assert "Complexité cosmique doit être entre 0.1 et 1.0" in str(exc_info.value)

    def test_ultimate_generator_toggle_ultimate_effects(self, ultimate_generator):
        """Test de l'activation/désactivation des effets ultimate."""
        # Test désactivation
        ultimate_generator.toggle_ultimate_effects(False)
        assert ultimate_generator.ultimate_effects is False
        assert ultimate_generator.ultimate_stats["ultimate_effects"] is False

        # Test activation
        ultimate_generator.toggle_ultimate_effects(True)
        assert ultimate_generator.ultimate_effects is True
        assert ultimate_generator.ultimate_stats["ultimate_effects"] is True

    def test_ultimate_generator_toggle_holographic_mode(self, ultimate_generator):
        """Test de l'activation/désactivation du mode holographique."""
        # Test désactivation
        ultimate_generator.toggle_holographic_mode(False)
        assert ultimate_generator.holographic_mode is False
        assert ultimate_generator.ultimate_stats["holographic_mode"] is False

        # Test activation
        ultimate_generator.toggle_holographic_mode(True)
        assert ultimate_generator.holographic_mode is True
        assert ultimate_generator.ultimate_stats["holographic_mode"] is True

    def test_ultimate_generator_get_ultimate_stats(self, ultimate_generator):
        """Test de la récupération des statistiques ultimate."""
        stats = ultimate_generator.get_ultimate_stats()

        # Vérifier les statistiques de base
        assert stats["generator_type"] == "Ultimate"
        assert stats["cosmic_complexity"] == 0.98
        assert stats["ultimate_effects"] is True
        assert stats["holographic_mode"] is True

        # Vérifier les optimisations
        assert "100+ stops de gradients cosmiques" in stats["optimizations"]
        assert "Effets de turbulence cosmique" in stats["optimizations"]
        assert "Masques organiques complexes" in stats["optimizations"]
        assert "20 particules cosmiques animées" in stats["optimizations"]
        assert "Effets holographiques extrêmes" in stats["optimizations"]
        assert "Auras d'énergie cosmiques" in stats["optimizations"]

    def test_ultimate_generator_compare_with_other_versions(
        self, ultimate_generator, tmp_path
    ):
        """Test de la comparaison avec d'autres versions."""
        # Créer des répertoires temporaires pour la comparaison
        exports_dir = tmp_path / "exports"
        exports_dir.mkdir()
        (exports_dir / "arkalia-luna-serenity-200.svg").touch()

        # Mock de la comparaison
        with patch.object(
            ultimate_generator, "output_dir", tmp_path / "exports-ultimate"
        ):
            (ultimate_generator.output_dir).mkdir(exist_ok=True)
            (
                ultimate_generator.output_dir / "arkalia-luna-ultimate-serenity-200.svg"
            ).touch()

            comparison = ultimate_generator.compare_with_other_versions()

            assert "basic_svg_count" in comparison
            assert "ultimate_svg_count" in comparison
            # Vérifier que les compteurs sont des nombres positifs
            assert comparison["basic_svg_count"] >= 0
            assert comparison["ultimate_svg_count"] >= 0

    def test_ultimate_generator_compare_with_other_versions_nonexistent_dirs(
        self, ultimate_generator
    ):
        """Test de la comparaison avec des répertoires inexistants."""
        comparison = ultimate_generator.compare_with_other_versions()

        # Vérifier que la comparaison fonctionne
        assert isinstance(comparison, dict)
        assert len(comparison) > 0

        # Vérifier que les clés de comparaison existent
        expected_keys = ["basic_svg_count", "ultimate_svg_count"]
        for key in expected_keys:
            assert key in comparison

    def test_ultimate_generator_cleanup_ultimate_files(
        self, ultimate_generator, tmp_path
    ):
        """Test du nettoyage des fichiers ultimate."""
        # Créer des fichiers temporaires
        output_dir = tmp_path / "exports-ultimate"
        output_dir.mkdir(exist_ok=True)
        (output_dir / "arkalia-luna-ultimate-serenity-200.svg").touch()
        (output_dir / "favicon-serenity-32.png").touch()

        # Mock du répertoire de sortie
        with patch.object(ultimate_generator, "output_dir", output_dir):
            # Test du nettoyage
            count = ultimate_generator.cleanup_ultimate_files()

            assert count == 2
            assert ultimate_generator.ultimate_stats["total_files"] == 0
            assert ultimate_generator.ultimate_stats["ultimate_svg_logos"] == 0
            assert ultimate_generator.ultimate_stats["ultimate_png_favicons"] == 0

    def test_ultimate_generator_cleanup_ultimate_files_empty(self, ultimate_generator):
        """Test du nettoyage avec aucun fichier."""
        # Test du nettoyage sans fichiers
        count = ultimate_generator.cleanup_ultimate_files()

        assert count == 0

    def test_ultimate_generator_inheritance(self, ultimate_generator):
        """Test que le générateur ultimate hérite correctement."""
        from src.logo_generator import ArkaliaLunaLogo

        assert isinstance(ultimate_generator, ArkaliaLunaLogo)
        assert hasattr(ultimate_generator, "generate_svg_logo")
        assert hasattr(ultimate_generator, "generate_all_variants")

    def test_ultimate_generator_method_override(self, ultimate_generator):
        """Test que les méthodes sont correctement surchargées."""
        # Vérifier que les méthodes ultimate existent
        assert hasattr(ultimate_generator, "generate_ultimate_logo")
        assert hasattr(ultimate_generator, "generate_all_ultimate_variants")
        assert hasattr(ultimate_generator, "set_cosmic_complexity")
        assert hasattr(ultimate_generator, "toggle_ultimate_effects")
        assert hasattr(ultimate_generator, "toggle_holographic_mode")

    def test_ultimate_generator_logging(self, ultimate_generator):
        """Test de la configuration du logging."""
        assert ultimate_generator.logger is not None
        assert hasattr(ultimate_generator.logger, "info")
        assert hasattr(ultimate_generator.logger, "error")

    def test_ultimate_generator_error_handling(self, ultimate_generator):
        """Test de la gestion d'erreur globale."""
        # Test avec des paramètres invalides
        with pytest.raises(ValueError):
            ultimate_generator.set_cosmic_complexity(2.0)

    def test_ultimate_generator_performance_optimization(self, ultimate_generator):
        """Test des optimisations de performance."""
        import time

        # Test de performance de configuration
        start_time = time.time()
        ultimate_generator.set_cosmic_complexity(0.5)
        end_time = time.time()

        # La configuration devrait être rapide (< 0.1 seconde)
        assert (end_time - start_time) < 0.1
        assert ultimate_generator.cosmic_complexity == 0.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
