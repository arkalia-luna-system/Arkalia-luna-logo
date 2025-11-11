# 🔧 Guide d'Installation des Modèles ComfyUI

<div align="center">

**Comment installer les modèles manquants dans ComfyUI**

</div>

---

## 🎯 Problème : "Modèles manquants"

Si ComfyUI vous dit que des modèles sont manquants, c'est qu'ils ne sont pas dans le bon dossier.

<div align="center">

| Situation | Solution |
|:---------:|:--------:|
| **Modèles téléchargés dans Téléchargements** | Script automatique |
| **Modèles téléchargés ailleurs** | Déplacement manuel |
| **Modèles pas encore téléchargés** | Téléchargement via script |

</div>

---

## 🚀 Solution 1 : Script Automatique (Recommandé)

### **Si vous avez téléchargé les modèles dans Téléchargements**

```bash
bash scripts/install_models_comfyui.sh
```

**Ce script** :
- ✅ Cherche les modèles dans `~/Downloads`
- ✅ Les déplace automatiquement vers les bons dossiers
- ✅ Affiche les modèles déjà installés
- ✅ Vous dit où placer les modèles manuellement si besoin

---

## 📋 Solution 2 : Installation Manuelle

### **Emplacements des Modèles**

ComfyUI cherche les modèles dans ces dossiers :

<div align="center">

| Type de Modèle | Dossier | Extensions |
|:--------------:|:------:|:----------:|
| **Checkpoints** (modèles principaux) | `comfyui/models/checkpoints/` | `.safetensors`, `.ckpt` |
| **ControlNet** | `comfyui/models/controlnet/` | `.safetensors`, `.ckpt` |
| **VAE** | `comfyui/models/vae/` | `.safetensors`, `.ckpt`, `.pt` |
| **LoRA** | `comfyui/models/loras/` | `.safetensors`, `.ckpt` |
| **Upscale** | `comfyui/models/upscale_models/` | `.pth` |
| **CLIP** | `comfyui/models/clip/` | `.safetensors`, `.pt` |
| **Embeddings** | `comfyui/models/embeddings/` | `.pt`, `.bin` |

</div>

### **Étapes Manuelles**

1. **Trouvez votre modèle téléchargé**
   - Dans Téléchargements, Bureau, ou ailleurs

2. **Identifiez le type de modèle** :
   - **Checkpoint** : Gros fichier (1-7GB), nom comme `sd_xl_base_1.0.safetensors`
   - **ControlNet** : Nom contient "controlnet", "canny", "depth"
   - **VAE** : Nom contient "vae"
   - **LoRA** : Nom contient "lora", généralement plus petit (<1GB)

3. **Déplacez le modèle** :
   ```bash
   # Exemple : Déplacer un checkpoint
   mv ~/Downloads/sd_xl_base_1.0.safetensors comfyui/models/checkpoints/
   
   # Exemple : Déplacer un ControlNet
   mv ~/Downloads/controlnet_canny.safetensors comfyui/models/controlnet/
   ```

4. **Redémarrez ComfyUI** :
   ```bash
   bash scripts/stop_comfyui.sh
   bash scripts/start_comfyui.sh
   ```

5. **Rafraîchissez l'interface web** (F5)

---

## 📥 Solution 3 : Téléchargement Automatique

### **Modèles SDXL (Recommandés pour Logos)**

```bash
bash scripts/install_comfyui.sh
```

Ce script télécharge automatiquement :
- ✅ SDXL Base (`sd_xl_base_1.0.safetensors`) - ~7GB
- ✅ SDXL Refiner (`sd_xl_refiner_1.0.safetensors`) - ~7GB
- ✅ ControlNet Canny - ~1GB
- ✅ ControlNet Depth - ~1GB
- ✅ RealESRGAN (upscale) - ~100MB

### **Téléchargement Manuel d'un Modèle Spécifique**

Si vous voulez télécharger un modèle spécifique :

```bash
cd comfyui/models/checkpoints

# Exemple : SDXL Base
wget -O sd_xl_base_1.0.safetensors \
  "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors"

# Exemple : SD 1.5 (plus petit, plus rapide)
wget -O v1-5-pruned-emaonly.safetensors \
  "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors"
```

---

## 🔍 Vérifier les Modèles Installés

### **Via Script**

```bash
bash scripts/install_models_comfyui.sh
```

Affiche tous les modèles installés par catégorie.

### **Via Terminal**

```bash
# Checkpoints
ls -lh comfyui/models/checkpoints/

# ControlNet
ls -lh comfyui/models/controlnet/

# VAE
ls -lh comfyui/models/vae/
```

### **Via Interface ComfyUI**

1. Ouvrez http://localhost:8188
2. Cliquez sur le nœud **CheckpointLoaderSimple**
3. Le menu déroulant `ckpt_name` liste tous les modèles disponibles

---

## ⚠️ Problèmes Courants

### **"Model not found" après installation**

**Solution** :
1. Vérifiez que le fichier est bien dans le bon dossier
2. Vérifiez l'extension (`.safetensors` ou `.ckpt`)
3. Redémarrez ComfyUI
4. Rafraîchissez l'interface (F5)

### **Modèle trop gros pour Téléchargements**

**Solution** :
1. Téléchargez directement dans le bon dossier :
   ```bash
   cd comfyui/models/checkpoints
   wget "URL_DU_MODELE"
   ```

### **Modèle dans un sous-dossier**

**Solution** :
ComfyUI ne cherche pas dans les sous-dossiers. Déplacez le modèle à la racine :
```bash
# Mauvais : comfyui/models/checkpoints/sous-dossier/modele.safetensors
# Bon : comfyui/models/checkpoints/modele.safetensors

mv comfyui/models/checkpoints/sous-dossier/modele.safetensors \
   comfyui/models/checkpoints/modele.safetensors
```

---

## 📚 Modèles Recommandés pour Logos

<div align="center">

| Modèle | Taille | Usage | Téléchargement |
|:------:|:------:|:-----:|:--------------:|
| **SDXL Base** | ~7GB | ⭐ Logos haute qualité | `bash scripts/install_comfyui.sh` |
| **SD 1.5** | ~4GB | Logos rapides | Manuel (voir ci-dessus) |
| **ControlNet Canny** | ~1GB | Contrôle par contours | `bash scripts/install_comfyui.sh` |
| **ControlNet Depth** | ~1GB | Contrôle par profondeur | `bash scripts/install_comfyui.sh` |

</div>

---

## 🎯 Résumé Rapide

**Si modèles dans Téléchargements** :
```bash
bash scripts/install_models_comfyui.sh
```

**Si modèles ailleurs** :
```bash
mv /chemin/vers/modele.safetensors comfyui/models/checkpoints/
bash scripts/stop_comfyui.sh && bash scripts/start_comfyui.sh
```

**Si pas de modèles** :
```bash
bash scripts/install_comfyui.sh
```

---

**Créé** : Novembre 2025  
**Dernière mise à jour** : Novembre 2025

