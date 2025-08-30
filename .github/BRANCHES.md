# 🌿 Gestion des Branches - Arkalia-LUNA Logo Generator

## 📋 Structure des Branches

### 🎯 Branches Principales

#### `main` (Production)
- **Rôle** : Code stable et déployé en production
- **Protection** : Branche protégée, merge uniquement via PR
- **Déploiement** : Automatique lors des tags de version
- **Tests** : Tous les tests doivent passer
- **Code Review** : Obligatoire (2 approbations minimum)

#### `develop` (Développement)
- **Rôle** : Intégration des nouvelles fonctionnalités
- **Protection** : Branche protégée, merge uniquement via PR
- **Tests** : Tous les tests doivent passer
- **Code Review** : Obligatoire (1 approbation minimum)

### 🌱 Branches de Fonctionnalités

#### `feature/*`
- **Format** : `feature/nom-fonctionnalite`
- **Exemples** : `feature/new-logo-style`, `feature/ai-enhancement`
- **Merge** : Vers `develop` via Pull Request
- **Tests** : Tests unitaires obligatoires

#### `bugfix/*`
- **Format** : `bugfix/description-bug`
- **Exemples** : `bugfix/svg-export-error`, `bugfix/test-failure`
- **Merge** : Vers `develop` via Pull Request
- **Tests** : Tests de régression obligatoires

#### `hotfix/*`
- **Format** : `hotfix/description-urgent`
- **Exemples** : `hotfix/security-patch`, `hotfix/critical-bug`
- **Merge** : Vers `main` ET `develop` via Pull Request
- **Tests** : Tests complets obligatoires

#### `release/*`
- **Format** : `release/version-number`
- **Exemples** : `release/v2.1.0`, `release/v2.0.1`
- **Merge** : Vers `main` ET `develop` via Pull Request
- **Tests** : Tests d'intégration complets

#### `docs/*`
- **Format** : `docs/type-documentation`
- **Exemples** : `docs/api-update`, `docs/readme-fix`
- **Merge** : Vers `develop` via Pull Request
- **Tests** : Validation de la documentation

#### `refactor/*`
- **Format** : `refactor/description-refactorisation`
- **Exemples** : `refactor/svg-builder`, `refactor/test-structure`
- **Merge** : Vers `develop` via Pull Request
- **Tests** : Tests existants doivent passer

## 🔄 Workflow de Développement

### 1. **Création de Branche**
```bash
# Depuis develop
git checkout develop
git pull origin develop
git checkout -b feature/nouvelle-fonctionnalite
```

### 2. **Développement**
```bash
# Travail sur la fonctionnalité
git add .
git commit -m "feat(logo): ajouter nouveau style mystique"
git push origin feature/nouvelle-fonctionnalite
```

### 3. **Pull Request**
- Créer PR vers `develop`
- Titre formaté : `feat(logo): ajouter nouveau style mystique`
- Description détaillée avec tests et impact
- Assigner reviewers

### 4. **Code Review**
- Tests automatiques (CI/CD)
- Review du code par l'équipe
- Approbation requise pour merge

### 5. **Merge et Déploiement**
- Merge automatique si tous les checks passent
- Déploiement automatique sur `develop`
- Tests d'intégration

## 🚀 Release Process

### 1. **Préparation Release**
```bash
# Depuis develop
git checkout develop
git pull origin develop
git checkout -b release/v2.1.0
```

### 2. **Finalisation**
- Mise à jour du CHANGELOG.md
- Mise à jour des versions dans pyproject.toml
- Tests finaux

### 3. **Merge Release**
```bash
# Merge vers main
git checkout main
git merge release/v2.1.0
git tag v2.1.0
git push origin main --tags

# Merge vers develop
git checkout develop
git merge release/v2.1.0
git push origin develop
```

### 4. **Déploiement Automatique**
- GitHub Actions détecte le tag
- Build automatique du package
- Création de la release GitHub
- Upload des assets

## 📝 Conventions de Commits

### Format
```
type(scope): description courte

Description détaillée si nécessaire

BREAKING CHANGE: description des changements breaking
```

### Types
- `feat` : Nouvelle fonctionnalité
- `fix` : Correction de bug
- `docs` : Documentation
- `style` : Formatage, point-virgules manquants, etc.
- `refactor` : Refactorisation du code
- `test` : Ajout ou modification de tests
- `chore` : Tâches de maintenance
- `perf` : Amélioration des performances
- `ci` : Configuration CI/CD
- `build` : Build system ou dépendances externes
- `revert` : Revert d'un commit précédent

### Exemples
```bash
git commit -m "feat(logo): ajouter variante mystique avec effets lumineux"
git commit -m "fix(tests): corriger test_save_logo_not_implemented_perfect"
git commit -m "docs(api): mettre à jour documentation des générateurs"
git commit -m "refactor(svg): simplifier la logique de construction"
```

## 🛡️ Protection des Branches

### Règles de Protection
- **main** : Protection stricte, merge uniquement via PR
- **develop** : Protection modérée, merge via PR
- **feature/*, bugfix/*, etc.** : Pas de protection

### Checks Obligatoires
- ✅ Tests unitaires passent
- ✅ Tests d'intégration passent
- ✅ Code coverage > 80%
- ✅ Linting (Ruff) sans erreurs
- ✅ Formatage (Black) conforme
- ✅ Type checking (MyPy) sans erreurs
- ✅ Sécurité (Bandit) sans vulnérabilités critiques

## 🔧 Configuration Git

### Git Hooks (Pre-commit)
```bash
# Installation des hooks
make pre-commit-install

# Vérification avant commit
make pre-commit-run
```

### Configuration Git
```bash
# Configuration des alias utiles
git config alias.st status
git config alias.co checkout
git config alias.br branch
git config alias.ci commit
git config alias.unstage 'reset HEAD --'
git config alias.last 'log -1 HEAD'
git config alias.visual '!gitk'
```

## 📊 Monitoring et Métriques

### Qualité du Code
- **Coverage** : Maintenu > 80%
- **Complexité** : Cyclomatic complexity < 10
- **Maintenabilité** : Score A sur CodeClimate

### Performance
- **Tests** : < 30 secondes pour la suite complète
- **Build** : < 2 minutes pour le package
- **Déploiement** : < 5 minutes

---

*Dernière mise à jour : 2024-12-19*
