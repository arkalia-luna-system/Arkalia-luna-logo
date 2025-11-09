# 🧠 ComfyUI + Hyper-AI Generator

<div align="center">

**Génération IA Ultra-Intelligente avec ComfyUI + SDXL + ControlNet**

*Arkalia-LUNA Logo Generator*

</div>

---

## 📋 Vue d'Ensemble

Le générateur **Hyper-AI** utilise ComfyUI, SDXL et ControlNet pour créer des logos d'une qualité professionnelle exceptionnelle avec une intelligence artificielle avancée.

### **Caractéristiques Principales**

<div align="center">

| Fonctionnalité | Description | Statut |
|:-------------:|:-----------:|:------:|
| **ComfyUI** | Interface de workflow pour génération IA | ✅ Installé |
| **SDXL** | Modèle Stable Diffusion XL haute qualité | ⚠️ Partiellement installé |
| **ControlNet** | Contrôle précis de la génération | ⚠️ Partiellement installé |
| **Hyper-AI Generator** | Générateur intégré Arkalia-LUNA | ✅ Fonctionnel |

</div>

---

## 🚀 Installation

### **Prérequis**

- Python 3.8+
- PyTorch (avec CUDA si GPU disponible)
- 10GB+ d'espace disque pour les modèles

### **Installation Automatique**

```bash
# Depuis la racine du projet
cd /Volumes/T7/logo/arkalia-luna-logo
source arkalia-luna-env/bin/activate
bash scripts/install_comfyui.sh
```

### **Installation Manuelle**

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

### **1. Démarrer ComfyUI**

```bash
cd /Volumes/T7/logo/arkalia-luna-logo
source arkalia-luna-env/bin/activate
cd comfyui
./launch_comfyui.sh
```

Ou manuellement :

```bash
cd comfyui
python main.py --listen 0.0.0.0 --port 8188 --output ../exports-hyper-ai
```

**ComfyUI sera accessible sur** : http://localhost:8188

### **2. Utiliser le Générateur Hyper-AI**

#### **Via CLI**

```bash
source arkalia-luna-env/bin/activate
python -m src.cli generate --variant serenity --generator hyper_ai --size 200
```

#### **Via API Python**

```python
from src.hyper_ai_generator import HyperAIGenerator

# Initialisation
generator = HyperAIGenerator()

# Génération d'un logo
output_path = generator.generate_svg_logo(
    variant_name="serenity",
    size=200
)

print(f"Logo généré : {output_path}")
```

### **3. Générer Toutes les Variantes**

```python
from src.hyper_ai_generator import HyperAIGenerator

generator = HyperAIGenerator()
all_logos = generator.generate_all_hyper_variants(size=200)

for logo_path in all_logos:
    print(f"✅ {logo_path}")
```

---

## 🔧 Configuration

### **Workflow Templates**

Le générateur Hyper-AI utilise des templates de workflow ComfyUI pré-configurés :

- **cosmic_sphere** : Sphère cosmique avec réseaux neuronaux
- **neural_network** : Réseau neuronal complexe
- **crystal_core** : Cœur cristallin central

### **Modèles Disponibles**

| Modèle | Description | Taille | Statut |
|:------:|:-----------:|:------:|:------:|
| **SDXL Base** | Modèle principal SDXL | ~7GB | ⚠️ À télécharger |
| **SDXL Refiner** | Raffinement haute qualité | ~7GB | ⚠️ À télécharger |
| **ControlNet Canny** | Contrôle par contours | ~1GB | ⚠️ À télécharger |
| **ControlNet Depth** | Contrôle par profondeur | ~1GB | ⚠️ À télécharger |
| **RealESRGAN** | Upscaling 4x | ~100MB | ⚠️ À télécharger |

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

### **ComfyUI ne démarre pas**

```bash
# Vérifier les dépendances
cd comfyui
pip install -r requirements.txt

# Vérifier Python
python --version  # Doit être 3.8+

# Vérifier PyTorch
python -c "import torch; print(torch.__version__)"
```

### **Modèles manquants**

```bash
# Vérifier les modèles installés
ls -lh comfyui/models/checkpoints/
ls -lh comfyui/models/controlnet/

# Télécharger les modèles manquants
bash scripts/install_comfyui.sh
```

### **Erreur GPU**

```bash
# Vérifier CUDA
python -c "import torch; print(torch.cuda.is_available())"

# Si False, installer PyTorch avec CUDA
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
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

### **Tests Unitaires**

```bash
source arkalia-luna-env/bin/activate
pytest tests/test_hyper_ai_generator.py -v
```

**Résultats attendus** : 6 tests passants

### **Test d'Intégration**

```bash
# 1. Démarrer ComfyUI
cd comfyui && ./launch_comfyui.sh &

# 2. Tester la génération
python -m src.cli generate --variant serenity --generator hyper_ai --size 200

# 3. Vérifier le résultat
ls -lh exports-hyper-ai/
```

---

## 🎯 Prochaines Étapes

1. ✅ **Installation** : ComfyUI installé
2. ✅ **Tests** : Tests unitaires créés
3. ⚠️ **Modèles** : Télécharger SDXL et ControlNet
4. ⚠️ **Production** : Démarrer ComfyUI en production
5. ⚠️ **Optimisation** : Optimiser les workflows

---

**📚 Documentation mise à jour - Novembre 2025**

