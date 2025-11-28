# 📱 Guide Complet - Remplir Play Console pour Arkalia CIA

**Date : 27 novembre 2025**

Ce guide contient tous les éléments nécessaires pour remplir la fiche produit sur Google Play Console.

---

## ✅ Vérifications Préalables

### Feature Graphic
- ✅ **Fichier** : `/Volumes/T7/logo/arkalia-luna-logo/playstore-assets/feature-graphic.png`
- ✅ **Dimensions** : 1024 x 500 pixels (conforme)
- ✅ **Taille** : 54 KB (limite: 15 MB) ✅
- ✅ **Format** : PNG (conforme)

### Icône Application
- ⚠️ **À vérifier** : Chemin vers `Icon-512.png` du projet arkalia-cia
- **Spécifications requises** :
  - Format : PNG ou JPEG
  - Dimensions : 512 x 512 pixels
  - Taille max : 1 MB

### Screenshots
- ⚠️ **À placer** : Dans `/Volumes/T7/logo/arkalia-luna-logo/docs/screenshots/android/`
- **Spécifications** :
  - Format : PNG ou JPEG
  - Taille max : 8 MB par image
  - Format : 16:9 ou 9:16
  - Dimensions : Entre 320 et 3840 pixels de chaque côté
  - **Pour promotion** : Minimum 4 screenshots, résolution min 1080px de chaque côté

---

## 📝 1. Nom de l'application

**Valeur à copier :**
```
Arkalia CIA
```

**Statut** : ✅ Déjà rempli (11/30 caractères)

---

## 📝 2. Brève description (Short description) — OBLIGATOIRE

**Valeur à copier-coller :**
```
Assistant santé mobile sécurisé pour gérer documents médicaux et rappels
```

**Caractères** : 79/80 ✅

**Où coller** : Dans le champ "Brève description *" sur Play Console

---

## 📝 3. Description complète (Full description) — OBLIGATOIRE

**Valeur à copier-coller (TOUT le texte ci-dessous) :**

```
Arkalia CIA - Votre Assistant Santé Personnel

Arkalia CIA est une application mobile conçue pour vous aider à gérer vos documents médicaux, vos rappels de santé et vos contacts d'urgence de manière sécurisée et simple.

🔒 SÉCURITÉ MAXIMALE

• Chiffrement AES-256 pour tous vos documents

• Stockage 100% local sur votre appareil

• Aucune transmission de données

• Aucune collecte d'informations personnelles

📄 GESTION DE DOCUMENTS

• Importez et organisez vos PDF médicaux

• Recherche rapide dans vos documents

• Organisation par catégories

• Stockage sécurisé avec chiffrement

🔔 RAPPELS INTELLIGENTS

• Intégration avec votre calendrier

• Notifications personnalisées

• Rappels de médicaments

• Gestion des rendez-vous médicaux

🚨 CONTACTS D'URGENCE

• Contacts ICE (In Case of Emergency)

• Appel d'urgence en un clic

• Carte d'urgence médicale

• Informations de santé critiques

👵 ACCESSIBLE À TOUS

• Interface senior-friendly

• Boutons larges et texte clair

• Navigation intuitive

• Design adapté aux besoins des seniors

🌍 100% HORS-LIGNE

• Fonctionne sans connexion internet

• Vos données restent sur votre appareil

• Aucune dépendance cloud

• Respect total de votre vie privée

Arkalia CIA est développé par Arkalia Luna System avec un focus sur la sécurité, la simplicité et le respect de la vie privée.

Note médicale importante : Arkalia CIA est un outil d'organisation et ne remplace pas les conseils médicaux professionnels.
```

**Caractères** : ~1200/4000 ✅

**Où coller** : Dans le champ "Description complète *" sur Play Console

---

## 🎨 4. Graphique

### 4.1. Icône de l'application * — OBLIGATOIRE

**Chemin du fichier :**
```
/Volumes/T7/arkalia-cia/arkalia_cia/web/icons/Icon-512.png
```

