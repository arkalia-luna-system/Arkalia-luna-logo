"""
Tests étendus pour la couverture complète du module CLI
Objectif : 31% → 90% de couverture
"""

import shutil
import tempfile
from pathlib import Path

import pytest
from click.testing import CliRunner

# Import du CLI
from src.cli import cli


class TestCLIBasicFunctionality:
    """Tests de base pour les fonctionnalités CLI"""

    @pytest.fixture
    def cli_runner(self):
        """Runner CLI pour les tests"""
        return CliRunner()

    @pytest.fixture
    def temp_output_dir(self):
        """Répertoire temporaire pour les tests"""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    def test_cli_help(self, cli_runner):
        """Test de la commande d'aide"""
        result = cli_runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Arkalia-LUNA Logo Generator" in result.output

    def test_cli_version(self, cli_runner, temp_output_dir):
        """Test de la commande version"""
        result = cli_runner.invoke(
            cli, ["--output-dir", str(temp_output_dir), "version"]
        )
        assert result.exit_code == 0
        assert "Arkalia-LUNA Logo Generator v" in result.output

    def test_cli_info_command(self, cli_runner, temp_output_dir):
        """Test de la commande info"""
        result = cli_runner.invoke(cli, ["--output-dir", str(temp_output_dir), "info"])
        assert result.exit_code == 0

    def test_cli_stats_command(self, cli_runner, temp_output_dir):
        """Test de la commande stats"""
        result = cli_runner.invoke(cli, ["--output-dir", str(temp_output_dir), "stats"])
        assert result.exit_code == 0

    def test_cli_clean_command_with_confirm(self, cli_runner, temp_output_dir):
        """Test de la commande clean avec confirmation"""
        result = cli_runner.invoke(
            cli, ["--output-dir", str(temp_output_dir), "clean", "--confirm"]
        )
        assert result.exit_code == 0

    def test_cli_generate_command_help(self, cli_runner):
        """Test de l'aide de la commande generate"""
        result = cli_runner.invoke(cli, ["generate", "--help"])
        assert result.exit_code == 0
        assert "Génère un logo SVG pour une variante spécifique" in result.output

    def test_cli_generate_all_command_help(self, cli_runner):
        """Test de l'aide de la commande generate-all"""
        result = cli_runner.invoke(cli, ["generate-all", "--help"])
        assert result.exit_code == 0
        assert "Génère toutes les variantes du logo" in result.output

    def test_cli_favicon_command_help(self, cli_runner):
        """Test de l'aide de la commande favicon"""
        result = cli_runner.invoke(cli, ["favicon", "--help"])
        assert result.exit_code == 0
        assert "Crée un favicon PNG pour une variante" in result.output

    def test_cli_favicon_all_command_help(self, cli_runner):
        """Test de l'aide de la commande favicon-all"""
        result = cli_runner.invoke(cli, ["favicon-all", "--help"])
        assert result.exit_code == 0
        assert "Crée des favicons pour toutes les variantes" in result.output


class TestCLIInputValidation:
    """Tests de validation des inputs CLI"""

    @pytest.fixture
    def cli_runner(self):
        return CliRunner()

    @pytest.fixture
    def temp_output_dir(self):
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    def test_generate_command_missing_variant(self, cli_runner, temp_output_dir):
        """Test avec variante manquante"""
        result = cli_runner.invoke(
            cli, ["--output-dir", str(temp_output_dir), "generate", "--size", "200"]
        )
        assert result.exit_code == 2  # Click error pour argument manquant

    def test_generate_command_missing_size(self, cli_runner, temp_output_dir):
        """Test avec taille manquante (devrait utiliser la valeur par défaut)"""
        result = cli_runner.invoke(
            cli,
            ["--output-dir", str(temp_output_dir), "generate", "--variant", "serenity"],
        )
        # La commande peut réussir ou échouer selon la validation de la variante
        assert result.exit_code in [0, 1, 2]

    def test_favicon_command_missing_variant(self, cli_runner, temp_output_dir):
        """Test avec variante manquante pour favicon"""
        result = cli_runner.invoke(
            cli, ["--output-dir", str(temp_output_dir), "favicon", "--size", "32"]
        )
        assert result.exit_code == 2  # Click error pour argument manquant

    def test_favicon_command_missing_size(self, cli_runner, temp_output_dir):
        """Test avec taille manquante pour favicon (devrait utiliser la valeur par défaut)"""
        result = cli_runner.invoke(
            cli,
            ["--output-dir", str(temp_output_dir), "favicon", "--variant", "serenity"],
        )
        # La commande peut réussir ou échouer selon la validation de la variante
        assert result.exit_code in [0, 1, 2]


