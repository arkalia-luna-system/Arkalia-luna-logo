# 🧠 ComfyUI + Hyper-AI Generator

<div align="center">

**Génération IA Ultra-Intelligente avec ComfyUI + SDXL + ControlNet**

*Arkalia-LUNA Logo Generator*

</div>

---

## 📋 Vue d'Ensemble

<div align="center">

Le générateur **Hyper-AI** utilise ComfyUI, SDXL et ControlNet pour créer des logos d'une qualité professionnelle exceptionnelle avec une intelligence artificielle avancée.

**✅ Statut** : **FONCTIONNEL** - ComfyUI opérationnel, modèles installés, génération testée avec succès

</div>

### 🎨 Exemple de Logo Généré

<div align="center">

**Logo généré avec ComfyUI - Variante "Serenity"**

![Logo ComfyUI Exemple](images/comfyui-logo-exemple.png)

*Prompt : "cosmic sphere, neural network, glowing orb, calm blue and cyan colors, serene atmosphere, professional logo design, minimalist, high quality"*

*Modèle : SD 1.5 FP16 | Taille : 512x512 | Date : Novembre 2025*

</div>

### 🎯 Navigation Rapide

<div align="center">

| Section | Description |
|:-------:|:-----------:|
| **[🚀 Installation](#-installation)** | Installer ComfyUI et les modèles |
| **[🎯 Utilisation](#-utilisation)** | Démarrer et gérer ComfyUI |
| **[🎨 Générer un Logo](#-générer-un-logo-avec-comfyui-interface-web)** | ⭐ **Guide étape par étape** |
| **[🔧 Configuration](#-configuration)** | Workflows et modèles |
| **[✅ Tests](#-tests)** | Tester la génération |

</div>

### 🎯 À Quoi Sert ComfyUI ?

**ComfyUI** est une interface graphique avancée pour la génération d'images par IA. Dans Arkalia-LUNA, il sert à :

1. **🎨 Génération de logos ultra-réalistes** : Créer des logos avec une qualité professionnelle maximale, comparable aux outils commerciaux modernes (MidJourney, DALL-E, etc.)

2. **🔧 Workflows personnalisables** : Construire des pipelines de génération visuels et modulaires via une interface graphique intuitive

3. **🚀 Intégration SDXL** : Utiliser les modèles Stable Diffusion XL pour une qualité supérieure (résolution jusqu'à 1024x1024)

4. **🎯 ControlNet** : Contrôler précisément la génération avec des masques, des guides de profondeur et des contours

5. **🔌 API REST** : Intégrer la génération IA dans Arkalia-LUNA via l'API ComfyUI pour automatisation complète

6. **⚡ Performance** : Utiliser l'accélération GPU (CUDA/MPS) pour des générations rapides

**En résumé** : ComfyUI transforme Arkalia-LUNA d'un générateur SVG classique en un système de génération IA professionnel, capable de créer des logos d'une qualité comparable aux outils commerciaux modernes, tout en restant **local, gratuit et open-source**.

### 🤔 ComfyUI vs Inkscape vs Figma

<div align="center">

| Caractéristique | ComfyUI | Inkscape | Figma |
|:---------------:|:-------:|:--------:|:-----:|
| **Type** | Génération IA | Design vectoriel | Design collaboratif |
| **Méthode** | Prompts + Workflows | Dessin manuel | Design manuel |
| **Création** | Automatique par IA | Manuelle | Manuelle |
| **Format** | Raster (PNG/JPG) | Vectoriel (SVG) | Vectoriel (SVG) |
| **Apprentissage** | Workflows visuels | Techniques de dessin | Interface design |
| **Usage** | Génération rapide | Design précis | Design collaboratif |

</div>

**Différences clés** :

- **Inkscape/Figma** : Vous dessinez manuellement, vous contrôlez chaque élément, vous créez vous-même
- **ComfyUI** : Vous créez des workflows visuels (comme des nœuds connectés), l'IA génère l'image selon vos prompts et paramètres

**Exemple concret** :
- **Inkscape** : Vous dessinez un cercle, vous ajoutez des gradients, vous positionnez les éléments → Résultat : Logo SVG que vous avez créé manuellement
- **ComfyUI** : Vous créez un workflow "Prompt → SDXL → ControlNet → Post-processing" → Résultat : Logo généré par IA selon votre description

**Dans Arkalia-LUNA** :
- Les générateurs SVG (default, ultimate, etc.) = Création manuelle programmée (comme Inkscape automatisé)
- Le générateur Hyper-AI avec ComfyUI = Génération IA (comme MidJourney mais local)

### 🎨 Workflow Hyper-AI

```mermaid
flowchart LR
    A[🎨 Prompt] --> B[🧠 ComfyUI]
    B --> C[📐 SDXL Base]
    C --> D[🎯 ControlNet]
    D --> E[✨ Post-Processing]
    E --> F[🌙 Logo Final]
    
    style A fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style B fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    style C fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    style D fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style E fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    style F fill:#e0f2f1,stroke:#004d40,stroke-width:3px
```

### **Caractéristiques Principales**

<div align="center">

| Fonctionnalité | Description | Statut |
|:-------------:|:-----------:|:------:|
| **ComfyUI** | Interface de workflow pour génération IA | ✅ Installé et fonctionnel |
| **SDXL** | Modèle Stable Diffusion XL haute qualité | ✅ Installé et testé |
| **SD 1.5 FP16** | Modèle SD 1.5 optimisé | ✅ Installé et testé |
| **ControlNet** | Contrôle précis de la génération | ✅ Installé (Canny + Depth) |
| **Hyper-AI Generator** | Générateur intégré Arkalia-LUNA | ✅ Fonctionnel |
| **Génération de logos** | Testée avec succès | ✅ Opérationnel |

</div>

---

## 🚀 Installation

### 📋 Prérequis

<div align="center">

| Prérequis | Version | Description | Statut |
|:---------:|:-------:|:-----------:|:------:|
| **Python** | 3.8+ | Version Python requise | ✅ |
| **PyTorch** | Dernière | Avec CUDA si GPU disponible | ✅ |
| **Espace disque** | 10GB+ | Pour les modèles SDXL | ✅ |
| **RAM** | 8GB+ | Mémoire recommandée | ✅ |
| **GPU** | Optionnel | CUDA/MPS pour accélération | ⚠️ |

</div>

### ⚡ Méthodes d'Installation

<div align="center">

| Méthode | Commande | Avantages | Recommandé |
|:-------:|:--------:|:---------:|:----------:|
| **Automatique** | `bash scripts/install_comfyui.sh` | ✅ Rapide, tout-en-un | ⭐ Oui |
| **Manuelle** | Étapes ci-dessous | ✅ Contrôle total | ⚠️ Avancé |

</div>

### 🔧 Installation Automatique

<div align="center">

**Méthode recommandée pour la plupart des utilisateurs**

</div>

```bash
# Depuis la racine du projet
cd /Volumes/T7/logo/arkalia-luna-logo
source arkalia-luna-env/bin/activate
bash scripts/install_comfyui.sh
```

### 🔨 Installation Manuelle

```bash
# 1. Cloner ComfyUI (déjà fait si install_comfyui.sh exécuté)
cd comfyui
git clone https://github.com/comfyanonymous/ComfyUI.git .

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Télécharger les modèles SDXL
mkdir -p models/checkpoints
wget -O models/checkpoints/sd_xl_base_1.0.safetensors \
    "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors"

# 4. Télécharger ControlNet
mkdir -p models/controlnet
wget -O models/controlnet/sd_xl_canny.safetensors \
    "https://huggingface.co/diffusers/controlnet-canny-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors"
```

---

## 🎯 Utilisation

### 1️⃣ Démarrer ComfyUI

#### 📋 Comparaison des Méthodes

<div align="center">

| Méthode | Commande | Usage | Avantages |
|:-------:|:--------:|:-----:|:---------:|
| **Script automatique** | `bash scripts/start_comfyui.sh` | Production | ✅ Gestion complète |
| **Script de lancement** | `./launch_comfyui.sh` | Développement | ✅ Simple |
| **Arrière-plan** | `nohup python main.py &` | Serveur | ✅ Détaché |
| **Manuel** | `python main.py` | Debug | ✅ Contrôle total |

</div>

#### 🚀 Méthode 1 : Script Automatique (Recommandé)

<div align="center">

**⭐ Méthode recommandée pour production**

</div>

```bash
cd /Volumes/T7/logo/arkalia-luna-logo
bash scripts/start_comfyui.sh
```

<div align="center">

| Fonctionnalité | Description | Statut |
|:--------------:|:-----------:|:------:|
| **Vérification installation** | Vérifie que ComfyUI est installé | ✅ |
| **Vérification port** | Vérifie que le port est libre | ✅ |
| **Démarrage arrière-plan** | Démarre ComfyUI en background | ✅ |
| **Gestion PID** | Crée un fichier PID pour gestion | ✅ |
| **Vérification réponse** | Vérifie que ComfyUI répond | ✅ |

</div>

**Arrêter ComfyUI** :
```bash
bash scripts/stop_comfyui.sh
```

#### 🔧 Méthode 2 : Script de Lancement

```bash
cd /Volumes/T7/logo/arkalia-luna-logo
source arkalia-luna-env/bin/activate
cd comfyui
./launch_comfyui.sh
```

#### 🔄 Méthode 3 : En Arrière-Plan (Manuel)

```bash
cd /Volumes/T7/logo/arkalia-luna-logo
source arkalia-luna-env/bin/activate
cd comfyui
nohup python main.py --listen 0.0.0.0 --port 8188 --output ../exports-hyper-ai > ../logs/comfyui.log 2>&1 &
```

#### 🛠️ Méthode 4 : Manuellement (Développement)

```bash
cd comfyui
python main.py --listen 0.0.0.0 --port 8188 --output ../exports-hyper-ai
```

**ComfyUI sera accessible sur** : http://localhost:8188

**⚠️ Note** : Si le port 8188 est déjà utilisé, vous pouvez changer le port :
```bash
python main.py --listen 0.0.0.0 --port 8189 --output ../exports-hyper-ai
```

**Vérifier que ComfyUI fonctionne** :
```bash
curl http://localhost:8188/
# Doit retourner HTTP 200

# Ou ouvrir dans le navigateur : http://localhost:8188
```

**✅ ComfyUI est maintenant accessible !**

**🎨 Interface ComfyUI** :
ComfyUI a probablement ouvert automatiquement une fenêtre de navigateur avec l'interface graphique. C'est **normal** ! Cette interface vous permet de :
- ✅ Créer des workflows visuels de génération IA
- ✅ Tester les modèles SDXL et ControlNet
- ✅ Générer des images avec des prompts personnalisés
- ✅ Utiliser l'API pour intégration avec Arkalia-LUNA

**Interface accessible sur** : http://localhost:8188

### 🎛️ Gestion de ComfyUI

<div align="center">

| Action | Commande | Description |
|:------:|:--------:|:-----------:|
| **Démarrer** | `bash scripts/start_comfyui.sh` | Démarre ComfyUI |
| **Arrêter** | `bash scripts/stop_comfyui.sh` | Arrête ComfyUI proprement |
| **Vérifier statut** | `bash scripts/check_comfyui.sh` | ⭐ **RECOMMANDÉ** - Vérification complète |
| **Vérifier logs** | `tail -f logs/comfyui.log` | Affiche les logs en temps réel |
| **Vérifier manuellement** | `lsof -ti:8188` | Vérifie le port (doit retourner PID) |

</div>

### 🔍 Comment Vérifier que ComfyUI Fonctionne ?

#### 📋 Méthodes de Vérification

<div align="center">

| Méthode | Commande | Avantages | Recommandé |
|:-------:|:--------:|:---------:|:----------:|
| **Script automatique** | `bash scripts/check_comfyui.sh` | ✅ Vérification complète | ⭐ Oui |
| **Vérification manuelle** | Commandes ci-dessous | ✅ Contrôle détaillé | ⚠️ Avancé |
| **Interface web** | http://localhost:8188 | ✅ Visuel | ✅ Simple |

</div>

#### 1️⃣ Script Automatique (Recommandé)

<div align="center">

**⭐ Méthode la plus simple et complète**

</div>

```bash
bash scripts/check_comfyui.sh
```

<div align="center">

| Vérification | Description | Statut |
|:------------:|:-----------:|:------:|
| **Processus** | ComfyUI est actif | ✅ |
| **Port** | Port 8188 utilisé | ✅ |
| **HTTP** | Interface répond (HTTP 200) | ✅ |
| **Logs** | Logs accessibles | ✅ |

</div>

#### 2️⃣ Vérification Manuelle

```bash
# 1. Vérifier le processus
ps aux | grep comfyui | grep -v grep

# 2. Vérifier le port
lsof -ti:8188

# 3. Vérifier HTTP
curl http://localhost:8188/
# Doit retourner du HTML (code 200)

# 4. Ouvrir dans le navigateur
open http://localhost:8188  # macOS
# ou simplement : http://localhost:8188
```

#### 3️⃣ Interface Web

<div align="center">

**Ouvrez votre navigateur** : **http://localhost:8188**

</div>

<div align="center">

| Élément | Description | Statut |
|:-------:|:-----------:|:------:|
| **Interface graphique** | Nœuds (blocs connectés) | ✅ Visible |
| **Espace de travail** | Création de workflows visuels | ✅ Disponible |
| **Menus modèles** | Chargement de modèles | ✅ Accessible |
| **Outils prompts** | Création de prompts et génération | ✅ Fonctionnel |

</div>

**💡 Comment utiliser l'interface** :
1. **Créer un workflow** : Glissez-déposez des nœuds (Load Checkpoint, Text Prompt, etc.)
2. **Connecter les nœuds** : Reliez-les pour créer un pipeline de génération
3. **Configurer les paramètres** : Entrez votre prompt, choisissez le modèle
4. **Générer** : Cliquez sur "Queue Prompt" pour lancer la génération
5. **Résultat** : L'image générée apparaît dans l'interface

**C'est comme créer un schéma visuel** qui dit à l'IA comment générer votre logo, plutôt que de le dessiner vous-même.

**💡 Astuce** : Si vous ne voulez pas que le navigateur s'ouvre automatiquement, utilisez :
```bash
python main.py --listen 0.0.0.0 --port 8188 --output ../exports-hyper-ai --disable-auto-launch
```

### **2. Utiliser le Générateur Hyper-AI**

<div align="center">

**⭐ Méthode recommandée : Tout est automatique**

</div>

#### **🤔 Où Faire le Prompt ?**

<div align="center">

| Méthode | Où faire le prompt | Avantages | Recommandé |
|:-------:|:------------------:|:---------:|:----------:|
| **Via Arkalia-LUNA** | Dans votre projet Python | ✅ Automatique, workflow complet | ⭐ **OUI** |
| **Via ComfyUI direct** | Dans l'interface web | ✅ Contrôle total, expérimentation | ⚠️ Avancé |

</div>

**💡 Réponse courte** : **Dans votre projet Arkalia-LUNA !** Le prompt est construit automatiquement selon la variante émotionnelle.

#### **📋 Via CLI (Recommandé)**

```bash
source arkalia-luna-env/bin/activate

# Génération automatique
# Le prompt est construit automatiquement selon la variante
python -m src.cli generate \
    --variant serenity \
    --generator hyper_ai \
    --size 512
```

**Comment ça marche ?**

1. Vous spécifiez la variante (`serenity`, `power`, `mystery`, etc.)
2. Arkalia-LUNA construit automatiquement :
   - Le prompt selon la variante émotionnelle
   - Le workflow ComfyUI complet
   - Les paramètres (steps, CFG, etc.)
3. ComfyUI génère l'image via l'API
4. Le logo est sauvegardé dans `exports-hyper-ai/`

**Vous n'avez rien à faire dans ComfyUI !** 🎉

#### **📋 Via API Python**

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

#### **⚠️ Utilisation Directe de ComfyUI (Avancé)**

Si vous voulez utiliser ComfyUI directement dans l'interface web, vous devez créer un workflow complet.

**Erreur courante** : "Prompt has no outputs" = Workflow incomplet.

**Solution** : Voir le guide complet : `docs/GUIDE_COMFYUI_UTILISATION.md`

**Workflow minimum requis** :
- CheckpointLoaderSimple (modèle)
- CLIPTextEncode (prompt positif)
- CLIPTextEncode (prompt négatif)
- EmptyLatentImage (image latente)
- KSampler (génération)
- VAEDecode (décodage)
- SaveImage (sauvegarde)

### **3. Générer Toutes les Variantes**

```python
from src.hyper_ai_generator import HyperAIGenerator

generator = HyperAIGenerator()
all_logos = generator.generate_all_hyper_variants(size=200)

for logo_path in all_logos:
    print(f"✅ {logo_path}")
```

---

## 🎨 Générer un Logo avec ComfyUI (Interface Web)

### **📋 Étape par Étape - Workflow Déjà Chargé**

Si vous voyez déjà un workflow dans ComfyUI (comme l'image de la bouteille), voici comment générer votre logo :

#### **1. Modifier le Prompt Positif**

1. **Trouvez le nœud `CLIP Text Encode (Prompt)`** (celui avec le texte "beautiful scenery nature glass bottle...")
2. **Cliquez sur la zone de texte**
3. **Remplacez par votre description de logo** :

**Exemple pour logo cosmique "Serenity"** :
```
cosmic sphere, neural network, glowing orb, calm blue and cyan colors, 
serene atmosphere, professional logo design, minimalist, high quality, 
luminous energy veins, central crystal core, abstract logo, 
geometric patterns, clean background
```

**Exemples par variante émotionnelle** :

| Variante | Prompt Exemple |
|:--------:|:--------------:|
| **Serenity** | `cosmic sphere, calm blue and cyan colors, peaceful energy, serene atmosphere, professional logo, minimalist` |
| **Power** | `cosmic sphere, vibrant red and orange, powerful energy, dynamic, professional logo, bold, energetic` |
| **Mystery** | `cosmic sphere, deep purple and dark blue, mysterious energy, enigmatic, professional logo, dark, mystical` |
| **Awakening** | `cosmic sphere, bright yellow and gold, awakening energy, radiant, professional logo, luminous, vibrant` |

#### **2. Modifier le Prompt Négatif (Optionnel)**

1. **Trouvez le deuxième nœud `CLIP Text Encode (Prompt)`** (celui avec "text, watermark")
2. **Améliorez-le** :
```
text, watermark, signature, blurry, low quality, distorted, 
ugly, bad anatomy, extra limbs, duplicate, poorly drawn, 
noise, artifacts, jpeg artifacts
```

#### **3. Choisir le Modèle (Important !)**

1. **Cliquez sur le nœud `Charger Point de Contrôle`** (Load Checkpoint)
2. **Dans le menu déroulant `ckpt_name`**, choisissez :
   - **`sd_xl_base_1.0.safetensors`** ⭐ **Recommandé pour logos** (meilleure qualité)
   - **`v1-5-pruned-emaonly-fp16.safetensors`** (plus rapide, qualité correcte)

**💡 Astuce** : SDXL donne de meilleurs résultats pour les logos professionnels.

#### **4. Ajuster la Taille (Optionnel)**

1. **Cliquez sur le nœud `Image Latente Vide`** (Empty Latent Image)
2. **Modifiez** :
   - `largeur` (width) : `512` ou `1024` (1024 = meilleure qualité mais plus lent)
   - `hauteur` (height) : `512` ou `1024`
   - `taille_du_lot` (batch_size) : `1`

**💡 Pour les logos** : 512x512 est suffisant et plus rapide.

#### **5. Paramètres de Génération (Optionnel)**

1. **Cliquez sur le nœud `KSampler`**
2. **Ajustez si besoin** :
   - `seed` : `0` ou "randomize" (pour varier les résultats)
   - `steps` : `20-30` (plus = meilleur mais plus lent)
   - `cfg` : `7.0-8.0` (force du prompt)
   - `sampler_name` : `euler` ou `euler_ancestral`
   - `scheduler` : `normal` ou `simple`

**Valeurs recommandées pour logos** :
- `steps` : `25`
- `cfg` : `7.5`
- `sampler_name` : `euler`
- `scheduler` : `normal`

#### **6. Générer le Logo**

1. **Cliquez sur le bouton "Exécuter"** (Queue Prompt) en bas de l'interface
2. **Attendez** : 10-60 secondes selon la taille et le modèle
3. **L'image apparaît** dans le nœud `Enregistrer Image` (Save Image)

#### **7. Sauvegarder le Logo**

1. **Cliquez sur l'image** dans le nœud `Enregistrer Image` pour l'agrandir
2. **Clic droit** → "Save Image As..." pour télécharger
3. **Ou** : L'image est automatiquement sauvegardée dans `exports-hyper-ai/`

---

### **🔄 Générer Plusieurs Variantes**

Pour générer plusieurs logos avec des variations :

1. **Changez le `seed`** dans KSampler :
   - `0`, `1`, `42`, `123`, `999`, etc.
   - Ou cliquez sur "randomize" pour un seed aléatoire

2. **Modifiez légèrement le prompt** :
   - Ajoutez des mots-clés : `glowing`, `neon`, `geometric`, `minimalist`
   - Changez les couleurs : `blue`, `purple`, `gold`, `red`

3. **Cliquez "Exécuter"** à nouveau

---

### **💡 Astuces pour Meilleurs Résultats**

#### **Pour Améliorer la Qualité**

- ✅ Utilisez **SDXL** (`sd_xl_base_1.0.safetensors`)
- ✅ Augmentez les **steps** à 30-50
- ✅ Utilisez un **prompt détaillé** avec des mots-clés professionnels
- ✅ Ajoutez : `high quality, professional, detailed, 4k, 8k, logo design`

#### **Pour Accélérer**

- ✅ Utilisez **512x512** au lieu de 1024x1024
- ✅ Réduisez les **steps** à 15-20
- ✅ Utilisez **SD 1.5** (`v1-5-pruned-emaonly-fp16.safetensors`)

#### **Pour Varier les Résultats**

- ✅ Changez le **seed** : `0`, `1`, `42`, `123`, etc.
- ✅ Ajustez le **CFG** : Plus haut = suit mieux le prompt, plus bas = plus créatif
- ✅ Modifiez les **couleurs** dans le prompt

---

### **⚠️ Problèmes Courants**

#### **"Model not found"**

**Solution** :
1. Vérifiez que le modèle est dans `comfyui/models/checkpoints/`
2. Redémarrez ComfyUI : `bash scripts/stop_comfyui.sh && bash scripts/start_comfyui.sh`
3. Rafraîchissez l'interface (F5)

#### **Génération très lente**

**Solution** :
- Réduisez la taille (512x512)
- Réduisez les steps (15-20)
- Utilisez SD 1.5 au lieu de SDXL

#### **Résultat pas satisfaisant**

**Solution** :
- Améliorez le prompt (plus de détails)
- Augmentez les steps (30-50)
- Changez le seed pour essayer d'autres variations
- Utilisez SDXL pour meilleure qualité

---

## 🔧 Configuration

### 📋 Workflow Templates

<div align="center">

**Templates de workflow ComfyUI pré-configurés**

</div>

<div align="center">

| Template | Description | Usage | Statut |
|:--------:|:-----------:|:-----:|:------:|
| **cosmic_sphere** | Sphère cosmique avec réseaux neuronaux | ✅ Disponible | ✅ |
| **neural_network** | Réseau neuronal complexe | ✅ Disponible | ✅ |
| **crystal_core** | Cœur cristallin central | ✅ Disponible | ✅ |

</div>

**Emplacement** : `comfyui/workflows/`

### 🤖 Modèles Disponibles

| Modèle | Description | Taille | Statut |
|:------:|:-----------:|:------:|:------:|
| **SDXL Base** | Modèle principal SDXL | ~7GB | ✅ Installé |
| **SDXL Refiner** | Raffinement haute qualité | ~7GB | ✅ Installé |
| **SD 1.5 FP16** | Modèle SD 1.5 optimisé | ~2GB | ✅ Installé |
| **ControlNet Canny** | Contrôle par contours | ~5GB | ✅ Installé |
| **ControlNet Depth** | Contrôle par profondeur | ~5GB | ✅ Installé |
| **RealESRGAN** | Upscaling 4x | ~100MB | ⚠️ À télécharger |

### 📥 Installation de Modèles Manquants

#### **🚀 Solution Automatique (Recommandé)**

Si vous avez téléchargé des modèles dans Téléchargements :

```bash
bash scripts/install_models_comfyui.sh
```

Ce script :
- ✅ Cherche les modèles dans `~/Downloads`
- ✅ Les déplace automatiquement vers les bons dossiers
- ✅ Affiche les modèles déjà installés

#### **📋 Installation Manuelle**

**Emplacements des modèles** :

| Type de Modèle | Dossier | Extensions |
|:--------------:|:------:|:----------:|
| **Checkpoints** | `comfyui/models/checkpoints/` | `.safetensors`, `.ckpt` |
| **ControlNet** | `comfyui/models/controlnet/` | `.safetensors`, `.ckpt` |
| **VAE** | `comfyui/models/vae/` | `.safetensors`, `.ckpt`, `.pt` |
| **LoRA** | `comfyui/models/loras/` | `.safetensors`, `.ckpt` |
| **Upscale** | `comfyui/models/upscale_models/` | `.pth` |

**Étapes** :
1. Téléchargez le modèle
2. Déplacez-le dans le bon dossier :
   ```bash
   # Exemple : Checkpoint
   mv ~/Downloads/sd_xl_base_1.0.safetensors comfyui/models/checkpoints/
   ```
3. Redémarrez ComfyUI :
   ```bash
   bash scripts/stop_comfyui.sh && bash scripts/start_comfyui.sh
   ```
4. Rafraîchissez l'interface web (F5)

#### **🔍 Vérifier les Modèles Installés**

```bash
# Checkpoints
ls -lh comfyui/models/checkpoints/

# ControlNet
ls -lh comfyui/models/controlnet/
```

Ou utilisez le script :
```bash
bash scripts/install_models_comfyui.sh
```

---

## 🎨 Workflows ComfyUI

### **Workflow Cosmic Sphere**

Génère une sphère cosmique avec :
- Réseaux neuronaux énergétiques
- Cœur cristallin central
- Halo lumineux
- Veines énergétiques

### **Workflow Neural Network**

Génère un réseau neuronal avec :
- Connexions complexes
- Flux de données
- Effets lumineux
- Ambiance technologique

---

## 📊 Performance

### **Temps de Génération**

| Configuration | Temps moyen | GPU requis |
|:------------:|:-----------:|:----------:|
| **CPU uniquement** | 5-10 minutes | ❌ |
| **GPU (NVIDIA)** | 30-60 secondes | ✅ |
| **GPU (AMD)** | 1-2 minutes | ✅ |

### **Ressources Requises**

- **RAM** : 8GB minimum (16GB recommandé)
- **VRAM** : 6GB minimum pour SDXL
- **Stockage** : 20GB pour modèles complets

---

## 🐛 Dépannage

### ⚠️ Problèmes Courants

<div align="center">

| Problème | Symptôme | Solution | Statut |
|:--------:|:--------:|:--------:|:------:|
| **ComfyUI ne démarre pas** | Erreur au démarrage | Vérifier dépendances | ✅ |
| **Modèles manquants** | Erreur de chargement | Télécharger modèles | ✅ |
| **Erreur GPU** | CUDA non disponible | Installer PyTorch CUDA | ✅ |
| **Port occupé** | Port 8188 utilisé | Changer le port | ✅ |

</div>

#### 1️⃣ ComfyUI ne démarre pas

<div align="center">

**Symptôme** : Erreur au démarrage ou crash immédiat

</div>

```bash
# Vérifier les dépendances
cd comfyui
pip install -r requirements.txt

# Vérifier Python
python --version  # Doit être 3.8+

# Vérifier PyTorch
python -c "import torch; print(torch.__version__)"
```

#### 2️⃣ Modèles manquants

<div align="center">

**Symptôme** : `ModelNotFoundError` ou erreur de chargement

</div>

```bash
# Vérifier les modèles installés
ls -lh comfyui/models/checkpoints/
ls -lh comfyui/models/controlnet/

# Télécharger les modèles manquants
bash scripts/install_comfyui.sh
```

#### 3️⃣ Erreur GPU

<div align="center">

**Symptôme** : `CUDA not available` ou utilisation CPU uniquement

</div>

```bash
# Vérifier CUDA
python -c "import torch; print(torch.cuda.is_available())"

# Si False, installer PyTorch avec CUDA
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

#### 4️⃣ Port Déjà Utilisé

<div align="center">

**Symptôme** : `Address already in use` sur le port 8188

</div>

```bash
# Solution : Utiliser un autre port
python comfyui/main.py --port 8189

# Ou arrêter le processus existant
bash scripts/stop_comfyui.sh
```

---

## 📚 Ressources

### **Documentation ComfyUI**

- **GitHub** : https://github.com/comfyanonymous/ComfyUI
- **Documentation** : https://github.com/comfyanonymous/ComfyUI/wiki
- **Exemples** : `comfyui/script_examples/`

### **Modèles SDXL**

- **HuggingFace** : https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
- **ControlNet** : https://huggingface.co/diffusers/controlnet-canny-sdxl-1.0

---

## ✅ Tests

### 🧪 Tests Unitaires

<div align="center">

| Test | Description | Statut | Résultat |
|:----:|:-----------:|:------:|:---------:|
| **test_hyper_ai_generator.py** | Tests du générateur Hyper-AI | ✅ | 6 tests passants |

</div>

```bash
source arkalia-luna-env/bin/activate
pytest tests/test_hyper_ai_generator.py -v
```

**Résultats attendus** : 6 tests passants ✅

### 🔗 Test d'Intégration

<div align="center">

**Workflow de test d'intégration complet**

</div>

```bash
# 1. Démarrer ComfyUI
bash scripts/start_comfyui.sh

# 2. Tester la génération
python -m src.cli generate --variant serenity --generator hyper_ai --size 200

# 3. Vérifier le résultat
ls -lh exports-hyper-ai/
```

<div align="center">

| Étape | Action | Vérification |
|:-----:|:------:|:------------:|
| **1** | Démarrer ComfyUI | `bash scripts/check_comfyui.sh` |
| **2** | Générer logo | Vérifier fichier créé |
| **3** | Vérifier résultat | `ls -lh exports-hyper-ai/` |

</div>

---

## 🎯 Prochaines Étapes

<div align="center">

| Étape | Description | Statut | Priorité |
|:-----:|:-----------:|:------:|:--------:|
| **Installation** | ComfyUI installé | ✅ | - |
| **Tests** | Tests unitaires créés | ✅ | - |
| **Modèles** | Télécharger SDXL et ControlNet | ⚠️ | 🚨 Haute |
| **Production** | Démarrer ComfyUI en production | ⚠️ | ⚠️ Moyenne |
| **Optimisation** | Optimiser les workflows | ⚠️ | ⚠️ Moyenne |

</div>

---

**📚 Documentation mise à jour - Novembre 2025**