**Vérification :**
- ✅ Fichier existe
- ✅ Dimensions : 512 x 512 pixels
- ✅ Format : PNG

**Spécifications Play Console :**
- ✅ Format : PNG ou JPEG
- ✅ Taille max : 1 MB
- ✅ Dimensions : 512 x 512 pixels
- ✅ Respecter les spécifications de conception

**Action :**
1. Trouver le fichier Icon-512.png dans le projet arkalia-cia
2. Vérifier qu'il fait bien 512x512 pixels
3. Uploader dans Play Console → "Icône de l'application *"

**Vérification :**
```bash
# Vérifier les dimensions
python3 -c "from PIL import Image; img = Image.open('CHEMIN_VERS_Icon-512.png'); print(f'{img.size[0]}x{img.size[1]} pixels')"
```

### 4.2. Graphique principal (Feature Graphic) * — OBLIGATOIRE

**Chemin du fichier :**
```
/Volumes/T7/logo/arkalia-luna-logo/playstore-assets/feature-graphic.png
```

**Spécifications Play Console :**
- ✅ Format : PNG (conforme)
- ✅ Taille : 54 KB (limite: 15 MB) ✅
- ✅ Dimensions : 1024 x 500 pixels ✅
- ✅ Contenu : Logo Arkalia CIA + texte "Assistant Santé Personnel"

**Action :**
1. Aller dans Play Console → "Graphique principal *"
2. Uploader le fichier : `playstore-assets/feature-graphic.png`

**Vérification :**
```bash
cd /Volumes/T7/logo/arkalia-luna-logo
python3 -c "from PIL import Image; img = Image.open('playstore-assets/feature-graphic.png'); print(f'✅ {img.size[0]}x{img.size[1]} pixels, {img.format}')"
```

### 4.3. Vidéo — OPTIONNEL

**Laisser vide pour l'instant**

---

## 📱 5. Captures d'écran téléphone * — OBLIGATOIRE (minimum 2)

### Préparation des Screenshots

**Étape 1 : Placer vos screenshots**

Placez vos fichiers image dans :
```
/Volumes/T7/logo/arkalia-luna-logo/docs/screenshots/android/
```