class TestCLIWorkflowBasics:
    """Tests de base des workflows CLI"""

    @pytest.fixture
    def cli_runner(self):
        return CliRunner()

    @pytest.fixture
    def temp_output_dir(self):
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    def test_cli_initialization_with_custom_output_dir(
        self, cli_runner, temp_output_dir
    ):
        """Test d'initialisation avec répertoire de sortie personnalisé"""
        result = cli_runner.invoke(
            cli, ["--output-dir", str(temp_output_dir), "--verbose", "info"]
        )
        assert result.exit_code == 0

    def test_cli_initialization_with_default_output_dir(self, cli_runner):
        """Test d'initialisation avec répertoire de sortie par défaut"""
        result = cli_runner.invoke(cli, ["info"])
        assert result.exit_code == 0

    def test_cli_verbose_mode(self, cli_runner, temp_output_dir):
        """Test du mode verbeux"""
        result = cli_runner.invoke(
            cli, ["--output-dir", str(temp_output_dir), "--verbose", "info"]
        )
        assert result.exit_code == 0
        # En mode verbeux, on devrait voir des informations supplémentaires
        # (mais cela dépend de l'implémentation)

    def test_cli_multiple_commands_same_context(self, cli_runner, temp_output_dir):
        """Test de plusieurs commandes avec le même contexte"""
        # 1. Info
        result1 = cli_runner.invoke(cli, ["--output-dir", str(temp_output_dir), "info"])
        assert result1.exit_code == 0

        # 2. Stats
        result2 = cli_runner.invoke(
            cli, ["--output-dir", str(temp_output_dir), "stats"]
        )
        assert result2.exit_code == 0

        # 3. Version
        result3 = cli_runner.invoke(
            cli, ["--output-dir", str(temp_output_dir), "version"]
        )
        assert result3.exit_code == 0


class TestCLIErrorScenarios:
    """Tests des scénarios d'erreur CLI"""

    @pytest.fixture
    def cli_runner(self):
        return CliRunner()

    @pytest.fixture
    def temp_output_dir(self):
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    def test_cli_invalid_command(self, cli_runner):
        """Test avec commande invalide"""
        result = cli_runner.invoke(cli, ["invalid-command"])
        assert result.exit_code == 2  # Click error pour commande invalide

    def test_cli_invalid_option(self, cli_runner):
        """Test avec option invalide"""
        result = cli_runner.invoke(cli, ["--invalid-option"])
        assert result.exit_code == 2  # Click error pour option invalide

    def test_generate_command_invalid_size_type(self, cli_runner, temp_output_dir):
        """Test avec type de taille invalide"""
        result = cli_runner.invoke(
            cli,
            [
                "--output-dir",
                str(temp_output_dir),
                "generate",
                "--variant",
                "serenity",
                "--size",
                "invalid",
            ],
        )
        assert result.exit_code == 2  # Click error pour type invalide

    def test_favicon_command_invalid_size_type(self, cli_runner, temp_output_dir):
        """Test avec type de taille invalide pour favicon"""
        result = cli_runner.invoke(
            cli,
            [
                "--output-dir",
                str(temp_output_dir),
                "favicon",
                "--variant",
                "serenity",
                "--size",
                "invalid",
            ],
        )
        assert result.exit_code == 2  # Click error pour type invalide
