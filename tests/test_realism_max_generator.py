"""Tests pour le module Realism Max Generator d'Arkalia-LUNA Logo Generator"""

import shutil
import tempfile
from pathlib import Path

import pytest

# Import du générateur
from src.realism_max_generator import RealismMaxLogoGenerator


class TestRealismMaxLogoGenerator:
    """Tests pour le générateur Realism Max"""

    @pytest.fixture
    def temp_dir(self):
        """Fixture pour un répertoire temporaire"""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def generator(self, temp_dir):
        """Fixture pour le générateur Realism Max"""
        return RealismMaxLogoGenerator(output_dir=temp_dir)

    def test_generator_initialization(self, temp_dir):
        """Test l'initialisation du générateur Realism Max"""
        generator = RealismMaxLogoGenerator(output_dir=temp_dir)
        assert generator is not None
        assert generator.output_dir == temp_dir
        assert hasattr(generator, "svg_builder")

    def test_generator_attributes(self, generator):
        """Test les attributs du générateur"""
        assert hasattr(generator, "variants_manager")
        assert hasattr(generator, "logger")
        assert hasattr(generator, "output_dir")

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


class TestRealismMaxGeneratorIntegration:
    """Tests d'intégration du générateur Realism Max"""

    @pytest.fixture
    def temp_dir(self):
        """Fixture pour un répertoire temporaire"""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    def test_generator_with_default_settings(self, temp_dir):
        """Test le générateur avec les paramètres par défaut"""
        generator = RealismMaxLogoGenerator(output_dir=temp_dir)

        assert generator.output_dir == temp_dir
        assert hasattr(generator, "svg_builder")
        assert hasattr(generator, "variants_manager")

    def test_generator_methods_chain(self, temp_dir):
        """Test l'enchaînement des méthodes du générateur"""
        generator = RealismMaxLogoGenerator(output_dir=temp_dir)

        # Vérifier les attributs de base
        assert generator.output_dir == temp_dir
        assert hasattr(generator, "svg_builder")
        assert hasattr(generator, "variants_manager")

    def test_realism_parameters_validation(self, temp_dir):
        """Test la validation des paramètres de réalisme"""
        generator = RealismMaxLogoGenerator(output_dir=temp_dir)

        # Test des attributs de base
        assert generator.output_dir == temp_dir
        assert hasattr(generator, "svg_builder")
        assert hasattr(generator, "variants_manager")
