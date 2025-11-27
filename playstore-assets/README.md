# 📱 Assets Play Store Générés

Ce répertoire contient les assets générés pour la publication sur Google Play Store.

## ✅ Assets Disponibles

### Feature Graphic (Bannière)
- **Fichier** : `feature-graphic.png`
- **Dimensions** : 1024 x 500 pixels ✅
- **Taille** : ~54 KB (limite: 1 MB) ✅
- **Format** : PNG optimisé
- **Contenu** :
  - Logo Arkalia CIA centré
  - Texte "Assistant Santé Personnel"
  - Couleurs : Bleu (#0175C2) et blanc

## 📱 Screenshots

Pour générer les screenshots optimisés, placez vos images dans `docs/screenshots/android/` et exécutez :

```bash
python -m src.cli playstore \
  --logo exports/arkalia-luna-serenity-512.svg \
  --screenshots-dir docs/screenshots/android \
  --output-dir playstore-assets
```

### Formats acceptés
- `.jpg` / `.jpeg`
- `.png`
- `.webp`

### Optimisation automatique
- Redimensionnement si > 1080x1920 pixels
- Conversion en JPEG (qualité 92)
- Conservation du ratio d'aspect
- Nommage automatique avec préfixe `playstore-`

## 🚀 Utilisation

1. **Feature Graphic** : Uploader `feature-graphic.png` dans Play Console
2. **Screenshots** : Uploader les fichiers `playstore-*.jpg` générés

## 📝 Notes

- Les screenshots trop grands seront automatiquement redimensionnés
- Les images transparentes seront converties avec fond blanc
- Tous les fichiers respectent les limites Play Store

---

**Dernière mise à jour : 27 novembre 2025**

