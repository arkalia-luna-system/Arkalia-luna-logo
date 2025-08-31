# 🚀 Guide de Déploiement - Arkalia-LUNA Logo Generator

## 📋 Prérequis

### 🔑 Accès GitHub
- **Repository** : Accès en écriture au repository
- **Secrets** : `GITHUB_TOKEN` configuré (automatique)
- **Actions** : GitHub Actions activées

### 🛠️ Outils Locaux
- **Git** : Version 2.30+ avec authentification configurée
- **Python** : Version 3.8+ avec pip
- **Make** : Pour utiliser les commandes du Makefile

## 🌿 Structure des Branches

### Branches Principales
```
main (production) ← develop (développement)
```

### Branches de Développement
```
develop ← feature/*, bugfix/*, hotfix/*, release/*
```

## 🔄 Workflow de Développement

### 1. **Initialisation du Repository**

```bash
# Cloner le repository
git clone https://github.com/username/arkalia-luna-logo.git
cd arkalia-luna-logo

# Vérifier la branche actuelle
git branch -a

# Si pas de branche develop, la créer
git checkout -b develop
git push -u origin develop
```

### 2. **Configuration des Branches Protégées**

**Via GitHub Web Interface :**
1. Aller dans `Settings` → `Branches`
2. Ajouter une règle pour `main` :
   - ✅ Require a pull request before merging
   - ✅ Require approvals (2 reviewers)
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging
   - ✅ Include administrators

3. Ajouter une règle pour `develop` :
   - ✅ Require a pull request before merging
   - ✅ Require approvals (1 reviewer)
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging

### 3. **Workflow Quotidien**

```bash
# Mise à jour de develop
git checkout develop
git pull origin develop

# Création d'une branche de fonctionnalité
git checkout -b feature/nouvelle-fonctionnalite

# Développement
# ... travail sur le code ...

# Tests locaux
make test
make lint
make type-check

# Commit avec convention
git add .
git commit -m "feat(logo): ajouter nouveau style mystique"

# Push de la branche
git push origin feature/nouvelle-fonctionnalite
```

### 4. **Pull Request et Review**

1. **Créer la PR** sur GitHub vers `develop`
2. **Utiliser le template** fourni
3. **Assigner des reviewers**
4. **Attendre les checks CI/CD**
5. **Review et approbation**
6. **Merge automatique** si tous les checks passent

## 🚀 Processus de Release

### 1. **Préparation de la Release**

```bash
# Depuis develop
git checkout develop
git pull origin develop

# Créer la branche de release
git checkout -b release/v2.1.0

# Mise à jour des versions
# - pyproject.toml
# - CHANGELOG.md
# - Documentation

# Tests finaux
make test
make quality-check

# Commit des changements
git add .
git commit -m "chore(release): préparer release v2.1.0"
git push origin release/v2.1.0
```

### 2. **Pull Request de Release**

1. **Créer PR** `release/v2.1.0` → `main`
2. **Review complète** par l'équipe
3. **Merge** vers `main`
4. **Tag automatique** déclenche le déploiement

### 3. **Déploiement Automatique**

**GitHub Actions déclenche :**
- ✅ Build du package
- ✅ Tests de validation
- ✅ Création de la release
- ✅ Upload des assets
- ✅ Déploiement

### 4. **Synchronisation des Branches**

```bash
# Depuis main
git checkout main
git pull origin main

# Merge vers develop
git checkout develop
git merge main
git push origin develop

# Nettoyage des branches
git branch -d release/v2.1.0
git push origin --delete release/v2.1.0
```

## 🔧 Configuration CI/CD

### Workflows GitHub Actions

#### 1. **CI (ci.yml)**
- **Déclencheur** : Push sur `main`, `develop` + PR
- **Jobs** : Quality, Tests, Build, Performance
- **Environnements** : Python 3.8-3.12

#### 2. **Deploy (deploy.yml)**
- **Déclencheur** : Tags `v*` + Workflow dispatch
- **Jobs** : Build, Release, Upload Assets

#### 3. **Branch Protection (branch-protection.yml)**
- **Déclencheur** : PR + Push sur `main`, `develop`
- **Jobs** : Validation des conventions, Auto-merge

### Configuration des Secrets

**Automatique :**
- `GITHUB_TOKEN` : Fourni par GitHub

**Optionnels (si nécessaire) :**
- `PYPI_TOKEN` : Pour publication sur PyPI
- `DOCKER_TOKEN` : Pour images Docker
- `SLACK_WEBHOOK` : Pour notifications

## 📊 Monitoring et Métriques

### Checks de Qualité
- ✅ **Tests** : 101/101 passent (100%)
- ✅ **Coverage** : 78% (+13 points)
- ✅ **Linting** : Ruff sans erreurs
- ✅ **Formatting** : Black conforme
- ✅ **Type Checking** : MyPy strict

### Performance
- ⚡ **Tests** : < 30 secondes
- ⚡ **Build** : < 2 minutes
- ⚡ **Déploiement** : < 5 minutes

## 🚨 Gestion des Erreurs

### Erreurs CI/CD
1. **Vérifier les logs** dans GitHub Actions
2. **Corriger localement** avec `make test`
3. **Push et re-test** automatique
4. **Escalade** si problème persistant

### Rollback
```bash
# En cas de problème critique
git checkout main
git revert HEAD
git push origin main

# Ou rollback vers un tag spécifique
git checkout v2.0.0
git checkout -b hotfix/rollback-v2.0.0
git push origin hotfix/rollback-v2.0.0
```

## 🔒 Sécurité

### Bonnes Pratiques
- ✅ **Branches protégées** pour `main` et `develop`
- ✅ **Reviews obligatoires** avant merge
- ✅ **Tests automatisés** avant déploiement
- ✅ **Secrets sécurisés** dans GitHub
- ✅ **Audit des dépendances** avec Bandit

### Permissions
- **Maintainers** : Merge sur `main`, `develop`
- **Contributors** : Branches de fonctionnalités
- **Bots** : Actions automatisées uniquement

## 📚 Ressources

### Documentation
- [Guide de contribution](docs/CONTRIBUTING.md)
- [Architecture](docs/ARCHITECTURE.md)
- [API Reference](docs/API.md)
- [Gestion des branches](.github/BRANCHES.md)

### Commandes Utiles
```bash
# Vérification de l'état
make test          # Tests complets
make quality-check # Qualité complète
make benchmark     # Tests de performance

# Développement
make format        # Formatage du code
make lint          # Vérification du style
make type-check    # Vérification des types

# Build et déploiement
make build         # Build du package
make clean         # Nettoyage
make install       # Installation locale
```

---

*Dernière mise à jour : 2024-12-19*
