# Makefile principal pour Arkalia-LUNA Logo Generator
# Utilise les configurations du dossier config/

.PHONY: help install dev-install test test-cov format lint type-check quality-check clean build install-package quick-start generate-all generate favicon clean-exports docs

# Variables
PYTHON := python3
PIP := pip
PYTEST := pytest
BLACK := black
RUFF := ruff
MYPY := mypy
SRC_DIR := src
TESTS_DIR := tests
DOCS_DIR := docs
CONFIG_DIR := config

# Aide
help:
	@echo "🌙 Arkalia-LUNA Logo Generator - Makefile"
	@echo ""
	@echo "📋 Commandes disponibles :"
	@echo "  install          - Installation de base"
	@echo "  dev-install      - Installation avec dépendances de développement"
	@echo "  test             - Lancement des tests"
	@echo "  test-cov         - Tests avec couverture de code"
	@echo "  format           - Formatage du code avec Black"
	@echo "  lint             - Vérification du code avec Ruff"
	@echo "  type-check       - Vérification des types avec MyPy"
	@echo "  quality-check    - Vérification complète de la qualité"
	@echo "  clean            - Nettoyage des fichiers temporaires"
	@echo "  build            - Build du package"
	@echo "  install-package  - Installation du package en mode développement"
	@echo "  quick-start      - Configuration rapide complète"
	@echo "  generate-all     - Génération de tous les logos"
	@echo "  generate         - Génération d'un logo spécifique (VARIANT=serenity)"
	@echo "  favicon          - Génération de favicons (VARIANT=serenity)"
	@echo "  clean-exports    - Nettoyage des exports"
	@echo "  docs             - Génération de la documentation"
	@echo ""

# Installation
install:
	@echo "🔧 Installation de base..."
	$(PIP) install -e .

dev-install:
	@echo "🔧 Installation avec dépendances de développement..."
	$(PIP) install -e ".[dev]"

# Tests
test:
	@echo "🧪 Lancement des tests..."
	$(PYTEST) $(TESTS_DIR)/ -v --config-file $(CONFIG_DIR)/pytest.ini

test-cov:
	@echo "🧪 Tests avec couverture de code..."
	$(PYTEST) $(TESTS_DIR)/ --cov=$(SRC_DIR) --cov-report=html --cov-report=term-missing --config-file $(CONFIG_DIR)/pytest.ini

# Qualité du code
format:
	@echo "🎨 Formatage du code avec Black..."
	$(BLACK) $(SRC_DIR)/ $(TESTS_DIR)/

lint:
	@echo "🔍 Vérification du code avec Ruff..."
	$(RUFF) check $(SRC_DIR)/ $(TESTS_DIR)/

lint-fix:
	@echo "🔍 Correction automatique avec Ruff..."
	$(RUFF) check --fix $(SRC_DIR)/ $(TESTS_DIR)/

type-check:
	@echo "🔍 Vérification des types avec MyPy..."
	$(MYPY) $(SRC_DIR)/

quality-check: format lint type-check test
	@echo "✅ Vérification de la qualité terminée !"

# Nettoyage
clean:
	@echo "🧹 Nettoyage des fichiers temporaires..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	@echo "🧹 Nettoyage terminé !"

# Build et installation
build:
	@echo "🏗️ Build du package..."
	$(PYTHON) -m build

install-package: build
	@echo "📦 Installation du package..."
	$(PIP) install -e .

# Configuration rapide
quick-start: dev-install quality-check
	@echo "🚀 Configuration rapide terminée !"
	@echo "🌙 Arkalia-LUNA Logo Generator est prêt !"

# Génération de logos
generate-all:
	@echo "🎨 Génération de tous les logos..."
	$(PYTHON) -m src.cli generate-all

generate:
	@echo "🎨 Génération du logo $(VARIANT)..."
	$(PYTHON) -m src.cli generate $(VARIANT)

favicon:
	@echo "🎨 Génération du favicon $(VARIANT)..."
	$(PYTHON) -m src.cli favicon $(VARIANT)

# Nettoyage des exports
clean-exports:
	@echo "🧹 Nettoyage des exports..."
	rm -rf exports/unified/logos/*
	rm -rf exports/unified/favicons/*
	rm -f exports/*.svg
	rm -f exports/*.png
	@echo "🧹 Exports nettoyés !"

# Documentation
docs:
	@echo "📚 Génération de la documentation..."
	@echo "📖 Documentation disponible dans $(DOCS_DIR)/"

# Pre-commit hooks
pre-commit-install:
	@echo "🔧 Installation des pre-commit hooks..."
	pre-commit install --config-file $(CONFIG_DIR)/.pre-commit-config.yaml

pre-commit-run:
	@echo "🔧 Exécution des pre-commit hooks..."
	pre-commit run --config-file $(CONFIG_DIR)/.pre-commit-config.yaml --all-files

# Développement
dev-setup: dev-install pre-commit-install
	@echo "🔧 Configuration de développement terminée !"

# CI/CD
ci-setup: dev-install
	@echo "🔧 Configuration CI/CD terminée !"

# Benchmark
benchmark:
	@echo "⚡ Lancement des benchmarks..."
	$(PYTEST) $(TESTS_DIR)/ --benchmark-only --config-file $(CONFIG_DIR)/pytest.ini

# Sécurité
security-check:
	@echo "🔒 Vérification de sécurité..."
	bandit -r $(SRC_DIR)/ -f json -o bandit-report.json

# Statistiques
stats:
	@echo "📊 Statistiques du projet..."
	@echo "📁 Fichiers source: $(shell find $(SRC_DIR) -name '*.py' | wc -l)"
	@echo "🧪 Tests: $(shell find $(TESTS_DIR) -name '*.py' | wc -l)"
	@echo "📚 Documentation: $(shell find $(DOCS_DIR) -name '*.md' | wc -l)"

# Aide rapide
quick-help:
	@echo "🚀 Commandes rapides :"
	@echo "  make quick-start    # Configuration complète"
	@echo "  make generate-all   # Tous les logos"
	@echo "  make quality-check  # Vérification qualité"
	@echo "  make clean          # Nettoyage"
	@echo "  make help           # Aide complète"
