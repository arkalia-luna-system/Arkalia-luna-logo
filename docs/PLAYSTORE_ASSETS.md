# 📱 Guide de Génération des Assets Play Store

Ce guide explique comment utiliser le générateur d'assets Play Store pour créer automatiquement tous les fichiers nécessaires à la publication sur Google Play Store.

## 🎯 Utilisation pour Arkalia CIA

Ce générateur a été développé et utilisé pour créer tous les assets Play Store de **Arkalia CIA**, une application mobile de santé qui sera publiée sur Google Play Console pour tests utilisateurs.

**Résultat :** Tous les assets nécessaires ont été générés avec succès :
- Feature Graphic (1024x500) avec logo Ultimate Serenity rouge
- Icône application (512x512) en version rouge
- 8 screenshots optimisés automatiquement

## 🎯 Assets Générés

Le générateur crée automatiquement :

1. **Feature Graphic (Bannière)** - 1024x500 pixels
   - Logo Arkalia CIA centré
   - Texte "Assistant Santé Personnel"
   - Couleurs : Bleu (#0175C2) et blanc
   - Format : PNG

2. **Screenshots Optimisés**
   - Redimensionnement automatique selon les limites Play Store
   - Conversion en JPEG optimisé
   - Conservation du ratio d'aspect
   - Taille max recommandée : 1080x1920 pixels (portrait)

## 🚀 Utilisation

### Installation des Dépendances

```bash
pip install pillow cairosvg
```

### Commande de Base

Générer tous les assets (feature graphic + screenshots) :

```bash
python -m src.cli playstore
```

### Options Disponibles

#### Générer uniquement la Feature Graphic

```bash
python -m src.cli playstore --feature-only
```

#### Optimiser uniquement les Screenshots

```bash
python -m src.cli playstore --screenshots-only
```

#### Spécifier le Logo

```bash
python -m src.cli playstore --logo exports/arkalia-luna-ultimate-serenity-200.svg
```

#### Spécifier le Répertoire des Screenshots

```bash
python -m src.cli playstore --screenshots-dir docs/screenshots/android
```

#### Spécifier le Répertoire de Sortie

```bash
python -m src.cli playstore --output-dir playstore-assets
```

#### Changer la Couleur de Fond de la Feature Graphic

```bash
python -m src.cli playstore --bg-color "#0175C2"
```

### Exemple Complet

```bash
python -m src.cli playstore \
  --logo exports/arkalia-luna-ultimate-serenity-200.svg \
  --screenshots-dir docs/screenshots/android \
  --output-dir playstore-assets \
  --bg-color "#FFFFFF"
```

## 📁 Structure des Fichiers

### Répertoire Source (Screenshots)

```
docs/screenshots/android/
├── screenshot-01-home-screen.jpeg
├── screenshot-03-documents-screen.jpeg
├── screenshot-06-reminders-screen.jpeg
└── screenshot-07-emergency-screen.jpeg
```

### Répertoire de Sortie

```
playstore-assets/
├── feature-graphic.png          # Bannière 1024x500
├── playstore-screenshot-01-home-screen.jpg
├── playstore-screenshot-03-documents-screen.jpg
├── playstore-screenshot-06-reminders-screen.jpg
└── playstore-screenshot-07-emergency-screen.jpg
```

## 🎨 Spécifications Play Store

### Feature Graphic

- **Dimensions** : 1024 x 500 pixels (obligatoire)
- **Format** : PNG ou JPEG
- **Taille max** : 1 Mo
- **Contenu** :
  - Logo Arkalia CIA centré
  - Texte "Assistant Santé Personnel"
  - Design simple et professionnel

### Phone Screenshots

- **Minimum** : 2 screenshots
- **Recommandé** : 4+ screenshots
- **Dimensions** :
  - Portrait : 1080 x 1920 pixels (recommandé)
  - Paysage : 1920 x 1080 pixels
  - Max : 3840 x 2160 pixels
- **Format** : JPEG ou PNG
- **Taille max** : 8 Mo par image

## 🔧 Utilisation en Python

```python
from pathlib import Path
from src.playstore_assets_generator import PlayStoreAssetsGenerator

# Initialiser le générateur
generator = PlayStoreAssetsGenerator(
    output_dir=Path("playstore-assets"),
    logo_path=Path("exports/arkalia-luna-ultimate-serenity-200.svg"),
    screenshots_dir=Path("docs/screenshots/android"),
)

# Générer la feature graphic
feature_path = generator.generate_feature_graphic()

# Optimiser un screenshot
screenshot_path = generator.optimize_screenshot(
    Path("docs/screenshots/android/screenshot-01-home-screen.jpeg")
)

# Générer tous les assets
assets = generator.generate_all_assets()
```

## ⚠️ Notes Importantes

1. **Logo** : Si aucun logo n'est spécifié, un logo par défaut avec le texte "Arkalia CIA" sera créé
2. **Screenshots** : Les images trop grandes seront automatiquement redimensionnées en gardant le ratio
3. **Formats** : Les screenshots seront convertis en JPEG pour optimiser la taille
4. **Transparence** : Les images avec transparence (PNG) seront converties avec un fond blanc

## 🐛 Dépannage

### Erreur : "cairosvg requis pour convertir SVG"

```bash
pip install cairosvg
```

### Erreur : "Pillow est requis"

```bash
pip install pillow
```

### Screenshots non trouvés

Vérifiez que le répertoire `docs/screenshots/android` existe et contient des fichiers image.

### Logo non trouvé

Le générateur créera automatiquement un logo par défaut si aucun logo n'est spécifié.

## 📝 Checklist de Publication

Avant de publier sur Play Store, vérifiez :

- [ ] Feature Graphic générée (1024x500 pixels)
- [ ] Au moins 2 screenshots optimisés
- [ ] Tous les fichiers dans le répertoire `playstore-assets/`
- [ ] Tailles des fichiers respectent les limites Play Store
- [ ] Qualité des images acceptable

## 🔗 Ressources

- [Documentation Play Store - Assets](https://support.google.com/googleplay/android-developer/answer/9866151)
- [Spécifications des Images](https://support.google.com/googleplay/android-developer/answer/9866151#zippy=%2Cfeature-graphic)

---

**Dernière mise à jour : 27 novembre 2025**

