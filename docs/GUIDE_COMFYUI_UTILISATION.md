# 🎨 Guide d'Utilisation ComfyUI avec Arkalia-LUNA

<div align="center">

**Comment générer des logos avec ComfyUI : Deux méthodes simples**

</div>

---

## 🤔 Où Faire le Prompt ?

<div align="center">

| Méthode | Où faire le prompt | Avantages | Recommandé |
|:-------:|:------------------:|:---------:|:----------:|
| **Via Arkalia-LUNA** | Dans votre projet Python | ✅ Automatique, workflow complet | ⭐ **OUI** |
| **Via ComfyUI direct** | Dans l'interface web | ✅ Contrôle total, expérimentation | ⚠️ Avancé |

</div>

---

## 🚀 Méthode 1 : Via Arkalia-LUNA (Recommandé)

<div align="center">

**⭐ Méthode la plus simple : Tout est automatique**

</div>

### ✅ Avantages

- ✅ **Workflow automatique** : Arkalia-LUNA crée le workflow ComfyUI complet
- ✅ **Pas besoin de connaître ComfyUI** : Vous utilisez juste la CLI ou l'API
- ✅ **Intégration native** : Les logos sont générés directement dans votre projet
- ✅ **Gestion des variantes** : Toutes les variantes émotionnelles sont gérées

### 📋 Utilisation

#### **Via CLI**

```bash
source arkalia-luna-env/bin/activate

# Générer un logo avec Hyper-AI
python -m src.cli generate \
    --variant serenity \
    --generator hyper_ai \
    --size 512
```

#### **Via API Python**

```python
from src.hyper_ai_generator import HyperAIGenerator

# Initialisation
generator = HyperAIGenerator()

# Génération automatique
# Le prompt est construit automatiquement selon la variante
output_path = generator.generate_svg_logo(
    variant_name="serenity",  # Variante émotionnelle
    size=512
)

print(f"✅ Logo généré : {output_path}")
```

### 🎯 Comment ça marche ?

1. **Vous appelez** `generate_svg_logo()` avec une variante (serenity, power, etc.)
2. **Arkalia-LUNA construit automatiquement** :
   - Le prompt selon la variante émotionnelle
   - Le workflow ComfyUI complet
   - Les paramètres (steps, CFG, etc.)
3. **ComfyUI génère** l'image via l'API
4. **Le logo est sauvegardé** dans `exports-hyper-ai/`

**Vous n'avez rien à faire dans ComfyUI !** 🎉

---

## 🎨 Méthode 2 : Via ComfyUI Directement (Avancé)

<div align="center">

**⚠️ Pour les utilisateurs avancés qui veulent contrôler chaque détail**

</div>

### ⚠️ Votre Erreur Actuelle

L'erreur **"Prompt has no outputs"** signifie que votre workflow est incomplet.

**Problème** : Vous avez seulement un nœud `KSampler` qui n'est connecté à rien.

**Solution** : Il faut créer un workflow complet avec tous les nœuds nécessaires.

### 📋 Workflow Complet Minimum

Un workflow ComfyUI valide doit contenir :

<div align="center">

| Nœud | Rôle | Obligatoire |
|:----:|:----:|:----------:|
| **CheckpointLoaderSimple** | Charge le modèle SDXL | ✅ Oui |
| **CLIPTextEncode (positive)** | Prompt positif | ✅ Oui |
| **CLIPTextEncode (negative)** | Prompt négatif | ✅ Oui |
| **EmptyLatentImage** | Crée l'image latente | ✅ Oui |
| **KSampler** | Génère l'image | ✅ Oui |
| **VAEDecode** | Décode l'image | ✅ Oui |
| **SaveImage** | Sauvegarde l'image | ✅ Oui |

</div>

### 🔧 Comment Créer un Workflow Valide

#### **Étape 1 : Ouvrir ComfyUI**

```bash
# Vérifier que ComfyUI est démarré
bash scripts/check_comfyui.sh

# Ouvrir dans le navigateur
open http://localhost:8188
```

Vous verrez l'interface ComfyUI avec une fenêtre modale **"Commencez avec un modèle"** (Start with a model).

#### **Étape 2 : Choisir un Modèle de Départ**

Dans la fenêtre modale, vous avez plusieurs options :

<div align="center">

| Option | Description | Usage pour Logos |
|:------:|:-----------:|:----------------:|
| **Génération d'Image** | Génère des images à partir de descriptions textuelles | ⭐ **PARFAIT** pour logos |
| **Image à Image** | Transforme des images existantes | ✅ Pour modifier logos existants |
| **LoRA** | Génère avec des styles LoRA | ✅ Pour styles spécifiques |

</div>

**💡 Pour générer des logos** : Cliquez sur **"Génération d'Image"** (Image Generation).

Cela va charger automatiquement un workflow de base avec tous les nœuds nécessaires :
- CheckpointLoaderSimple
- CLIPTextEncode (positive)
- CLIPTextEncode (negative)
- EmptyLatentImage
- KSampler
- VAEDecode
- SaveImage

#### **Étape 3 : Configurer le Workflow**

**Si vous avez cliqué sur "Génération d'Image"** : Le workflow est déjà créé ! Passez directement à la configuration.

**Si vous voulez créer manuellement** :

1. **Clic droit** dans l'espace de travail → **Add Node**

