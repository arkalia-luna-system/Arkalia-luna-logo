"""Tests pour le générateur BBIA
Vérification de la génération des logos BBIA (mark_only, vertical, horizontal)
"""

import shutil
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from src.bbia_branding_generator import BBIABrandingGenerator
from src.generator_factory import LogoGeneratorFactory


class TestBBIABrandingGenerator:
    """Tests pour BBIABrandingGenerator"""

    @pytest.fixture
    def temp_output_dir(self):
        """Répertoire temporaire pour les tests"""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def bbia_generator(self, temp_output_dir):
        """Générateur BBIA pour les tests"""
        return BBIABrandingGenerator(output_dir=temp_output_dir)

    def test_init(self, temp_output_dir):
        """Test de l'initialisation du générateur BBIA"""
        generator = BBIABrandingGenerator(output_dir=temp_output_dir)

        assert generator.output_dir == temp_output_dir
        assert generator.palette is not None
        assert hasattr(generator, "logger")

    def test_get_source_svg_path_valid(self, bbia_generator):
        """Test récupération chemin SVG source valide"""
        # Vérifier que les variantes sont reconnues
        for variant in ["mark_only", "vertical", "horizontal"]:
            try:
                source_path = bbia_generator._get_source_svg_path(variant)
                assert isinstance(source_path, Path)
                assert source_path.suffix == ".svg"
            except FileNotFoundError:
                # OK si les assets ne sont pas présents (test local)
                pytest.skip("Assets BBIA non disponibles")

    def test_get_source_svg_path_invalid(self, bbia_generator):
        """Test récupération chemin SVG source invalide"""
        with pytest.raises(ValueError, match="Variante.*non reconnue"):
            bbia_generator._get_source_svg_path("invalid_variant")

    def test_load_svg_content(self, bbia_generator, temp_output_dir):
        """Test chargement contenu SVG"""
        # Créer un SVG de test
        test_svg = temp_output_dir / "test.svg"
        test_svg.write_text(
            '<?xml version="1.0"?><svg><circle r="10"/></svg>', encoding="utf-8"
        )

        content = bbia_generator._load_svg_content(test_svg)

        assert isinstance(content, str)
        assert "svg" in content.lower()
        assert "circle" in content.lower()

    def test_transform_svg_size(self, bbia_generator):
        """Test transformation taille SVG"""
        svg_content = '<?xml version="1.0"?><svg width="100" height="100" viewBox="0 0 100 100"><circle r="10"/></svg>'

        transformed = bbia_generator._transform_svg_size(svg_content, 200)

        assert isinstance(transformed, str)
        assert "200" in transformed

    def test_generate_svg_logo(self, bbia_generator):
        """Test génération logo SVG"""
        try:
            output_path = bbia_generator.generate_svg_logo("mark_only", 512)

            assert output_path.exists()
            assert output_path.suffix == ".svg"
            assert "bbia-mark_only-512" in str(output_path)

            # Vérifier le contenu
            content = output_path.read_text(encoding="utf-8")
            assert "svg" in content.lower()
        except FileNotFoundError:
            pytest.skip("Assets BBIA non disponibles")

    def test_generate_png_logo_without_cairosvg(self, bbia_generator):
        """Test génération PNG sans cairosvg"""
        with patch("src.bbia_branding_generator.cairosvg", None):
            result = bbia_generator.generate_png_logo("mark_only", 512)

            assert result is None

    def test_generate_all_declinations(self, bbia_generator):
        """Test génération toutes les déclinaisons"""
        try:
            generated = bbia_generator.generate_all_declinations(
                sizes=[32, 512], formats=["svg"]
            )

            assert isinstance(generated, list)
            # Devrait générer 3 variantes × 2 tailles = 6 fichiers
            assert len(generated) == 6

            # Vérifier que tous les fichiers existent
            for file_path in generated:
                assert file_path.exists()
                assert file_path.suffix == ".svg"
        except FileNotFoundError:
            pytest.skip("Assets BBIA non disponibles")

    def test_get_bbia_stats(self, bbia_generator):
        """Test récupération statistiques BBIA"""
        stats = bbia_generator.get_bbia_stats()

        assert isinstance(stats, dict)
        assert "assets_available" in stats
        assert "assets_path" in stats
        assert "available_variants" in stats
        assert "emotion_variants" in stats
        assert "palette" in stats
        assert "status" in stats
        assert "cairosvg_available" in stats

    def test_generate_svg_logo_with_emotion(self, bbia_generator):
        """Test génération logo SVG avec variante émotionnelle"""
        try:
            output_path = bbia_generator.generate_svg_logo(
                "mark_only", 512, emotion_variant="serenity"
            )

            assert output_path.exists()
            assert output_path.suffix == ".svg"
            assert "serenity" in str(output_path)

            # Vérifier le contenu contient des effets
            content = output_path.read_text(encoding="utf-8")
            assert "svg" in content.lower()
            # Vérifier présence de filtres ou effets
            assert "filter" in content.lower() or "circle" in content.lower()
        except FileNotFoundError:
            pytest.skip("Assets BBIA non disponibles")

    def test_generate_all_emotion_variants(self, bbia_generator):
        """Test génération toutes les variantes émotionnelles"""
        try:
            generated = bbia_generator.generate_all_emotion_variants(
                "mark_only", 512, formats=["svg"]
            )

            assert isinstance(generated, list)
            # Devrait générer 10 variantes émotionnelles
            assert len(generated) == 10

            # Vérifier que tous les fichiers existent
            for file_path in generated:
                assert file_path.exists()
                assert file_path.suffix == ".svg"
                assert "mark_only" in str(file_path)
        except FileNotFoundError:
            pytest.skip("Assets BBIA non disponibles")


class TestBBIAGeneratorFactory:
    """Tests pour l'intégration BBIA dans la Factory"""

    @pytest.fixture
    def temp_output_dir(self):
        """Répertoire temporaire pour les tests"""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    def test_factory_create_bbia_generator(self, temp_output_dir):
        """Test création générateur BBIA via Factory"""
        generator = LogoGeneratorFactory.create_generator(
            generator_type="bbia", output_dir=temp_output_dir
        )

        assert isinstance(generator, BBIABrandingGenerator)
        assert generator.output_dir == temp_output_dir

    def test_factory_bbia_in_available_generators(self):
        """Test que BBIA est dans les générateurs disponibles"""
        available = LogoGeneratorFactory.get_available_generators()

        assert "bbia" in available
        assert available["bbia"]["name"] == "BBIA Branding"
        assert "BBIA" in available["bbia"]["description"]

    def test_factory_bbia_in_generator_types(self):
        """Test que BBIA est dans GENERATOR_TYPES"""
        assert "bbia" in LogoGeneratorFactory.GENERATOR_TYPES
        assert LogoGeneratorFactory.GENERATOR_TYPES["bbia"] == BBIABrandingGenerator
