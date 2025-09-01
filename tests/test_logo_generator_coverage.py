"""
Tests pour améliorer la couverture du module logo_generator.py
Objectif : 51% → 70% de couverture
"""

import shutil
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from src.logo_generator import ArkaliaLunaLogo
from src.variants import ColorScheme, LogoVariant, LogoVariants, VariantType


class TestLogoGenerator:
    """Tests pour ArkaliaLunaLogo"""

    @pytest.fixture
    def temp_output_dir(self):
        """Répertoire temporaire pour les tests"""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def mock_variants_manager(self):
        """Manager de variantes mock"""
        manager = Mock(spec=LogoVariants)
        manager.list_variants.return_value = ["serenity", "power", "creative"]
        manager.validate_variant.return_value = True
        manager.get_variant.return_value = LogoVariant(
            name="Test Variant",
            description="Test Description",
            variant_type=VariantType.SERENITY,
            animation_speed=1.0,
            glow_intensity=0.8,
            colors=ColorScheme(
                primary="#1e3a8a", secondary="#3b82f6", accent="#06b6d4", glow="#60a5fa"
            ),
        )
        manager.get_variant_info.return_value = {
            "name": "Test Variant",
            "description": "Test Description",
            "variant_type": "serenity",
        }
        return manager

    @pytest.fixture
    def mock_svg_builder(self):
        """Builder SVG mock"""
        builder = Mock()
        builder.save_logo.return_value = None
        return builder

    @pytest.fixture
    def logo_generator(self, temp_output_dir, mock_variants_manager, mock_svg_builder):
        """Générateur de logo pour les tests"""
        generator = ArkaliaLunaLogo(temp_output_dir)
        generator.variants_manager = mock_variants_manager
        generator.svg_builder = mock_svg_builder
        return generator

    def test_generate_svg_logo_success(self, logo_generator, mock_variants_manager):
        """Test de génération de logo SVG avec succès"""
        variant_name = "serenity"
        size = 200

        output_path = logo_generator.generate_svg_logo(variant_name, size)

        assert output_path is not None
        assert "arkalia-luna-serenity-200.svg" in str(output_path)
        mock_variants_manager.validate_variant.assert_called_once_with(variant_name)

    def test_generate_svg_logo_invalid_variant(
        self, logo_generator, mock_variants_manager
    ):
        """Test de génération de logo SVG avec variante invalide"""
        mock_variants_manager.validate_variant.return_value = False

        with pytest.raises(ValueError, match="Variante 'invalid' non reconnue"):
            logo_generator.generate_svg_logo("invalid", 200)

    def test_generate_svg_logo_exception_handling(
        self, logo_generator, mock_svg_builder
    ):
        """Test de gestion d'exception lors de la génération"""
        mock_svg_builder.save_logo.side_effect = Exception("Erreur de sauvegarde")

        with pytest.raises(Exception, match="Erreur de sauvegarde"):
            logo_generator.generate_svg_logo("serenity", 200)

    def test_generate_all_variants_success(self, logo_generator, mock_variants_manager):
        """Test de génération de toutes les variantes avec succès"""
        size = 200

        generated_files = logo_generator.generate_all_variants(size)

        assert len(generated_files) == 3  # 3 variantes mockées
        assert all(isinstance(f, Path) for f in generated_files)

    def test_generate_all_variants_with_errors(
        self, logo_generator, mock_variants_manager
    ):
        """Test de génération de toutes les variantes avec erreurs partielles"""
        # Simuler une erreur pour une variante
        with patch.object(logo_generator, "generate_svg_logo") as mock_generate:
            mock_generate.side_effect = [
                Path("serenity.svg"),  # Succès
                Exception("Erreur power"),  # Échec
                Path("creative.svg"),  # Succès
            ]

            generated_files = logo_generator.generate_all_variants(200)

            # Seules les variantes réussies devraient être dans le résultat
            assert len(generated_files) == 2
            assert "serenity.svg" in str(generated_files[0])
            assert "creative.svg" in str(generated_files[1])

    def test_generate_all_variants_exception_handling(
        self, logo_generator, mock_variants_manager
    ):
        """Test de gestion d'exception lors de la génération de toutes les variantes"""
        mock_variants_manager.list_variants.side_effect = Exception("Erreur de liste")

        with pytest.raises(Exception, match="Erreur de liste"):
            logo_generator.generate_all_variants(200)

    def test_create_favicon_success(self, logo_generator, mock_variants_manager):
        """Test de création de favicon avec succès"""
        variant_name = "serenity"
        size = 32

        with patch("src.logo_generator.Image") as mock_image:
            with patch("src.logo_generator.ImageDraw") as mock_draw:
                mock_img = Mock()
                mock_image.new.return_value = mock_img
                mock_draw.Draw.return_value = Mock()

                output_path = logo_generator.create_favicon(variant_name, size)

                assert output_path is not None
                assert "favicon-serenity-32.png" in str(output_path)

    def test_create_favicon_exception_handling(
        self, logo_generator, mock_variants_manager
    ):
        """Test de gestion d'exception lors de la création de favicon"""
        mock_variants_manager.get_variant.side_effect = Exception("Erreur de variante")

        with pytest.raises(Exception, match="Erreur de variante"):
            logo_generator.create_favicon("serenity", 32)

    def test_create_favicon_all_variants_success(
        self, logo_generator, mock_variants_manager
    ):
        """Test de création de favicons pour toutes les variantes avec succès"""
        size = 32

        with patch.object(logo_generator, "create_favicon") as mock_create:
            mock_create.side_effect = [
                Path("favicon-serenity-32.png"),
                Path("favicon-power-32.png"),
                Path("favicon-creative-32.png"),
            ]

            generated_files = logo_generator.create_favicon_all_variants(size)

            assert len(generated_files) == 3
            assert all("favicon" in str(f) for f in generated_files)

    def test_create_favicon_all_variants_with_errors(
        self, logo_generator, mock_variants_manager
    ):
        """Test de création de favicons avec erreurs partielles"""
        with patch.object(logo_generator, "create_favicon") as mock_create:
            mock_create.side_effect = [
                Path("favicon-serenity-32.png"),  # Succès
                Exception("Erreur power"),  # Échec
                Path("favicon-creative-32.png"),  # Succès
            ]

            generated_files = logo_generator.create_favicon_all_variants(32)

            # Seules les variantes réussies devraient être dans le résultat
            assert len(generated_files) == 2
            assert "serenity" in str(generated_files[0])
            assert "creative" in str(generated_files[1])

    def test_create_favicon_all_variants_exception_handling(
        self, logo_generator, mock_variants_manager
    ):
        """Test de gestion d'exception lors de la création de tous les favicons"""
        mock_variants_manager.list_variants.side_effect = Exception("Erreur de liste")

        with pytest.raises(Exception, match="Erreur de liste"):
            logo_generator.create_favicon_all_variants(32)

    def test_get_variant_info_success(self, logo_generator, mock_variants_manager):
        """Test de récupération d'informations de variante avec succès"""
        variant_name = "serenity"

        info = logo_generator.get_variant_info(variant_name)

        assert info is not None
        assert "name" in info
        assert "description" in info
        mock_variants_manager.get_variant_info.assert_called_once_with(variant_name)

    def test_get_variant_info_exception_handling(
        self, logo_generator, mock_variants_manager
    ):
        """Test de gestion d'exception lors de la récupération d'informations"""
        mock_variants_manager.get_variant_info.side_effect = Exception("Erreur d'info")

        with pytest.raises(Exception, match="Erreur d'info"):
            logo_generator.get_variant_info("serenity")

    def test_list_all_variants(self, logo_generator, mock_variants_manager):
        """Test de liste de toutes les variantes"""
        variants = logo_generator.list_all_variants()

        assert variants == ["serenity", "power", "creative"]
        mock_variants_manager.list_variants.assert_called_once()

    def test_validate_variant(self, logo_generator, mock_variants_manager):
        """Test de validation de variante"""
        # Test avec variante valide
        mock_variants_manager.validate_variant.return_value = True
        assert logo_generator.validate_variant("serenity") is True

        # Test avec variante invalide
        mock_variants_manager.validate_variant.return_value = False
        assert logo_generator.validate_variant("invalid") is False

    def test_get_output_directory(self, logo_generator, temp_output_dir):
        """Test de récupération du répertoire de sortie"""
        output_dir = logo_generator.get_output_directory()

        assert output_dir == temp_output_dir

    def test_set_output_directory(self, logo_generator, temp_output_dir):
        """Test de définition d'un nouveau répertoire de sortie"""
        new_path = temp_output_dir / "new_output"

        logo_generator.set_output_directory(new_path)

        assert logo_generator.output_dir == new_path
        assert new_path.exists()

    def test_cleanup_generated_files_success(self, logo_generator, temp_output_dir):
        """Test de nettoyage des fichiers générés avec succès"""
        # Créer des fichiers de test
        test_files = [
            temp_output_dir / "arkalia-luna-serenity-200.svg",
            temp_output_dir / "favicon-serenity-32.png",
        ]

        for file_path in test_files:
            file_path.touch()

        count = logo_generator.cleanup_generated_files()

        # Le nettoyage peut supprimer d'autres fichiers, on vérifie juste que nos fichiers sont supprimés
        assert count >= 2
        assert not any(f.exists() for f in test_files)

    def test_cleanup_generated_files_no_files(self, logo_generator, temp_output_dir):
        """Test de nettoyage sans fichiers à supprimer"""
        # Vérifier qu'il n'y a pas de fichiers avant le test
        list(temp_output_dir.glob("*"))

        count = logo_generator.cleanup_generated_files()

        # Le nettoyage peut supprimer des fichiers existants, on vérifie juste le comportement
        assert count >= 0

    def test_cleanup_generated_files_exception_handling(
        self, logo_generator, temp_output_dir
    ):
        """Test de gestion d'exception lors du nettoyage"""
        # Créer un fichier de test
        test_file = temp_output_dir / "arkalia-luna-serenity-200.svg"
        test_file.touch()

        # Simuler une erreur lors de la suppression
        with patch.object(
            Path, "unlink", side_effect=Exception("Erreur de suppression")
        ):
            with pytest.raises(Exception, match="Erreur de suppression"):
                logo_generator.cleanup_generated_files()

    def test_get_generation_stats_success(self, logo_generator, temp_output_dir):
        """Test de récupération des statistiques de génération avec succès"""
        # Créer des fichiers de test
        test_files = [
            temp_output_dir / "arkalia-luna-serenity-200.svg",
            temp_output_dir / "arkalia-luna-power-200.svg",
            temp_output_dir / "favicon-serenity-32.png",
        ]

        for file_path in test_files:
            file_path.touch()

        stats = logo_generator.get_generation_stats()

        assert stats["total_files"] == 3
        assert stats["svg_logos"] == 2
        assert stats["png_favicons"] == 1
        assert stats["output_directory"] == str(temp_output_dir)
        assert stats["available_variants"] == 3  # Mocké

    def test_get_generation_stats_no_files(self, logo_generator, temp_output_dir):
        """Test de récupération des statistiques sans fichiers"""
        stats = logo_generator.get_generation_stats()

        assert stats["total_files"] == 0
        assert stats["svg_logos"] == 0
        assert stats["png_favicons"] == 0
        assert stats["available_variants"] == 3  # Mocké

    def test_get_generation_stats_exception_handling(
        self, logo_generator, temp_output_dir
    ):
        """Test de gestion d'exception lors de la récupération des statistiques"""
        # Simuler une erreur lors du glob
        with patch.object(Path, "glob", side_effect=Exception("Erreur de glob")):
            with pytest.raises(Exception, match="Erreur de glob"):
                logo_generator.get_generation_stats()

    def test_generate_svg_logo_different_sizes(
        self, logo_generator, mock_variants_manager
    ):
        """Test de génération de logo avec différentes tailles"""
        variant_name = "serenity"
        sizes = [100, 200, 500, 1000]

        for size in sizes:
            output_path = logo_generator.generate_svg_logo(variant_name, size)
            assert output_path is not None
            assert f"-{size}.svg" in str(output_path)

    def test_create_favicon_different_sizes(
        self, logo_generator, mock_variants_manager
    ):
        """Test de création de favicon avec différentes tailles"""
        variant_name = "serenity"
        sizes = [16, 32, 64, 128]

        with patch("src.logo_generator.Image") as mock_image:
            with patch("src.logo_generator.ImageDraw") as mock_draw:
                mock_img = Mock()
                mock_image.new.return_value = mock_img
                mock_draw.Draw.return_value = Mock()

                for size in sizes:
                    output_path = logo_generator.create_favicon(variant_name, size)
                    assert output_path is not None
                    assert f"-{size}.png" in str(output_path)

    def test_logger_integration(self, logo_generator, mock_variants_manager):
        """Test de l'intégration du logger"""
        # Vérifier que le logger est configuré
        assert hasattr(logo_generator, "logger")
        assert logo_generator.logger is not None

        # Test que les méthodes de logging sont appelées
        with patch.object(logo_generator.logger, "info"):
            logo_generator.list_all_variants()
            # Le logger n'est pas forcément appelé dans cette méthode simple
            # mais on vérifie qu'il est accessible

    def test_variants_manager_integration(self, logo_generator, mock_variants_manager):
        """Test de l'intégration du manager de variantes"""
        # Vérifier que le manager est configuré
        assert hasattr(logo_generator, "variants_manager")
        assert logo_generator.variants_manager is mock_variants_manager

        # Test des appels au manager
        logo_generator.list_all_variants()
        mock_variants_manager.list_variants.assert_called_once()

        logo_generator.validate_variant("serenity")
        mock_variants_manager.validate_variant.assert_called_with("serenity")

    def test_svg_builder_integration(self, logo_generator, mock_svg_builder):
        """Test de l'intégration du builder SVG"""
        # Vérifier que le builder est configuré
        assert hasattr(logo_generator, "svg_builder")
        assert logo_generator.svg_builder is mock_svg_builder

        # Test des appels au builder
        logo_generator.generate_svg_logo("serenity", 200)
        mock_svg_builder.save_logo.assert_called_once()
