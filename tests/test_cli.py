"""Tests pour le module CLI d'Arkalia-LUNA Logo Generator"""

import pytest
from click.testing import CliRunner

from src.cli import cli, print_banner, print_error, print_info, print_success


class TestCLIFunctions:
    """Tests des fonctions utilitaires CLI"""

    def test_print_banner(self, capsys):
        """Test de l'affichage de la bannière"""
        print_banner()
        captured = capsys.readouterr()
        assert "Arkalia-LUNA" in captured.out

    def test_print_error(self, capsys):
        """Test de l'affichage d'erreur"""
        print_error("Test error")
        captured = capsys.readouterr()
        assert "Test error" in captured.out

    def test_print_success(self, capsys):
        """Test de l'affichage de succès"""
        print_success("Test success")
        captured = capsys.readouterr()
        assert "Test success" in captured.out

    def test_print_info(self, capsys):
        """Test de l'affichage d'information"""
        print_info("Test info")
        captured = capsys.readouterr()
        assert "Test info" in captured.out


class TestCLICommands:
    """Tests des commandes CLI"""

    @pytest.fixture
    def runner(self):
        """Fixture pour le runner CLI"""
        return CliRunner()

    def test_cli_help_output(self, runner):
        """Test de la sortie d'aide"""
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Commands:" in result.output

    def test_cli_with_output_dir(self, runner, tmp_path):
        """Test du CLI avec répertoire de sortie personnalisé"""
        result = runner.invoke(cli, ["--output-dir", str(tmp_path), "--help"])
        assert result.exit_code == 0

    def test_cli_verbose_mode(self, runner):
        """Test du mode verbeux"""
        result = runner.invoke(cli, ["--verbose", "--help"])
        assert result.exit_code == 0


class TestCLIErrorHandling:
    """Tests de la gestion d'erreurs CLI"""

    def test_cli_basic_functionality(self):
        """Test de base du CLI sans erreur"""
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0


class TestCLIOutput:
    """Tests de la sortie CLI"""

    def test_cli_help_output(self):
        """Test de la sortie d'aide"""
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Commands:" in result.output
