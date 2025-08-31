# 🌙 CI/CD Guide - Arkalia-LUNA Logo Generator

## 🎯 **Vue d'Ensemble**

Ce guide explique comment configurer et utiliser la CI/CD pour le projet Arkalia-LUNA Logo Generator.

## 🚀 **Configuration CI**

### **GitHub Actions**

Le workflow CI est configuré dans `.github/workflows/ci.yml` et inclut :

- **Tests multi-Python** (3.8, 3.9, 3.10, 3.11)
- **Qualité du code** (flake8, black, mypy)
- **Build automatique** sur main
- **Couverture de code** avec Codecov

### **Pre-commit Hooks**

Configuration dans `.pre-commit-config.yaml` :

```bash
# Installation
pip install pre-commit
pre-commit install

# Lancement manuel
pre-commit run --all-files
```

## 🧪 **Tests**

### **Structure des Tests**

```
tests/
├── __init__.py
├── test_variants.py          # Tests des variantes
├── test_svg_builders.py      # Tests des builders SVG
└── test_generators.py        # Tests des générateurs
```

### **Lancement des Tests**

```bash
# Tests basiques
make test

# Tests avec couverture
make test-cov

# Tests rapides (sans couverture)
make test-fast
```

## 🔍 **Qualité du Code**

### **Outils Utilisés**

- **Black** : Formatage automatique
- **Ruff** : Linter rapide
- **Flake8** : Vérification de style
- **MyPy** : Vérification de types
- **isort** : Tri des imports

### **Commandes**

```bash
# Formatage
make format

# Linting
make lint
make ruff

# Vérification des types
make type-check

# Tri des imports
make sort-imports
```

## 🏗️ **Build et Package**

### **Configuration setup.py**

- **Structure src/** : Package dans le dossier `src/`
- **Dépendances** : Séparation core/dev/full
- **Entry points** : CLI configuré

### **Build**

```bash
# Build du package
make build

# Installation en mode développement
make install-package
```

## 📋 **Checklist CI**

### **Avant Commit**

- [ ] Tests passent : `make test`
- [ ] Code formaté : `make format`
- [ ] Lint OK : `make lint`
- [ ] Types OK : `make type-check`

### **Avant Push**

- [ ] Pre-commit hooks passent
- [ ] Tests avec couverture OK
- [ ] Build du package OK

## 🐛 **Dépannage CI**

### **Erreurs Communes**

1. **Import Errors** : Vérifier les chemins dans `src/`
2. **Dépendances** : Vérifier `requirements.txt` et `requirements-dev.txt`
3. **Tests** : Vérifier la structure `tests/`

### **Debug Local**

```bash
# Configuration CI locale
make ci-setup

# Vérification complète
make dev-setup
make pre-commit
```

## 🔧 **Maintenance**

### **Mise à Jour des Dépendances**

```bash
# Mise à jour des requirements
pip install --upgrade -r requirements.txt
pip install --upgrade -r requirements-dev.txt

# Génération des requirements
pip freeze > requirements.txt
```

### **Ajout de Nouveaux Tests**

1. Créer le fichier de test dans `tests/`
2. Ajouter les imports conditionnels si nécessaire
3. Vérifier que les tests passent localement
4. Commiter et pousser

## 📊 **Métriques CI**

- **Couverture de code** : Objectif 64%
- **Temps de build** : <5 minutes
- **Tests** : Tous passent sur toutes les versions Python
- **Qualité** : Aucune erreur de lint/type

## 🚨 **Sécurité**

- **Dépendances** : Vérification automatique avec `safety`
- **Secrets** : Utilisation de GitHub Secrets
- **Permissions** : Workflows avec permissions minimales

---

**Note** : Cette CI est prête pour le futur. Tous les problèmes ont été anticipés et corrigés ! 🎉
