# 🎨 Guide ComfyUI Étape par Étape - Génération de Logo

<div align="center">

**Guide visuel pour générer votre premier logo avec ComfyUI**

</div>

---

## 📋 Vue d'Ensemble

Vous voyez l'interface ComfyUI avec la fenêtre modale **"Commencez avec un modèle"**.

<div align="center">

| Étape | Action | Résultat |
|:-----:|:------:|:--------:|
| **1** | Cliquer sur "Génération d'Image" | Workflow de base chargé |
| **2** | Configurer le prompt | Description du logo |
| **3** | Choisir le modèle | SDXL ou autre |
| **4** | Cliquer "Exécuter" | Logo généré |

</div>

---

## 🚀 Étape par Étape

### **Étape 1 : Choisir le Type de Génération**

Dans la fenêtre modale que vous voyez :

1. **Cliquez sur la carte "Génération d'Image"** (Image Generation)
   - C'est la carte avec l'image d'une bouteille en verre contenant un paysage miniature avec un ciel étoilé
   - Description : "Générez des images à partir de descriptions textuelles"

**Résultat** : Le workflow de base se charge automatiquement avec tous les nœuds nécessaires.

---

### **Étape 2 : Comprendre le Workflow Chargé**

Après avoir cliqué sur "Génération d'Image", vous verrez plusieurs nœuds connectés :

<div align="center">

```
CheckpointLoaderSimple
├─→ CLIPTextEncode (positive) ──┐
├─→ CLIPTextEncode (negative) ───┤
├─→ EmptyLatentImage ────────────┼─→ KSampler
└─→ VAE ─────────────────────────┘
                                    │
                                    ↓
                              VAEDecode
                                    │
                                    ↓
                              SaveImage
```

</div>

**Nœuds principaux** :

| Nœud | Rôle | À Configurer |
|:----:|:----:|:------------:|
| **CheckpointLoaderSimple** | Charge le modèle IA | ✅ Choisir le modèle |
| **CLIPTextEncode (positive)** | Prompt positif | ✅ **Votre description du logo** |
| **CLIPTextEncode (negative)** | Prompt négatif | ✅ Ce que vous ne voulez pas |
| **EmptyLatentImage** | Taille de l'image | ✅ Largeur/Hauteur |
| **KSampler** | Paramètres de génération | ✅ Steps, CFG, etc. |
| **SaveImage** | Sauvegarde | ✅ Automatique |

---

### **Étape 3 : Configurer le Prompt (Le Plus Important !)**

#### **3.1 : Prompt Positif (CLIPTextEncode positive)**

Cliquez sur le nœud **CLIPTextEncode (positive)** et entrez votre description :

**Exemple pour un logo cosmique** :
```
cosmic sphere, neural network, glowing orb, serenity colors, 
professional logo design, minimalist, high quality, 
luminous energy veins, central crystal core
```

**Exemples par variante émotionnelle** :

| Variante | Prompt Exemple |
|:--------:|:--------------:|
| **Serenity** | `cosmic sphere, calm blue colors, peaceful energy, serene atmosphere, professional logo` |
| **Power** | `cosmic sphere, vibrant red and orange, powerful energy, dynamic, professional logo` |
| **Mystery** | `cosmic sphere, deep purple and dark blue, mysterious energy, enigmatic, professional logo` |
| **Awakening** | `cosmic sphere, bright yellow and gold, awakening energy, radiant, professional logo` |

#### **3.2 : Prompt Négatif (CLIPTextEncode negative)**

Cliquez sur le nœud **CLIPTextEncode (negative)** et entrez :

```
text, watermark, signature, blurry, low quality, distorted, 
ugly, bad anatomy, extra limbs, duplicate, poorly drawn
```

---

### **Étape 4 : Choisir le Modèle**

Cliquez sur le nœud **CheckpointLoaderSimple** :

1. Dans le champ `ckpt_name`, cliquez sur la liste déroulante
2. Choisissez un modèle :
   - **SDXL Base** : `sd_xl_base_1.0.safetensors` (recommandé pour logos)
   - **SD 1.5** : `v1-5-pruned-emaonly.safetensors` (plus rapide)
   - **Autre modèle** : Selon vos préférences

**⚠️ Note** : Si vous ne voyez pas de modèles, ils doivent être téléchargés. Voir `docs/COMFYUI.md` pour l'installation.

---

### **Étape 5 : Configurer la Taille**

Cliquez sur le nœud **EmptyLatentImage** :

- **width** : `1024` (ou `512` pour plus rapide)
- **height** : `1024` (ou `512` pour plus rapide)
- **batch_size** : `1`

**💡 Pour les logos** : 512x512 ou 1024x1024 fonctionnent bien.

---