2. **Ajouter les nœuds dans cet ordre** :

   ```
   CheckpointLoaderSimple
   ├─→ CLIPTextEncode (positive)
   ├─→ CLIPTextEncode (negative)
   ├─→ EmptyLatentImage
   └─→ KSampler
        └─→ VAEDecode
             └─→ SaveImage
   ```

3. **Connecter les nœuds** :

   - **CheckpointLoaderSimple** :
     - `MODEL` → **KSampler** (`model`)
     - `CLIP` → **CLIPTextEncode (positive)** (`clip`)
     - `CLIP` → **CLIPTextEncode (negative)** (`clip`)
     - `VAE` → **VAEDecode** (`vae`)

   - **CLIPTextEncode (positive)** :
     - `CONDITIONING` → **KSampler** (`positive`)

   - **CLIPTextEncode (negative)** :
     - `CONDITIONING` → **KSampler** (`negative`)

   - **EmptyLatentImage** :
     - `LATENT` → **KSampler** (`latent_image`)

   - **KSampler** :
     - `LATENT` → **VAEDecode** (`samples`)

   - **VAEDecode** :
     - `IMAGE` → **SaveImage** (`images`)

#### **Étape 4 : Configurer les Paramètres**

- **CheckpointLoaderSimple** :
  - `ckpt_name` : Choisir un modèle (ex: `sd_xl_base_1.0.safetensors`)

- **CLIPTextEncode (positive)** :
  - `text` : Votre prompt (ex: `"cosmic sphere, neural network, glowing orb, serenity colors, professional logo design"`)

- **CLIPTextEncode (negative)** :
  - `text` : Prompt négatif (ex: `"text, watermark, signature, blurry, low quality"`)

- **EmptyLatentImage** :
  - `width` : `1024`
  - `height` : `1024`
  - `batch_size` : `1`

- **KSampler** :
  - `seed` : `0` (ou "randomize")
  - `steps` : `20`
  - `cfg` : `8.0`
  - `sampler_name` : `euler`
  - `scheduler` : `simple`

#### **Étape 5 : Générer**

1. Cliquez sur **"Queue Prompt"** (en haut à droite)
2. Attendez la génération
3. L'image apparaît dans le nœud **SaveImage**

### 🎯 Exemple de Workflow JSON Complet

Si vous voulez charger un workflow existant, voici un exemple minimal :

```json
{
  "nodes": [
    {
      "id": 1,
      "type": "CheckpointLoaderSimple",
      "pos": [100, 100],
      "size": [315, 98],
      "widgets_values": ["sd_xl_base_1.0.safetensors"]
    },
    {
      "id": 2,
      "type": "CLIPTextEncode",
      "pos": [500, 100],
      "size": [400, 200],
      "widgets_values": ["cosmic sphere, neural network, glowing orb, serenity colors, professional logo design"]
    },
    {
      "id": 3,
      "type": "CLIPTextEncode",
      "pos": [500, 350],
      "size": [400, 200],
      "widgets_values": ["text, watermark, signature, blurry, low quality"]
    },
    {
      "id": 4,
      "type": "EmptyLatentImage",
      "pos": [100, 250],
      "size": [315, 106],
      "widgets_values": [1024, 1024, 1]
    },
    {
      "id": 5,
      "type": "KSampler",
      "pos": [1000, 200],
      "size": [270, 262],
      "widgets_values": [0, "randomize", 20, 8.0, "euler", "simple", 1.0]
    },
    {
      "id": 6,
      "type": "VAEDecode",
      "pos": [1300, 200],
      "size": [210, 46],
      "inputs": [{"name": "samples", "type": "LATENT", "link": 5}]
    },
    {
      "id": 7,
      "type": "SaveImage",
      "pos": [1550, 200],
      "size": [315, 270],
      "inputs": [{"name": "images", "type": "IMAGE", "link": 6}]
    }
  ],
  "links": [
    [1, 0, 5, 0],  // MODEL
    [1, 1, 2, 0],  // CLIP → positive
    [1, 1, 3, 0],  // CLIP → negative
    [1, 2, 6, 0],  // VAE
    [2, 0, 5, 1],  // positive → KSampler
    [3, 0, 5, 2],  // negative → KSampler
    [4, 0, 5, 3],  // latent → KSampler
    [5, 0, 6, 0],  // KSampler → VAEDecode
    [6, 0, 7, 0]   // VAEDecode → SaveImage
  ]
}
```

---

## 🎯 Recommandation

<div align="center">

**⭐ Utilisez la Méthode 1 (Arkalia-LUNA) pour la plupart des cas**

</div>

**Pourquoi ?**

- ✅ Plus simple : Pas besoin de connaître ComfyUI
- ✅ Automatique : Workflow complet généré automatiquement
- ✅ Intégré : Les logos sont directement dans votre projet
- ✅ Variantes : Toutes les variantes émotionnelles sont gérées

**Utilisez la Méthode 2 seulement si** :

- ⚠️ Vous voulez expérimenter avec des workflows personnalisés
- ⚠️ Vous voulez tester de nouveaux modèles
- ⚠️ Vous voulez un contrôle total sur chaque paramètre

---

## 📚 Ressources

- **Documentation ComfyUI** : https://github.com/comfyanonymous/ComfyUI
- **Guide Arkalia-LUNA** : `docs/COMFYUI.md`
- **Exemples de workflows** : `comfyui/workflows/` (si disponibles)

---

**Créé** : Novembre 2025  
**Dernière mise à jour** : Novembre 2025

