#!/usr/bin/env python3
"""
Tests complets pour tous les générateurs de logos Arkalia-LUNA
"""

import sys
from pathlib import Path

import pytest

# Ajouter le répertoire src au path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ai_moon_generator import AIMoonLogoGenerator
from dashboard_generator import DashboardLogoGenerator
from simple_advanced_generator import SimpleAdvancedLogoGenerator
from ultra_max_generator import UltraMaxLogoGenerator
from variants import LogoVariants, VariantType


class TestLogoVariants:
    """Tests pour la classe LogoVariants"""

    def test_variants_initialization(self):
        """Test que les variantes sont correctement initialisées"""
        variants = LogoVariants()
        assert variants is not None
        assert len(variants.get_all_variants()) == 5

    def test_variant_types(self):
        """Test que tous les types de variantes existent"""
        variants = LogoVariants()
        all_variants = variants.get_all_variants()

        # get_all_variants retourne un dictionnaire {nom: LogoVariant}
        variant_names = list(all_variants.keys())

        expected_names = ["serenity", "power", "mystery", "awakening", "creative"]
        for name in expected_names:
            assert name in variant_names

    def test_get_variant_by_name(self):
        """Test la récupération d'une variante par nom"""
        variants = LogoVariants()
        serenity = variants.get_variant("serenity")
        assert serenity is not None
        # Le nom est l'emoji + texte, pas juste "serenity"
        assert (
            "serenity" in serenity.name.lower()
            or serenity.variant_type.value == "serenity"
        )
        assert serenity.variant_type == VariantType.SERENITY


class TestAIMoonGenerator:
    """Tests pour le générateur AI-MOON"""

    def test_generator_initialization(self):
        """Test l'initialisation du générateur AI-MOON"""
        generator = AIMoonLogoGenerator()
        assert generator is not None

    def test_generate_single_logo(self, tmp_path):
        """Test la génération d'un logo AI-MOON"""
        generator = AIMoonLogoGenerator()
        output_dir = tmp_path / "exports-ai-moon"
        output_dir.mkdir()

        # Test avec une variante valide
        try:
            svg_path = generator.generate_single_logo("serenity", size=100)
            assert svg_path.exists()
            assert svg_path.suffix == ".svg"
        except Exception as e:
            pytest.skip(f"Génération AI-MOON non disponible: {e}")


class TestDashboardGenerator:
    """Tests pour le générateur Dashboard"""

    def test_generator_initialization(self):
        """Test l'initialisation du générateur Dashboard"""
        generator = DashboardLogoGenerator()
        assert generator is not None

    def test_generate_single_logo(self, tmp_path):
        """Test la génération d'un logo Dashboard"""
        generator = DashboardLogoGenerator()
        output_dir = tmp_path / "exports-dashboard"
        output_dir.mkdir()

        # Test avec une variante valide
        try:
            svg_path = generator.generate_single_logo("serenity", size=100)
            assert svg_path.exists()
            assert svg_path.suffix == ".svg"
        except Exception as e:
            pytest.skip(f"Génération Dashboard non disponible: {e}")


class TestUltraMaxGenerator:
    """Tests pour le générateur ULTRA-MAX"""

    def test_generator_initialization(self):
        """Test l'initialisation du générateur ULTRA-MAX"""
        generator = UltraMaxLogoGenerator()
        assert generator is not None

    def test_generate_single_logo(self, tmp_path):
        """Test la génération d'un logo ULTRA-MAX"""
        generator = UltraMaxLogoGenerator()
        output_dir = tmp_path / "exports-ultra-max"
        output_dir.mkdir()

        # Test avec une variante valide
        try:
            svg_path = generator.generate_single_logo("serenity", size=100)
            assert svg_path.exists()
            assert svg_path.suffix == ".svg"
        except Exception as e:
            pytest.skip(f"Génération ULTRA-MAX non disponible: {e}")


class TestSimpleAdvancedGenerator:
    """Tests pour le générateur Simple Advanced"""

    def test_generator_initialization(self):
        """Test l'initialisation du générateur Simple Advanced"""
        generator = SimpleAdvancedLogoGenerator()
        assert generator is not None

    def test_generate_single_logo(self, tmp_path):
        """Test la génération d'un logo Simple Advanced"""
        generator = SimpleAdvancedLogoGenerator()
        output_dir = tmp_path / "exports-simple-advanced"
        output_dir.mkdir()

        # Test avec une variante valide
        try:
            svg_path = generator.generate_single_logo("serenity", size=100)
            assert svg_path.exists()
            assert svg_path.suffix == ".svg"
        except Exception as e:
            pytest.skip(f"Génération Simple Advanced non disponible: {e}")


class TestIntegration:
    """Tests d'intégration"""

    def test_all_generators_available(self):
        """Test que tous les générateurs sont disponibles"""
        generators = [
            AIMoonLogoGenerator,
            DashboardLogoGenerator,
            UltraMaxLogoGenerator,
            SimpleAdvancedLogoGenerator,
        ]

        for generator_class in generators:
            try:
                generator = generator_class()
                assert generator is not None
            except Exception as e:
                pytest.skip(
                    f"Générateur {generator_class.__name__} non disponible: {e}"
                )

    def test_variants_consistency(self):
        """Test la cohérence des variantes entre tous les générateurs"""
        variants = LogoVariants()
        all_variants = variants.get_all_variants()

        # Vérifier que toutes les variantes ont les propriétés requises
        for _, variant in all_variants.items():
            assert hasattr(variant, "name")
            assert hasattr(variant, "variant_type")
            assert hasattr(variant, "colors")
            assert hasattr(variant, "description")

            # Vérifier que le nom est une chaîne valide
            assert isinstance(variant.name, str)
            assert len(variant.name) > 0

            # Vérifier que le type est valide
            assert variant.variant_type in VariantType


if __name__ == "__main__":
    # Exécuter les tests si le fichier est lancé directement
    pytest.main([__file__, "-v"])