### **Étape 6 : Paramètres de Génération (Optionnel)**

Cliquez sur le nœud **KSampler** :

| Paramètre | Valeur Recommandée | Description |
|:---------:|:------------------:|:-----------:|
| **seed** | `0` ou "randomize" | Graine aléatoire pour varier |
| **steps** | `20-30` | Nombre d'itérations (plus = meilleur mais plus lent) |
| **cfg** | `7.0-8.0` | Force du prompt (plus = suit mieux le prompt) |
| **sampler_name** | `euler` ou `euler_ancestral` | Algorithme de génération |
| **scheduler** | `simple` ou `normal` | Planification des étapes |

**Valeurs par défaut** : Généralement bonnes pour commencer.

---

### **Étape 7 : Générer le Logo**

1. **Vérifiez que tous les nœuds sont connectés** (lignes entre les nœuds)
2. **Cliquez sur "Exécuter"** (Execute) en bas de l'interface
   - Ou utilisez le raccourci clavier : `Ctrl+Enter` (Windows/Linux) ou `Cmd+Enter` (Mac)

**⏱️ Temps d'attente** : 
- 512x512 : ~10-30 secondes
- 1024x1024 : ~30-60 secondes

---

### **Étape 8 : Récupérer le Logo**

Une fois la génération terminée :

1. **L'image apparaît dans le nœud SaveImage**
2. **Cliquez sur l'image** pour l'agrandir
3. **Clic droit sur l'image** → "Save Image As..." pour télécharger
4. **Ou** : L'image est sauvegardée dans `exports-hyper-ai/` (dossier configuré)

---

## 🎯 Exemple Complet : Logo "Serenity"

### **Configuration**

1. **CheckpointLoaderSimple** :
   - `ckpt_name` : `sd_xl_base_1.0.safetensors`

2. **CLIPTextEncode (positive)** :
   - `text` : `cosmic sphere, neural network, glowing orb, calm blue and cyan colors, serene atmosphere, professional logo design, minimalist, high quality, luminous energy veins, central crystal core`

3. **CLIPTextEncode (negative)** :
   - `text` : `text, watermark, signature, blurry, low quality, distorted, ugly, bad anatomy`

4. **EmptyLatentImage** :
   - `width` : `1024`
   - `height` : `1024`
   - `batch_size` : `1`

5. **KSampler** :
   - `seed` : `0`
   - `steps` : `25`
   - `cfg` : `7.5`
   - `sampler_name` : `euler`
   - `scheduler` : `simple`

6. **Cliquez "Exécuter"**

**Résultat** : Un logo cosmique avec des couleurs calmes (bleu/cyan) dans le style "Serenity".

---

## 💡 Astuces

### **Pour Varier les Résultats**

- **Changez le seed** : `0`, `1`, `42`, `123`, etc. (ou "randomize")
- **Ajustez le CFG** : Plus haut = suit mieux le prompt, plus bas = plus créatif
- **Modifiez les steps** : Plus = meilleure qualité mais plus lent

### **Pour Améliorer la Qualité**

- Utilisez **SDXL** plutôt que SD 1.5
- Augmentez les **steps** à 30-50
- Utilisez un **prompt plus détaillé**
- Ajoutez des mots-clés : `high quality, professional, detailed, 4k, 8k`

### **Pour Accélérer**

- Utilisez **512x512** au lieu de 1024x1024
- Réduisez les **steps** à 15-20
- Utilisez **SD 1.5** au lieu de SDXL

---

## ⚠️ Problèmes Courants

### **"Prompt has no outputs"**

**Cause** : Workflow incomplet ou nœuds non connectés.

**Solution** : 
- Vérifiez que tous les nœuds sont connectés
- Utilisez "Génération d'Image" pour charger un workflow complet

### **"Model not found"**

**Cause** : Le modèle n'est pas téléchargé.

**Solution** : 
- Téléchargez le modèle via ComfyUI Manager
- Ou utilisez un modèle déjà installé

### **Génération très lente**

**Cause** : Résolution trop élevée ou steps trop nombreux.

**Solution** : 
- Réduisez la taille (512x512)
- Réduisez les steps (15-20)

---

## 🎉 Alternative Plus Simple : Arkalia-LUNA

Si tout ça vous semble compliqué, utilisez Arkalia-LUNA :

```bash
source arkalia-luna-env/bin/activate
python -m src.cli generate --variant serenity --generator hyper_ai --size 512
```

**Avantages** :
- ✅ Tout est automatique
- ✅ Pas besoin de configurer ComfyUI
- ✅ Workflow complet généré automatiquement
- ✅ Prompts optimisés selon la variante

---

**Créé** : 2025-11-09  
**Dernière mise à jour** : 2025-11-09

