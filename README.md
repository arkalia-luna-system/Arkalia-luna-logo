<div align="center">

# Arkalia-LUNA Logo Generator

**Générateur de Logos Vectoriels avec Intelligence Artificielle**

*11 Styles • 10 Variantes Émotionnelles • API REST • Production Ready*

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.0.0-orange?style=flat-square)](CHANGELOG.md)
[![Tests](https://img.shields.io/badge/Tests-297%20passed-brightgreen?style=flat-square)](tests/)

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 20px; display: inline-block; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
<img src="exports/screenshots/ultimate-serenity-200.svg" width="220" alt="Logo Arkalia-LUNA" style="filter: drop-shadow(0 8px 16px rgba(0,0,0,0.3));">
</div>

[Quick Start](#quick-start) • [Galerie](#galerie) • [Documentation](#documentation) • [API](#api-rest)

</div>

---

## Vue d'ensemble

Arkalia-LUNA Logo Generator est un générateur de logos vectoriels avec intégration d'intelligence artificielle. Il propose 11 styles uniques (8 vectoriels SVG + 3 générateurs IA) et 10 variantes émotionnelles pour créer plus de 110 combinaisons de logos.

**Caractéristiques principales :**
- Génération vectorielle SVG rapide (< 10ms)
- Génération IA avec Stable Diffusion et ComfyUI
- API REST FastAPI avec documentation Swagger
- Infrastructure Docker complète avec monitoring
- Interface CLI et support batch

## Quick Start

### Installation

```bash
git clone https://github.com/arkalia-luna-system/Arkalia-luna-logo.git
cd arkalia-luna-logo
python3 -m venv arkalia-luna-env
source arkalia-luna-env/bin/activate
pip install -e ".[dev]"
```

### Génération d'un logo

```bash
# Générer un logo Ultimate en variante Sérénité
python -m src.cli generate -v serenity -s 200 -g ultimate
```

Le logo sera généré dans le dossier `exports/`.

### Commandes utiles

```bash
# Voir toutes les variantes disponibles
python -m src.cli info

# Générer tous les logos
python -m src.cli generate-all -s 200

# Voir les générateurs disponibles
python -m src.cli generators
```

## Galerie

### Styles vectoriels

<div align="center">

<table>
<tr>
<td align="center" style="padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; margin: 10px;">
<img src="exports/screenshots/ultimate-serenity-200.svg" width="140" alt="Ultimate" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
<br/><strong style="color: white; margin-top: 10px; display: block;">Ultimate</strong>
<p style="color: rgba(255,255,255,0.9); font-size: 0.9em; margin: 5px 0 0 0;">Style cosmique</p>
</td>
<td align="center" style="padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 12px; margin: 10px;">
<img src="exports/screenshots/ai_moon-serenity-200.svg" width="140" alt="AI-Moon" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
<br/><strong style="color: white; margin-top: 10px; display: block;">AI-Moon</strong>
<p style="color: rgba(255,255,255,0.9); font-size: 0.9em; margin: 5px 0 0 0;">Style réaliste IA</p>
</td>
<td align="center" style="padding: 20px; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); border-radius: 12px; margin: 10px;">
<img src="exports/screenshots/dashboard-serenity-200.svg" width="140" alt="Dashboard" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
<br/><strong style="color: white; margin-top: 10px; display: block;">Dashboard</strong>
<p style="color: rgba(255,255,255,0.9); font-size: 0.9em; margin: 5px 0 0 0;">Interface optimisée</p>
</td>
<td align="center" style="padding: 20px; background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); border-radius: 12px; margin: 10px;">
<img src="exports/screenshots/advanced-serenity-200.svg" width="140" alt="Advanced" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
<br/><strong style="color: white; margin-top: 10px; display: block;">Advanced</strong>
<p style="color: rgba(255,255,255,0.9); font-size: 0.9em; margin: 5px 0 0 0;">Techno-mystique</p>
</td>
</tr>
<tr>
<td align="center" style="padding: 20px; background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); border-radius: 12px; margin: 10px;">
<img src="exports/screenshots/ultra_max-serenity-200.svg" width="140" alt="Ultra-Max" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
<br/><strong style="color: white; margin-top: 10px; display: block;">Ultra-Max</strong>
<p style="color: rgba(255,255,255,0.9); font-size: 0.9em; margin: 5px 0 0 0;">Effets avancés</p>
</td>
<td align="center" style="padding: 20px; background: linear-gradient(135deg, #30cfd0 0%, #330867 100%); border-radius: 12px; margin: 10px;">
<img src="exports/screenshots/realism_max-serenity-200.svg" width="140" alt="Realism Max" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
<br/><strong style="color: white; margin-top: 10px; display: block;">Realism Max</strong>
<p style="color: rgba(255,255,255,0.9); font-size: 0.9em; margin: 5px 0 0 0;">Style réaliste</p>
</td>
<td align="center" style="padding: 20px; background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); border-radius: 12px; margin: 10px;">
<img src="exports/screenshots/simple_advanced-serenity-200.svg" width="140" alt="Simple-Advanced" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
<br/><strong style="color: #333; margin-top: 10px; display: block;">Simple-Advanced</strong>
<p style="color: #666; font-size: 0.9em; margin: 5px 0 0 0;">Style équilibré</p>
</td>
<td align="center" style="padding: 20px; background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%); border-radius: 12px; margin: 10px;">
<img src="exports/screenshots/simple-serenity-200.svg" width="140" alt="Base" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
<br/><strong style="color: #333; margin-top: 10px; display: block;">Base</strong>
<p style="color: #666; font-size: 0.9em; margin: 5px 0 0 0;">Style minimaliste</p>
</td>
</tr>
</table>

</div>

### Variantes émotionnelles

Chaque style supporte 10 variantes émotionnelles. Voici un exemple avec le style **Ultimate** :

<div align="center">

<table>
<tr>
<td align="center" style="padding: 15px;">
<img src="exports/screenshots/ultimate-serenity-200.svg" width="120" alt="Sérénité" style="border-radius: 8px; background: #f0f9ff; padding: 10px;">
<br/><strong>Sérénité</strong>
</td>
<td align="center" style="padding: 15px;">
<img src="exports/screenshots/ultimate-power-200.svg" width="120" alt="Puissance" style="border-radius: 8px; background: #fef2f2; padding: 10px;">
<br/><strong>Puissance</strong>
</td>
<td align="center" style="padding: 15px;">
<img src="exports/screenshots/ultimate-mystery-200.svg" width="120" alt="Mystère" style="border-radius: 8px; background: #faf5ff; padding: 10px;">
<br/><strong>Mystère</strong>
</td>
<td align="center" style="padding: 15px;">
<img src="exports/screenshots/ultimate-awakening-200.svg" width="120" alt="Éveil" style="border-radius: 8px; background: #f0fdf4; padding: 10px;">
<br/><strong>Éveil</strong>
</td>
<td align="center" style="padding: 15px;">
<img src="exports/screenshots/ultimate-creative-200.svg" width="120" alt="Créative" style="border-radius: 8px; background: #fffbeb; padding: 10px;">
<br/><strong>Créative</strong>
</td>
</tr>
</table>

**Variantes de base** : Sérénité, Puissance, Mystère, Éveil, Créative  
**Variantes dynamiques** : Pluie, Orage, Explosive, Ensoleillé, Neige

</div>

### Génération IA

Le projet intègre 3 générateurs IA :

1. **Stable Diffusion** - Génération locale avec modèle v1.5
2. **ComfyUI + SDXL** - Génération haute qualité jusqu'à 1024x1024
3. **Cosmic** - Sphères cosmiques vectorielles avec réseaux neuronaux

## Installation

### Option 1 : Installation standard (recommandée)

```bash
git clone https://github.com/arkalia-luna-system/Arkalia-luna-logo.git
cd arkalia-luna-logo
make quick-start
```

### Option 2 : Installation manuelle

```bash
python3 -m venv arkalia-luna-env
source arkalia-luna-env/bin/activate  # Linux/Mac
pip install -e ".[dev]"
```

### Option 3 : Docker

```bash
docker-compose -f docker-compose.prod.yml up -d
```

Services disponibles :
- API : http://localhost:8000
- Prometheus : http://localhost:9090
- Grafana : http://localhost:3000

### Option 4 : Avec génération IA

Pour utiliser les générateurs IA, installez les dépendances supplémentaires :

```bash
# Stable Diffusion
pip install torch diffusers transformers accelerate

# ComfyUI
bash scripts/install_comfyui.sh
bash scripts/start_comfyui.sh
```

## Utilisation

### Interface CLI

```bash
# Générer un logo spécifique
python -m src.cli generate -v serenity -s 200 -g ultimate

# Générer avec IA
python -m src.cli generate -v serenity -s 512 -g ai

# Générer toutes les variantes
python -m src.cli generate-all -s 200

# Créer des favicons
python -m src.cli favicon-all -s 32
```

### Utilisation en Python

```python
from src.generator_factory import LogoGeneratorFactory

# Créer un générateur
generator = LogoGeneratorFactory.create_generator("ultimate")

# Générer un logo
logo_path = generator.generate_svg_logo("serenity", size=200)
print(f"Logo généré : {logo_path}")
```

## API REST

### Démarrage

```bash
python main.py
```

L'API est accessible sur http://localhost:8000 avec la documentation Swagger sur `/docs`.

### Endpoints principaux

- `POST /generate` - Générer un logo
- `GET /variants` - Lister les variantes disponibles
- `GET /generators` - Lister les générateurs disponibles
- `GET /stats` - Statistiques de génération
- `GET /metrics` - Métriques Prometheus

### Exemple d'utilisation

```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"variant": "serenity", "size": 200, "generator": "ultimate"}'
```

## Architecture

```
arkalia-luna-logo/
├── src/                    # Code source
│   ├── *_generator.py      # Générateurs de logos
│   ├── svg_builder*.py     # Builders SVG spécialisés
│   └── cli.py              # Interface CLI
├── tests/                  # Tests automatisés
├── docs/                   # Documentation
├── exports/                # Logos générés
└── .github/                # CI/CD
```

Le projet utilise un pattern Factory pour gérer les différents générateurs et un système de builders pour la construction SVG.

## Performance

- **Génération vectorielle** : < 10ms par logo
- **Génération IA Stable Diffusion** : 5-10 secondes
- **Génération IA ComfyUI** : 10-30 secondes (selon résolution)

## Documentation

- [Guide de démarrage rapide](docs/QUICKSTART.md)
- [Documentation API](docs/API.md)
- [Architecture technique](docs/ARCHITECTURE.md)
- [Guide ComfyUI](docs/COMFYUI.md)
- [Index complet](docs/INDEX.md)

## Contribution

Les contributions sont les bienvenues ! Veuillez suivre les conventions de commit :

- Format : `type(scope): description`
- Types : `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Exemples :
- `feat(logo): ajouter nouveau style`
- `fix(tests): corriger erreur de validation`
- `docs: mise à jour README`

## Statut du projet

| Métrique | Valeur |
|:--------:|:------:|
| Version | 2.0.0 |
| Python | 3.8+ |
| Tests | 297 tests passent |
| Couverture | 75% |
| Générateurs | 11 styles |
| Variantes | 10 émotionnelles |

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

<div align="center">

**Arkalia-LUNA Logo Generator** - Créé avec ❤️ par l'équipe Arkalia-LUNA

*Dernière mise à jour : Novembre 2025*

</div>
