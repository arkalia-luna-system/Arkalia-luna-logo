"""
Tests de couverture pour améliorer la couverture de realism_max_generator.py.
Objectif : 27% → 70%+
Tests basés sur l'analyse du vrai code pour performance et précision.
"""

from pathlib import Path
from unittest.mock import patch

import pytest

from src.realism_max_generator import RealismMaxLogoGenerator


class TestRealismMaxGeneratorCoverage:
    """Tests pour améliorer la couverture de realism_max_generator.py."""

    @pytest.fixture
    def output_dir(self, tmp_path):
        """Fixture pour le répertoire de sortie temporaire."""
        return tmp_path / "exports-realism"

    @pytest.fixture
    def realism_generator(self, output_dir):
        """Fixture pour le générateur realism max."""
        return RealismMaxLogoGenerator(output_dir)

    def test_realism_generator_import(self):
        """Test que le générateur realism max peut être importé."""
        assert RealismMaxLogoGenerator is not None
        assert hasattr(RealismMaxLogoGenerator, "generate_realistic_logo")

    def test_realism_generator_initialization(self, output_dir):
        """Test de l'initialisation du générateur realism max."""
        generator = RealismMaxLogoGenerator(output_dir)

        assert generator is not None
        assert hasattr(generator, "svg_builder")
        assert hasattr(generator, "logger")
        assert generator.output_dir == output_dir

    def test_realism_generator_default_output_dir(self):
        """Test de l'initialisation avec répertoire par défaut."""
        generator = RealismMaxLogoGenerator()

        assert generator is not None
        assert generator.output_dir == Path("exports")

    def test_realism_generator_svg_builder_replacement(self, realism_generator):
        """Test que le SVG builder a été remplacé par le Realism Max."""
        assert realism_generator.svg_builder is not None
        assert hasattr(realism_generator.svg_builder, "save_logo")

    def test_realism_generator_generate_realistic_logo(self, realism_generator):
        """Test de la génération d'un logo ultra-réaliste."""
        # Mock de la validation et du builder
        with patch.object(
            realism_generator.variants_manager, "validate_variant", return_value=True
        ):
            with patch.object(realism_generator.svg_builder, "save_logo") as mock_save:
                mock_save.return_value = Path("test-logo.svg")

                # Test de la génération
                result = realism_generator.generate_realistic_logo(
                    "serenity", 200, 0.95
                )

                # Vérifier que le résultat est un Path et contient le bon nom de fichier
                assert isinstance(result, Path)
                assert "arkalia-luna-realism-serenity-200.svg" in str(result)
                mock_save.assert_called_once()

    def test_realism_generator_generate_realistic_logo_invalid_variant(
        self, realism_generator
    ):
        """Test de la gestion d'erreur pour variante invalide."""
        # Mock de la validation qui échoue
        with patch.object(
            realism_generator.variants_manager, "validate_variant", return_value=False
        ):
            with pytest.raises(ValueError) as exc_info:
                realism_generator.generate_realistic_logo("invalid_variant", 200)

            assert "Variante 'invalid_variant' non reconnue" in str(exc_info.value)

    def test_realism_generator_generate_realistic_logo_realism_level_validation(
        self, realism_generator
    ):
        """Test de la validation du niveau de réalisme."""
        # Mock de la validation
        with patch.object(
            realism_generator.variants_manager, "validate_variant", return_value=True
        ):
            with patch.object(realism_generator.svg_builder, "save_logo") as mock_save:
                mock_save.return_value = Path("test-logo.svg")

                # Test avec niveau de réalisme extrême
                result = realism_generator.generate_realistic_logo("serenity", 200, 1.5)

                # Le niveau devrait être accepté (pas de validation stricte dans le code)
                # Vérifier que le résultat est un Path et contient le bon nom de fichier
                assert isinstance(result, Path)
                assert "arkalia-luna-realism-serenity-200.svg" in str(result)

    def test_realism_generator_generate_realistic_logo_realism_level_minimum(
        self, realism_generator
    ):
        """Test avec niveau de réalisme minimum."""
        # Mock de la validation
        with patch.object(
            realism_generator.variants_manager, "validate_variant", return_value=True
        ):
            with patch.object(realism_generator.svg_builder, "save_logo") as mock_save:
                mock_save.return_value = Path("test-logo.svg")

                # Test avec niveau de réalisme très bas
                result = realism_generator.generate_realistic_logo(
                    "serenity", 200, -0.5
                )

                # Le niveau devrait être accepté (pas de validation stricte dans le code)
                # Vérifier que le résultat est un Path et contient le bon nom de fichier
                assert isinstance(result, Path)
                assert "arkalia-luna-realism-serenity-200.svg" in str(result)

    def test_realism_generator_generate_realistic_logo_output_path_format(
        self, realism_generator
    ):
        """Test du format du chemin de sortie."""
        # Mock de la validation et du builder
        with patch.object(
            realism_generator.variants_manager, "validate_variant", return_value=True
        ):
            with patch.object(realism_generator.svg_builder, "save_logo") as mock_save:
                mock_save.return_value = Path("test-logo.svg")

                # Test de la génération
                _ = realism_generator.generate_realistic_logo("serenity", 200, 0.95)

                # Vérifier que le chemin de sortie suit le format attendu
                assert "arkalia-luna-realism-serenity-200.svg" in str(
                    mock_save.call_args[0][2]
                )

    def test_realism_generator_generate_all_realistic_variants(self, realism_generator):
        """Test de la génération de toutes les variantes ultra-réalistes."""
        # Mock de la liste des variantes et de la génération
        with patch.object(
            realism_generator.variants_manager,
            "list_variants",
            return_value=["serenity", "power"],
        ):
            with patch.object(
                realism_generator, "generate_realistic_logo"
            ) as mock_generate:
                mock_generate.return_value = Path("test-logo.svg")

                # Test de la génération de toutes les variantes
                results = realism_generator.generate_all_realistic_variants(200, 0.95)

                assert len(results) == 2
                assert all(result == Path("test-logo.svg") for result in results)
                assert mock_generate.call_count == 2

    def test_realism_generator_generate_all_realistic_variants_with_errors(
        self, realism_generator
    ):
        """Test de la gestion d'erreur lors de la génération de toutes les variantes."""
        # Mock de la liste des variantes et de la génération avec erreur
        with patch.object(
            realism_generator.variants_manager,
            "list_variants",
            return_value=["serenity", "power"],
        ):
            with patch.object(
                realism_generator, "generate_realistic_logo"
            ) as mock_generate:
                mock_generate.side_effect = [
                    Path("test1.svg"),
                    Exception("Erreur génération"),
                ]

                # Test de la gestion d'erreur
                results = realism_generator.generate_all_realistic_variants(200, 0.95)

                # Seule la première variante devrait réussir
                assert len(results) == 1
                assert results[0] == Path("test1.svg")

    def test_realism_generator_generate_all_realistic_variants_empty_list(
        self, realism_generator
    ):
        """Test de la génération avec liste de variantes vide."""
        # Mock de la liste des variantes vide
        with patch.object(
            realism_generator.variants_manager, "list_variants", return_value=[]
        ):
            # Test de la génération sans variantes
            results = realism_generator.generate_all_realistic_variants(200, 0.95)

            assert len(results) == 0

    def test_realism_generator_create_realistic_favicon(self, realism_generator):
        """Test de la création d'un favicon ultra-réaliste."""
        # Mock de la méthode parent de la classe parent
        with patch.object(
            realism_generator.__class__.__bases__[0], "create_favicon"
        ) as mock_parent:
            mock_parent.return_value = Path("favicon.png")

            # Test de la création du favicon
            result = realism_generator.create_realistic_favicon("serenity", 32, 0.95)

            # Vérifier que le résultat est un Path et correspond au mock
            assert isinstance(result, Path)
            assert result == Path("favicon.png")
            # La méthode parent est appelée
            mock_parent.assert_called_once_with("serenity", 32)

    def test_realism_generator_create_realistic_favicon_invalid_variant(
        self, realism_generator
    ):
        """Test de la gestion d'erreur pour favicon avec variante invalide."""
        # Mock de la méthode parent qui lève une exception
        with patch.object(
            realism_generator,
            "create_favicon",
            side_effect=ValueError("Variante invalide"),
        ):
            with pytest.raises(ValueError) as exc_info:
                realism_generator.create_realistic_favicon("invalid_variant", 32)

            # Vérifier que l'erreur contient le bon message
            error_msg = str(exc_info.value)
            assert "Variante 'invalid_variant' non reconnue" in error_msg

    def test_realism_generator_create_realistic_favicon_different_sizes(
        self, realism_generator
    ):
        """Test de la création de favicons avec différentes tailles."""
        # Mock de la méthode parent de la classe parent
        with patch.object(
            realism_generator.__class__.__bases__[0], "create_favicon"
        ) as mock_parent:
            mock_parent.return_value = Path("favicon.png")

            # Test avec différentes tailles
            sizes = [16, 32, 64, 128]
            for size in sizes:
                result = realism_generator.create_realistic_favicon(
                    "serenity", size, 0.95
                )
                # Vérifier que le résultat est un Path et correspond au mock
                assert isinstance(result, Path)
                assert result == Path("favicon.png")
                # La méthode parent est appelée avec la bonne taille
                mock_parent.assert_called_with("serenity", size)

    def test_realism_generator_create_realistic_favicon_different_realism_levels(
        self, realism_generator
    ):
        """Test de la création de favicons avec différents niveaux de réalisme."""
        # Mock de la méthode parent de la classe parent
        with patch.object(
            realism_generator.__class__.__bases__[0], "create_favicon"
        ) as mock_parent:
            mock_parent.return_value = Path("favicon.png")

            # Test avec différents niveaux de réalisme
            levels = [0.1, 0.5, 0.95, 1.0]
            for level in levels:
                result = realism_generator.create_realistic_favicon(
                    "serenity", 32, level
                )
                # Vérifier que le résultat est un Path et correspond au mock
                assert isinstance(result, Path)
                assert result == Path("favicon.png")

    def test_realism_generator_inheritance(self, realism_generator):
        """Test que le générateur realism max hérite correctement."""
        from src.logo_generator import ArkaliaLunaLogo

        assert isinstance(realism_generator, ArkaliaLunaLogo)
        assert hasattr(realism_generator, "generate_svg_logo")
        assert hasattr(realism_generator, "generate_all_variants")

    def test_realism_generator_method_override(self, realism_generator):
        """Test que les méthodes sont correctement surchargées."""
        # Vérifier que les méthodes realism existent
        assert hasattr(realism_generator, "generate_realistic_logo")
        assert hasattr(realism_generator, "generate_all_realistic_variants")
        assert hasattr(realism_generator, "create_realistic_favicon")

    def test_realism_generator_logging(self, realism_generator):
        """Test de la configuration du logging."""
        assert realism_generator.logger is not None
        assert hasattr(realism_generator.logger, "info")
        assert hasattr(realism_generator.logger, "error")

    def test_realism_generator_error_handling(self, realism_generator):
        """Test de la gestion d'erreur globale."""
        # Test avec des paramètres invalides
        with pytest.raises(ValueError):
            realism_generator.generate_realistic_logo("invalid_variant", 200)

    def test_realism_generator_performance_optimization(self, realism_generator):
        """Test des optimisations de performance."""
        import time

        # Mock de la validation et du builder
        with patch.object(
            realism_generator.variants_manager, "validate_variant", return_value=True
        ):
            with patch.object(realism_generator.svg_builder, "save_logo") as mock_save:
                mock_save.return_value = Path("test-logo.svg")

                # Test de performance de génération
                start_time = time.time()
                result = realism_generator.generate_realistic_logo(
                    "serenity", 200, 0.95
                )
                end_time = time.time()

                # La génération devrait être rapide (< 1 seconde)
                assert (end_time - start_time) < 1.0
                # Vérifier que le résultat est un Path et contient le bon nom de fichier
                assert isinstance(result, Path)
                assert "arkalia-luna-realism-serenity-200.svg" in str(result)

    def test_realism_generator_output_directory_creation(
        self, realism_generator, tmp_path
    ):
        """Test de la création automatique du répertoire de sortie."""
        # Créer un nouveau répertoire
        new_output_dir = tmp_path / "new-exports-realism"

        # Mock du répertoire de sortie
        with patch.object(realism_generator, "output_dir", new_output_dir):
            # Mock de la validation et du builder
            with patch.object(
                realism_generator.variants_manager,
                "validate_variant",
                return_value=True,
            ):
                with patch.object(
                    realism_generator.svg_builder, "save_logo"
                ) as mock_save:
                    mock_save.return_value = Path("test-logo.svg")

                    # Test de la génération
                    result = realism_generator.generate_realistic_logo(
                        "serenity", 200, 0.95
                    )

                    # Vérifier que le résultat est un Path et contient le bon nom de fichier
                    assert isinstance(result, Path)
                    assert "arkalia-luna-realism-serenity-200.svg" in str(result)

    def test_realism_generator_variant_validation_integration(self, realism_generator):
        """Test de l'intégration avec la validation des variantes."""
        # Mock de la validation qui échoue
        with patch.object(
            realism_generator.variants_manager, "validate_variant", return_value=False
        ):
            with pytest.raises(ValueError) as exc_info:
                realism_generator.generate_realistic_logo("invalid_variant", 200)

            assert "Variante 'invalid_variant' non reconnue" in str(exc_info.value)

    def test_realism_generator_svg_builder_integration(self, realism_generator):
        """Test de l'intégration avec le SVG builder."""
        # Mock de la validation
        with patch.object(
            realism_generator.variants_manager, "validate_variant", return_value=True
        ):
            with patch.object(realism_generator.svg_builder, "save_logo") as mock_save:
                mock_save.return_value = Path("test-logo.svg")

                # Test de la génération
                _ = realism_generator.generate_realistic_logo("serenity", 200, 0.95)

                # Vérifier que le builder a été appelé avec les bons paramètres
                mock_save.assert_called_once()
                call_args = mock_save.call_args[0]
                assert call_args[0] == "serenity"  # variant_name
                assert call_args[1] == 200  # size
                assert "arkalia-luna-realism-serenity-200.svg" in str(
                    call_args[2]
                )  # output_path

    def test_realism_generator_error_logging(self, realism_generator):
        """Test du logging des erreurs."""
        # Mock de la validation qui échoue
        with patch.object(
            realism_generator.variants_manager, "validate_variant", return_value=False
        ):
            with patch.object(realism_generator.logger, "error") as mock_error:
                with pytest.raises(ValueError):
                    realism_generator.generate_realistic_logo("invalid_variant", 200)

                # Vérifier que l'erreur a été loggée
                mock_error.assert_called_once()

    def test_realism_generator_success_logging(self, realism_generator):
        """Test du logging des succès."""
        # Mock de la validation et du builder
        with patch.object(
            realism_generator.variants_manager, "validate_variant", return_value=True
        ):
            with patch.object(realism_generator.svg_builder, "save_logo") as mock_save:
                mock_save.return_value = Path("test-logo.svg")

                with patch.object(realism_generator.logger, "info") as mock_info:
                    # Test de la génération
                    _ = realism_generator.generate_realistic_logo("serenity", 200, 0.95)

                    # Vérifier que le succès a été loggé
                    assert mock_info.call_count >= 1

    def test_realism_generator_file_extension_consistency(self, realism_generator):
        """Test de la cohérence des extensions de fichiers."""
        # Mock de la validation et du builder
        with patch.object(
            realism_generator.variants_manager, "validate_variant", return_value=True
        ):
            with patch.object(realism_generator.svg_builder, "save_logo") as mock_save:
                mock_save.return_value = Path("test-logo.svg")

                # Test de la génération
                result = realism_generator.generate_realistic_logo(
                    "serenity", 200, 0.95
                )

                # Vérifier que l'extension est .svg
                assert result.suffix == ".svg"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
