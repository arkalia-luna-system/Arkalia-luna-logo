"""Tests pour le module Ultimate Generator d'Arkalia-LUNA Logo Generator"""

import shutil
import tempfile
from pathlib import Path

import pytest

# Import du générateur
from src.ultimate_generator import UltimateLogoGenerator


class TestUltimateLogoGenerator:
    """Tests pour le générateur Ultimate"""

    @pytest.fixture
    def temp_dir(self):
        """Fixture pour un répertoire temporaire"""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def generator(self, temp_dir):
        """Fixture pour le générateur Ultimate"""
        return UltimateLogoGenerator(output_dir=temp_dir)

    def test_generator_initialization(self, temp_dir):
        """Test l'initialisation du générateur Ultimate"""
        generator = UltimateLogoGenerator(output_dir=temp_dir)
        assert generator is not None
        assert generator.output_dir == temp_dir
        assert hasattr(generator, "svg_builder")

    def test_generator_attributes(self, generator):
        """Test les attributs du générateur"""
        assert hasattr(generator, "cosmic_complexity")
        assert hasattr(generator, "ultimate_effects")
        assert hasattr(generator, "holographic_mode")
        assert hasattr(generator, "variants_manager")

    def test_cosmic_complexity_default(self, generator):
        """Test la complexité cosmique par défaut"""
        assert generator.cosmic_complexity == 0.98

    def test_ultimate_effects_default(self, generator):
        """Test les effets ultimes par défaut"""
        assert generator.ultimate_effects is True

    def test_holographic_mode_default(self, generator):
        """Test le mode holographique par défaut"""
        assert generator.holographic_mode is True

    def test_get_ultimate_stats(self, generator):
        """Test la récupération des statistiques Ultimate"""
        stats = generator.get_ultimate_stats()
        assert isinstance(stats, dict)
        assert "cosmic_complexity" in stats
        assert "ultimate_effects" in stats
        assert "holographic_mode" in stats

    def test_list_all_variants(self, generator):
        """Test la liste des variantes disponibles"""
        variants = generator.list_all_variants()
        assert isinstance(variants, list)
        assert len(variants) > 0

    def test_validate_variant(self, generator):
        """Test la validation des variantes"""
        # Test avec une variante valide
        valid_variant = generator.list_all_variants()[0]
        assert generator.validate_variant(valid_variant) is True

        # Test avec une variante invalide
        assert generator.validate_variant("invalid_variant") is False

    def test_get_variant_info(self, generator):
        """Test la récupération d'informations sur une variante"""
        valid_variant = generator.list_all_variants()[0]
        info = generator.get_variant_info(valid_variant)
        assert isinstance(info, dict)
        assert "name" in info
        assert "description" in info

    def test_cleanup_generated_files(self, generator):
        """Test le nettoyage des fichiers générés"""
        # Créer un fichier temporaire avec le bon pattern
        temp_file = generator.output_dir / "arkalia-luna-test-200.svg"
        temp_file.write_text("test")

        # Nettoyer
        count = generator.cleanup_generated_files()

        # Vérifier que le fichier a été supprimé et le compte est correct
        assert not temp_file.exists()
        assert count >= 1

    def test_get_output_directory(self, generator):
        """Test la récupération du répertoire de sortie"""
        output_dir = generator.get_output_directory()
        assert generator.output_dir == output_dir

    def test_set_output_directory(self, generator, temp_dir):
        """Test la modification du répertoire de sortie"""
        new_dir = temp_dir / "new_output"
        generator.set_output_directory(new_dir)
        assert generator.output_dir == new_dir


class TestUltimateGeneratorIntegration:
    """Tests d'intégration du générateur Ultimate"""

    @pytest.fixture
    def temp_dir(self):
        """Fixture pour un répertoire temporaire"""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    def test_generator_with_default_settings(self, temp_dir):
        """Test le générateur avec les paramètres par défaut"""
        generator = UltimateLogoGenerator(output_dir=temp_dir)

        assert generator.cosmic_complexity == 0.98
        assert generator.ultimate_effects is True
        assert generator.holographic_mode is True

    def test_generator_methods_chain(self, temp_dir):
        """Test l'enchaînement des méthodes du générateur"""
        generator = UltimateLogoGenerator(output_dir=temp_dir)

        # Vérifier les attributs par défaut
        assert generator.cosmic_complexity == 0.98
        assert generator.ultimate_effects is True
        assert generator.holographic_mode is True

        # Vérifier les statistiques
        stats = generator.get_ultimate_stats()
        assert stats["cosmic_complexity"] == 0.98
        assert stats["ultimate_effects"] is True
        assert stats["holographic_mode"] is True

    def test_ultimate_parameters_validation(self, temp_dir):
        """Test la validation des paramètres Ultimate"""
        generator = UltimateLogoGenerator(output_dir=temp_dir)

        # Test des valeurs par défaut
        assert generator.cosmic_complexity == 0.98
        assert generator.ultimate_effects is True
        assert generator.holographic_mode is True