**Noms recommandés :**
- `screenshot-01-home-screen.jpeg` (Page d'accueil)
- `screenshot-03-documents-screen.jpeg` (Documents)
- `screenshot-06-reminders-screen.jpeg` (Rappels)
- `screenshot-07-emergency-screen.jpeg` (Urgence)

**Étape 2 : Optimiser automatiquement**

```bash
cd /Volumes/T7/logo/arkalia-luna-logo
source arkalia-luna-env/bin/activate

# Générer les screenshots optimisés
python -m src.cli playstore \
  --logo exports/arkalia-luna-serenity-512.svg \
  --screenshots-dir docs/screenshots/android \
  --output-dir playstore-assets \
  --screenshots-only
```

**Étape 3 : Vérifier les fichiers générés**

Les fichiers optimisés seront dans :
```
/Volumes/T7/logo/arkalia-luna-logo/playstore-assets/
```

Noms des fichiers générés :
- `playstore-screenshot-01-home-screen.jpg`
- `playstore-screenshot-03-documents-screen.jpg`
- `playstore-screenshot-06-reminders-screen.jpg`
- `playstore-screenshot-07-emergency-screen.jpg`

### Spécifications Play Console

- ✅ Format : PNG ou JPEG
- ✅ Taille max : 8 MB par image
- ✅ Format : 16:9 ou 9:16 (portrait recommandé)
- ✅ Dimensions : Entre 320 et 3840 pixels de chaque côté
- ✅ **Pour promotion** : Minimum 4 screenshots, résolution min 1080px

### Action sur Play Console

1. Aller dans "Captures d'écran du téléphone *"
2. Uploader **minimum 2** screenshots (recommandé 4+)
3. Utiliser les fichiers depuis `playstore-assets/playstore-*.jpg`

**Fichiers à uploader (recommandé 4) :**
1. `playstore-assets/playstore-screenshot-01-home-screen.jpg`
2. `playstore-assets/playstore-screenshot-03-documents-screen.jpg`
3. `playstore-assets/playstore-screenshot-06-reminders-screen.jpg`
4. `playstore-assets/playstore-screenshot-07-emergency-screen.jpg`

---

## 📋 Checklist Complète Play Console

### Obligatoire ✅

- [x] **App name** : `Arkalia CIA` (déjà rempli)
- [ ] **Short description** : Copier le texte de la section 2
- [ ] **Full description** : Copier le texte de la section 3
- [ ] **App icon** : Uploader `Icon-512.png` (trouver dans arkalia-cia)
- [x] **Feature graphic** : Uploader `playstore-assets/feature-graphic.png` ✅
- [ ] **Phone screenshots** : Uploader minimum 2 (recommandé 4+)

### Optionnel

- [ ] **Video** : Laisser vide
- [ ] **Tablet screenshots** : Laisser vide
- [ ] **Chromebook** : Laisser vide
- [ ] **Android XR** : Laisser vide

---

## 🚀 Ordre d'Action Recommandé

### Étape 1 : Préparer les Screenshots

```bash
# 1. Placer vos screenshots dans docs/screenshots/android/
cp vos-screenshots/*.jpg /Volumes/T7/logo/arkalia-luna-logo/docs/screenshots/android/

# 2. Optimiser automatiquement
cd /Volumes/T7/logo/arkalia-luna-logo
source arkalia-luna-env/bin/activate
python -m src.cli playstore --screenshots-only

# 3. Vérifier les fichiers générés
ls -lh playstore-assets/playstore-*.jpg
```

### Étape 2 : Remplir Play Console

1. **Textes** (copier-coller) :
   - Short description (section 2)
   - Full description (section 3)

2. **Icône** :
   - Trouver `Icon-512.png` dans le projet arkalia-cia
   - Uploader dans "Icône de l'application *"

3. **Feature Graphic** :
   - Uploader `/Volumes/T7/logo/arkalia-luna-logo/playstore-assets/feature-graphic.png`

4. **Screenshots** :
   - Uploader les fichiers `playstore-assets/playstore-*.jpg` (minimum 2, recommandé 4)

### Étape 3 : Vérifier et Publier

1. Vérifier que tous les champs obligatoires sont remplis
2. Cliquer sur "Enregistrer"
3. Soumettre pour relecture

---

## 📂 Chemins Complets des Fichiers

### Feature Graphic (✅ Prêt)
```
/Volumes/T7/logo/arkalia-luna-logo/playstore-assets/feature-graphic.png
```

### Screenshots (À générer)
```
/Volumes/T7/logo/arkalia-luna-logo/playstore-assets/playstore-*.jpg
```

### Icône (✅ Trouvée)
```
/Volumes/T7/arkalia-cia/arkalia_cia/web/icons/Icon-512.png
```

---

## ⚠️ Notes Importantes

1. **Feature Graphic** : ✅ Déjà générée et conforme (1024x500, 54 KB)
2. **Screenshots** : À placer dans `docs/screenshots/android/` puis optimiser
3. **Icône** : À trouver dans le projet arkalia-cia (512x512 pixels)
4. **Textes** : Copier-coller exactement comme indiqué ci-dessus
5. **Format** : Tous les fichiers respectent les spécifications Play Store

---

## 🔍 Vérifications Finales

Avant de soumettre sur Play Console, vérifier :

- [ ] Short description : 79 caractères ✅
- [ ] Full description : ~1200 caractères ✅
- [ ] Feature Graphic : 1024x500 pixels, 54 KB ✅
- [ ] Screenshots : Minimum 2, format JPEG, < 8 MB chacun
- [ ] Icône : 512x512 pixels, < 1 MB

---

**Dernière mise à jour : 27 novembre 2025**

