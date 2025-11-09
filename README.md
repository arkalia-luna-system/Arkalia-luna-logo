# 🎨⚡️🤖 **Arkalia-LUNA Logo Generator**

> **🌍 English**: Professional SVG/PNG logo generator with 11 unique styles, 10 emotional variants, FastAPI integration, monitoring & CI/CD - like Figma/Canva but for developers.

> **🇫🇷 Français**: Générateur professionnel de logos SVG/PNG multi-styles avec 11 styles uniques, 10 variantes émotionnelles, API FastAPI, monitoring & CI/CD inclus - comme Figma/Canva mais pour développeurs.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/arkalia-luna-system/arkalia-luna-logo?include_prereleases)](https://github.com/arkalia-luna-system/arkalia-luna-logo/releases)
[![Version](https://img.shields.io/badge/Version-2.0.0-orange.svg)](CHANGELOG.md)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/lint-ruff-red.svg)](https://github.com/astral-sh/ruff)
[![Tests](https://img.shields.io/badge/tests-297%20passed-brightgreen.svg)](tests/)
[![Coverage](https://img.shields.io/badge/coverage-75%25-yellow.svg)](htmlcov/)
[![Docker](https://img.shields.io/badge/docker-5%20services%20ready-blue.svg)](Dockerfile.prod)
[![API](https://img.shields.io/badge/API-0.03s%20response-green.svg)](main.py)
[![Monitoring](https://img.shields.io/badge/monitoring-Prometheus%20%2B%20Grafana-orange.svg)](monitoring/)
[![Metrics](https://img.shields.io/badge/metrics-histogram%20%2B%20labels-blue.svg)](http://localhost:8000/metrics)

[![Open to contributions](https://img.shields.io/badge/Open%20to-contributions-brightgreen.svg)](CONTRIBUTING.md)
[![Good first issue](https://img.shields.io/badge/Good%20first-issue-blue.svg)](https://github.com/arkalia-luna-system/arkalia-luna-logo/labels/good%20first%20issue)
[![Help wanted](https://img.shields.io/badge/Help-wanted-orange.svg)](https://github.com/arkalia-luna-system/arkalia-luna-logo/labels/help%20wanted)

## 📋 **Table of Contents**

- [🎯 Vue d'ensemble](#-vue-densemble)
- [🎯 Cas d'Usage](#-cas-dusage---dans-quel-projet-utiliser-ce-générateur-)
- [✨ Démonstration Live](#-démonstration-live)
- [🚀 Installation](#-installation)
- [💻 Utilisation](#-utilisation)
- [🎨 Styles Disponibles](#-styles-disponibles)
- [🔧 Configuration](#-configuration)
- [📊 Monitoring](#-monitoring)
- [🤝 Contribution](#-contribution)
- [📚 Documentation](#-documentation)
- [🛠️ Dépannage](#️-dépannage)
- [📄 Licence](#-licence)

---

## 🎯 **Vue d'ensemble**

> **🌍 English**: Arkalia-LUNA Logo Generator is a complete SVG vector logo generation system with **11 unique styles** and **10 emotional variants**. Professional modular architecture perfect for showcase projects, demonstrating advanced Python skills, design patterns, and graphics generation.

Arkalia-LUNA Logo Generator est un système complet de génération de logos vectoriels SVG avec **11 styles uniques** et **10 variantes émotionnelles** distinctes. L'architecture modulaire et professionnelle en fait un excellent projet vitrine pour GitHub, démontrant des compétences en Python avancé, design patterns, et génération de contenu graphique.

## 🎯 **Cas d'Usage - Dans Quel Projet Utiliser Ce Générateur ?**

| Type de Projet | Usage Recommandé | Bénéfice | Intégration |
|----------------|------------------|----------|-------------|
| **🌐 Applications Web** | Logos dynamiques selon le thème | Cohérence visuelle | API REST + Frontend |
| **📱 Apps Mobiles** | Favicons et icônes adaptatives | Multi-résolution automatique | CLI dans CI/CD |
| **📊 Dashboards Business** | Branding personnalisé | Identité professionnelle | Docker + monitoring |
| **🎮 Plateformes Gaming** | Logos émotionnels immersifs | Engagement utilisateur | API temps réel |
| **🤖 Projets IA/ML** | Visualisation d'émotions | Interface intuitive | Python natif |
| **🏢 Solutions Entreprise** | Multi-tenant branding | Personnalisation client | API scalable |
| **📚 Projets Open Source** | Branding cohérent | Identité communautaire | GitHub Actions |
| **🎨 Outils Créatifs** | Assets vectoriels de qualité | Export professionnel | CLI + batch processing |

## 🎬 **Démonstration en Temps Réel**

![Arkalia-LUNA Logo Generator Demo](exports/demo-gif/arkalia-luna-demo.gif)

*Génération de logos en 0.03 secondes - 10 variantes émotionnelles*

## 🎨 **Comparaison des 11 Styles de Logos**

### **🌟 Variante Sérénité** (Halo doux, pulsations lentes)
| Style | Logo | Description |
|-------|------|-------------|
| **🌙 Simple** | ![Simple Serenity](exports/screenshots/simple-serenity-200.svg) | Logo de base Arkalia-LUNA |
| **📊 Dashboard** | ![Dashboard Serenity](exports/screenshots/dashboard-serenity-200.svg) | Interface optimisée et épurée |
| **🌙 AI-Moon** | ![AI-Moon Serenity](exports/screenshots/ai_moon-serenity-200.svg) | IA réaliste avec lune vivante |
| **🎨 Advanced** | ![Advanced Serenity](exports/screenshots/advanced-serenity-200.svg) | Techno-mystique avancé |
| **⚡ Simple-Advanced** | ![Simple-Advanced Serenity](exports/screenshots/simple_advanced-serenity-200.svg) | Équilibré et configurable |
| **🚀 Ultra-Max** | ![Ultra-Max Serenity](exports/screenshots/ultra_max-serenity-200.svg) | Effets exceptionnels et performance |
| **🌍 Realism Max** | ![Realism Max Serenity](exports/screenshots/realism_max-serenity-200.svg) | Ultra-réaliste avec effets organiques |
| **🌟 Ultimate** | ![Ultimate Serenity](exports/screenshots/ultimate-serenity-200.svg) | Cosmique extrême (100+ stops, holographie) |

### **⚡ Variante Puissance** (Halo vibrant, réseau accéléré)
| Style | Logo | Description |
|-------|------|-------------|
| **🌙 Simple** | ![Simple Power](exports/screenshots/simple-power-200.svg) | Logo de base Arkalia-LUNA |
| **📊 Dashboard** | ![Dashboard Power](exports/screenshots/dashboard-power-200.svg) | Interface optimisée et épurée |
| **🌙 AI-Moon** | ![AI-Moon Power](exports/screenshots/ai_moon-power-200.svg) | IA réaliste avec lune vivante |
| **🎨 Advanced** | ![Advanced Power](exports/screenshots/advanced-power-200.svg) | Techno-mystique avancé |
| **⚡ Simple-Advanced** | ![Simple-Advanced Power](exports/screenshots/simple_advanced-power-200.svg) | Équilibré et configurable |
| **🚀 Ultra-Max** | ![Ultra-Max Power](exports/screenshots/ultra_max-power-200.svg) | Effets exceptionnels et performance |
| **🌍 Realism Max** | ![Realism Max Power](exports/screenshots/realism_max-power-200.svg) | Ultra-réaliste avec effets organiques |
| **🌟 Ultimate** | ![Ultimate Power](exports/screenshots/ultimate-power-200.svg) | Cosmique extrême (100+ stops, holographie) |

### **🔮 Variante Mystère** (Brumes mouvantes, réseau irrégulier)
| Style | Logo | Description |
|-------|------|-------------|
| **🌙 Simple** | ![Simple Mystery](exports/screenshots/simple-mystery-200.svg) | Logo de base Arkalia-LUNA |
| **📊 Dashboard** | ![Dashboard Mystery](exports/screenshots/dashboard-mystery-200.svg) | Interface optimisée et épurée |
| **🌙 AI-Moon** | ![AI-Moon Mystery](exports/screenshots/ai_moon-mystery-200.svg) | IA réaliste avec lune vivante |
| **🎨 Advanced** | ![Advanced Mystery](exports/screenshots/advanced-mystery-200.svg) | Techno-mystique avancé |
| **⚡ Simple-Advanced** | ![Simple-Advanced Mystery](exports/screenshots/simple_advanced-mystery-200.svg) | Équilibré et configurable |
| **🚀 Ultra-Max** | ![Ultra-Max Mystery](exports/screenshots/ultra_max-mystery-200.svg) | Effets exceptionnels et performance |
| **🌍 Realism Max** | ![Realism Max Mystery](exports/screenshots/realism_max-mystery-200.svg) | Ultra-réaliste avec effets organiques |
| **🌟 Ultimate** | ![Ultimate Mystery](exports/screenshots/ultimate-mystery-200.svg) | Cosmique extrême (100+ stops, holographie) |

### **✨ Variante Éveil/Sagesse** (Halo rayonnant, Λ-core clair)
| Style | Logo | Description |
|-------|------|-------------|
| **🌙 Simple** | ![Simple Awakening](exports/screenshots/simple-awakening-200.svg) | Logo de base Arkalia-LUNA |
| **📊 Dashboard** | ![Dashboard Awakening](exports/screenshots/dashboard-awakening-200.svg) | Interface optimisée et épurée |
| **🌙 AI-Moon** | ![AI-Moon Awakening](exports/screenshots/ai_moon-awakening-200.svg) | IA réaliste avec lune vivante |
| **🎨 Advanced** | ![Advanced Awakening](exports/screenshots/advanced-awakening-200.svg) | Techno-mystique avancé |
| **⚡ Simple-Advanced** | ![Simple-Advanced Awakening](exports/screenshots/simple_advanced-awakening-200.svg) | Équilibré et configurable |
| **🚀 Ultra-Max** | ![Ultra-Max Awakening](exports/screenshots/ultra_max-awakening-200.svg) | Effets exceptionnels et performance |
| **🌍 Realism Max** | ![Realism Max Awakening](exports/screenshots/realism_max-awakening-200.svg) | Ultra-réaliste avec effets organiques |
| **🌟 Ultimate** | ![Ultimate Awakening](exports/screenshots/ultimate-awakening-200.svg) | Cosmique extrême (100+ stops, holographie) |

### **🎇 Variante Énergie Créative** (Flux rapides, reflets multicolores)
| Style | Logo | Description |
|-------|------|-------------|
| **🌙 Simple** | ![Simple Creative](exports/screenshots/simple-creative-200.svg) | Logo de base Arkalia-LUNA |
| **📊 Dashboard** | ![Dashboard Creative](exports/screenshots/dashboard-creative-200.svg) | Interface optimisée et épurée |
| **🌙 AI-Moon** | ![AI-Moon Creative](exports/screenshots/ai_moon-creative-200.svg) | IA réaliste avec lune vivante |
| **🎨 Advanced** | ![Advanced Creative](exports/screenshots/advanced-creative-200.svg) | Techno-mystique avancé |
| **⚡ Simple-Advanced** | ![Simple-Advanced Creative](exports/screenshots/simple_advanced-creative-200.svg) | Équilibré et configurable |
| **🚀 Ultra-Max** | ![Ultra-Max Creative](exports/screenshots/ultra_max-creative-200.svg) | Effets exceptionnels et performance |
| **🌍 Realism Max** | ![Realism Max Creative](exports/screenshots/realism_max-creative-200.svg) | Ultra-réaliste avec effets organiques |
| **🌟 Ultimate** | ![Ultimate Creative](exports/screenshots/ultimate-creative-200.svg) | Cosmique extrême (100+ stops, holographie) |

## ✨ **Fonctionnalités**

### 🎨 **11 Styles de Logos Uniques**
- **🌙 Base (default)** : Logo standard Arkalia-LUNA
- **📊 Dashboard** : Interface optimisée et épurée
- **🌙 AI-Moon** : IA réaliste avec lune vivante
- **🎨 Advanced** : Techno-mystique avancé
- **⚡ Simple-Advanced** : Équilibré et configurable
- **🚀 Ultra-Max** : Effets exceptionnels et performance
- **🌍 Realism Max** : Ultra-réaliste avec effets organiques
- **🌟 Ultimate** : Cosmique extrême (100+ stops, holographie)
- **🤖 AI** : Génération IA avec Stable Diffusion
- **🌌 Cosmic** : Sphères cosmiques et réseaux neuronaux
- **🧠 Hyper-AI** : Intelligence artificielle avancée avec ComfyUI + SDXL + ControlNet

### 🌟 **10 Variantes Émotionnelles**
- **🌙 Sérénité** : Halo doux, pulsations lentes, ambiance calme et mystique
- **⚡ Puissance** : Halo vibrant, réseau accéléré, énergie intense  
- **🔮 Mystère** : Brumes mouvantes, réseau irrégulier, ambiance mystérieuse
- **✨ Éveil/Sagesse** : Halo rayonnant, Λ-core clair, sagesse éclairée
- **🎇 Énergie créative** : Flux rapides, reflets multicolores, créativité débordante
- **🌧️ Pluie/Gris** : Gouttes de pluie, nuages gris, ambiance mélancolique mais élégante
- **⚡ Orage/Colère** : Éclairs zigzagants, nuages sombres, énergie explosive et dynamique
- **💥 Vive/Explosion** : Particules explosives, feux d'artifice, mouvement radial et énergique
- **☀️ Ensoleillé** : Rayons de soleil, chaleur et luminosité, optimisme et énergie positive
- **❄️ Neige** : Flocons qui tombent, froid et pureté, sérénité cristalline

### 🛠️ **Capacités Techniques**
- **Génération SVG** haute qualité avec gradients et filtres
- **Favicons PNG** personnalisables (16x16 à 512x512)
- **Interface CLI** complète avec Click et Rich
- **Architecture modulaire** avec séparation des responsabilités
- **Factory Pattern** pour création dynamique de générateurs
- **Système de logging** professionnel
- **Gestion d'erreurs** robuste avec fallbacks
- **Tests automatisés** inclus avec couverture complète

## 🌐 **API Web & Déploiement**

### **🚀 API FastAPI Production-Ready**
- **API REST** complète avec FastAPI
- **Endpoints** : `/health`, `/generate`, `/download`, `/stats`, `/metrics`
- **Performance** : Génération de logo en 0.03 secondes
- **Documentation** : Swagger UI automatique (`/docs`)
- **Sécurité** : CORS, validation, gestion d'erreurs
- **Monitoring** : Métriques Prometheus enrichies (compteurs par route/labels, histogramme de durées)

### **🐳 Docker & Orchestration**
- **Dockerfile.prod** optimisé pour la production
- **Docker Compose** avec 5 services (app, redis, nginx, prometheus, grafana)
- **Monitoring** : Prometheus + Grafana intégrés (panels p95/p99, erreurs/min, statut par route)
- **Sécurité** : Utilisateur non-root, health checks
- **Scalabilité** : Prêt pour déploiement en production

### **📊 Infrastructure Complète - VALIDÉE** ✅
```bash
# Démarrage rapide avec Docker
docker-compose -f docker-compose.prod.yml up -d

# Services opérationnels :
# 🌐 API : http://localhost:8000 (FastAPI + Swagger)
# 🔄 Nginx : http://localhost:80 (Reverse Proxy)
# 📊 Prometheus : http://localhost:9090 (Métriques)
# 📈 Grafana : http://localhost:3000 (Monitoring)
# 💾 Redis : localhost:6379 (Cache)
```

### **⚡ Performance Exceptionnelle**
- **Génération de logo** : 0.03 secondes
- **5 logos en 0.1 seconde** (voir GIF ci-dessus)
- **API response** : < 100ms
- **Infrastructure** : 5 services Docker opérationnels
- **Monitoring** : métriques Prometheus en temps réel (quantiles via histogrammes)

### **🔬 Tests de charge (CI)**
- **Workflow GitHub Actions**: exécute Artillery à la demande avec `target_url`
- **SLA**: p95 < 2s, p99 < 5s, erreurs < 5%
- **Artefacts**: rapport JSON attaché à l’exécution CI

## 🚀 **Installation Rapide**

### **1. Configuration automatique (recommandée)**
```bash
git clone <repository-url>
cd arkalia-luna-logo
make quick-start
```

### **2. Configuration manuelle**
```bash
# Créer l'environnement virtuel
python3 -m venv arkalia-luna-env

# L'activer
source arkalia-luna-env/bin/activate  # Linux/Mac
# ou
arkalia-luna-env\Scripts\activate     # Windows

# Installer les dépendances
pip install -e .
```

## 📖 **Utilisation**

### **Interface CLI Principale**
```bash
# Activer l'environnement virtuel
source arkalia-luna-env/bin/activate

# Voir toutes les variantes
python -m src.cli info

# Voir tous les générateurs disponibles
python -m src.cli generators

# Générer un logo spécifique
python -m src.cli generate -v serenity -s 200 -g ultimate

# Générer toutes les variantes
python -m src.cli generate-all -s 200

# Créer des favicons
python -m src.cli favicon-all -s 32

# Voir les statistiques
python -m src.cli stats

# Nettoyer les fichiers
python -m src.cli clean
```

### **🚀 API FastAPI (Utilisation Complète)**
```bash
# Activer l'environnement virtuel
source arkalia-luna-env/bin/activate

# Démarrer l'API (script automatique)
./scripts/start_api.sh

# Ou manuellement
python main.py

# Accéder à Swagger UI
# http://localhost:8000/docs

# Générer un logo via API
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"variant": "serenity", "size": 200, "generator": "ultimate"}'
```

### **🐳 Docker + Infrastructure (Production-Ready)**
```bash
# Démarrer toute l'infrastructure
docker-compose -f docker-compose.prod.yml up -d

# Services disponibles :
# 🌐 API : http://localhost:8000
# 📊 Prometheus : http://localhost:9090
# 📈 Grafana : http://localhost:3000
# 🔄 Nginx : http://localhost:80
```

### **🎨 Utilisation Complète du Potentiel**
```bash
# Explorer toutes les fonctionnalités
./scripts/quick_explore.sh

# Générer avec tous les générateurs avancés
python -m src.cli generate -v serenity -g ultimate    # Cosmique extrême
python -m src.cli generate -v power -g cosmic          # Sphères lumineuses
python -m src.cli generate -v mystery -g hyper_ai     # Hyper-IA
python -m src.cli generate -v awakening -g ai        # Stable Diffusion

# Tester toutes les variantes dynamiques
for variant in rainy stormy explosive sunny snowy; do
  python -m src.cli generate -v $variant -g ultimate
done
```

## 📝 **Conventions de Commit et PR**

### **Format des Titres de PR**
Tous les titres de PR doivent suivre le format : `type(scope): description`

**Types acceptés :**
- `feat` : Nouvelle fonctionnalité
- `fix` : Correction de bug
- `docs` : Documentation
- `style` : Formatage du code
- `refactor` : Refactoring
- `test` : Tests
- `chore` : Maintenance
- `perf` : Performance
- `ci` : CI/CD
- `build` : Build
- `revert` : Annulation

**Exemples valides :**
- ✅ `feat(logo): ajouter nouveau style mystique`
- ✅ `fix(tests): corriger erreur de validation`
- ✅ `docs: mise à jour README avec exemples`
- ✅ `style: reformater le code avec ruff`
- ✅ `ci: corriger workflow GitHub Actions`

**Formats rejetés :**
- ❌ `Ajouter nouveau style` (pas de type)
- ❌ `fix` (pas de description)
- ❌ `feat:` (pas de description)
- ❌ `feat(): description` (scope vide)

### **Commandes Makefile (plus rapides)**
```bash
# Configuration rapide
make quick-start

# Génération
make generate-all
make generate VARIANT=serenity
make favicon VARIANT=power

# Développement
make format      # Formatage du code
make lint        # Vérification du code
make test        # Lancement des tests
```

## 🏗️ **Architecture du Projet**

```
arkalia-luna-logo/
├── src/                          # Code source principal
│   ├── __init__.py              # Configuration du package
│   ├── variants.py              # Gestion des variantes émotionnelles
│   ├── svg_builder.py           # Classe abstraite pour les builders SVG
│   ├── logo_generator.py        # Générateur de base
│   ├── generator_factory.py     # Factory Pattern pour les générateurs
│   ├── cli.py                   # Interface CLI professionnelle
│   │
│   ├── **11 Générateurs Uniques** :
│   │   ├── logo_generator.py              # Base (default)
│   │   ├── dashboard_generator.py         # Interface optimisée
│   │   ├── ai_moon_generator.py           # IA réaliste
│   │   ├── advanced_logo_generator.py      # Techno-mystique
│   │   ├── simple_advanced_generator.py  # Équilibré
│   │   ├── ultra_max_generator.py         # Effets exceptionnels
│   │   ├── realism_max_generator.py       # Ultra-réaliste
│   │   ├── ultimate_generator.py          # Cosmique extrême
│   │   ├── ai_logo_generator.py           # Génération IA (Stable Diffusion)
│   │   ├── cosmic_logo_generator.py       # Sphères cosmiques
│   │   └── hyper_ai_generator.py          # Hyper-IA (ComfyUI + SDXL)
│   │
│   └── **Builders SVG Spécialisés** :
│       ├── svg_builder.py                 # Base abstraite
│       ├── svg_builder_dashboard.py       # Dashboard
│       ├── svg_builder_ai_moon.py         # AI-Moon
│       ├── svg_builder_advanced.py        # Advanced
│       ├── svg_builder_simple_advanced.py # Simple-Advanced
│       ├── svg_builder_ultra_max.py       # Ultra-Max
│       ├── svg_builder_realism_max.py     # Realism Max
│       ├── svg_builder_ultimate.py        # Ultimate
│       └── cosmic_sphere_builder.py       # Cosmic
│
├── tests/                       # Tests automatisés
├── docs/                        # Documentation
├── build/                       # Build séparé Python/React
│   ├── python/                 # Fichiers Python
│   └── react/                  # Composants React
├── exports/                     # Exports unifiés
│   ├── unified/                # Structure organisée
│   │   ├── logos/              # Logos SVG
│   │   ├── favicons/           # Favicons PNG
│   │   └── logs/               # Fichiers de log
│   ├── svg/                    # Versions vectorielles
│   ├── react/                  # Composants React
│   ├── lottie/                 # Animations Lottie
│   └── print/                  # Versions print
└── .github/                     # CI/CD GitHub Actions
```

## 🧪 **Tests et Qualité**

### **Tests Automatisés**
```bash
# Tests complets
pytest tests/ -v

# Tests avec couverture
pytest tests/ --cov=src --cov-report=html

# Tests rapides
pytest tests/ -x
```

### **Qualité du Code**
```bash
# Formatage
black src/ --line-length=88

# Linting
ruff check src/

# Vérification des types
mypy src/ --strict
```

## 🚀 **Développement**

### **🎯 Roadmap Stratégique**
Le projet suit une **roadmap stratégique** en 4 phases pour atteindre l'excellence :

- **🚨 Phase 1 (2-3 sem)** : Solidification technique (couverture 90%+, tests robustes)
- **🚨 Phase 2 (3-4 sem)** : UX exceptionnelle (démo en ligne, onboarding simple)
- **🟡 Phase 3 (2-3 sem)** : Distribution (PyPI, API externe)
- **🟢 Phase 4 (4+ sem)** : Communauté (badges, communication externe)

**📊 Suivi détaillé** : [Documentation complète](docs/ROADMAP_SUMMARY.md)

### **Ajout d'un Nouveau Style**
1. Créer `svg_builder_*.py` héritant de `SVGBuilder`
2. Implémenter la méthode abstraite `build_logo()`
3. Créer `*_generator.py` héritant de `ArkaliaLunaLogo`
4. Ajouter dans `generator_factory.py`
5. Ajouter les tests correspondants

### **Structure des Tests**
- **Tests unitaires** : Chaque composant testé individuellement
- **Tests d'intégration** : Flux complet de génération
- **Tests de performance** : Benchmark des générateurs
- **Tests de régression** : Validation des fonctionnalités

## 📊 **Performance**

### **Benchmark des Générateurs (Mise à jour)**
- **Realism Max** : ~0.002s ⚡ (Le plus rapide)
- **Dashboard** : ~0.004s
- **AI-Moon** : ~0.007s
- **Ultra-Max** : ~0.008s
- **Ultimate** : ~0.007s
- **Simple-Advanced** : ~0.008s
- **Advanced** : ~0.008s
- **Base** : ~0.013s

*Note : Les temps varient selon la taille et la complexité du logo*

## 🤝 **Contribution**

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 **Licence**

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🆘 **Support**

- **Issues** : [GitHub Issues](https://github.com/arkalia-luna/arkalia-luna-logo/issues)
- **Documentation** : [Documentation complète](docs/)
- **Discussions** : [GitHub Discussions](https://github.com/arkalia-luna/arkalia-luna-logo/discussions)

## 🌟 **Statut du Projet**

- **Version** : 2.0.0
- **Statut** : Production/Stable
- **Python** : 3.8+
- **Tests** : **297 tests passent** ✅
- **Couverture** : **75%** (objectif 90%+) ✅ **MIS À JOUR**
- **CI/CD** : GitHub Actions automatisé
- **Qualité** : Black + Ruff + MyPy
- **Benchmarks** : 7/7 tests de performance ✅

---

**🌙 Arkalia-LUNA Logo Generator** - Créé avec ❤️ par l'équipe Arkalia-LUNA

*Dernière mise à jour : Novembre 2025*
