#!/bin/bash
"""
🚀 Script d'installation ComfyUI + SDXL + ControlNet
Installation complète pour génération IA hyper-intelligente
"""

set -e

echo "🧠 Installation ComfyUI + SDXL + ControlNet pour Arkalia-LUNA"
echo "=============================================================="

# Vérification Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 non trouvé. Installation requise."
    exit 1
fi

# Création du dossier ComfyUI
echo "📁 Création du dossier ComfyUI..."
mkdir -p comfyui
cd comfyui

# Clonage ComfyUI
echo "📥 Clonage ComfyUI..."
if [ ! -d ".git" ]; then
    git clone https://github.com/comfyanonymous/ComfyUI.git .
else
    echo "✅ ComfyUI déjà cloné, mise à jour..."
    git pull
fi

# Installation des dépendances
echo "📦 Installation des dépendances..."
pip install -r requirements.txt

# Installation des modèles SDXL
echo "🎨 Installation des modèles SDXL..."
mkdir -p models/checkpoints
mkdir -p models/controlnet
mkdir -p models/loras
mkdir -p models/upscale_models

# Téléchargement SDXL Base
echo "⬇️ Téléchargement SDXL Base..."
if [ ! -f "models/checkpoints/sd_xl_base_1.0.safetensors" ]; then
    wget -O models/checkpoints/sd_xl_base_1.0.safetensors \
        "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors"
fi

# Téléchargement SDXL Refiner
echo "⬇️ Téléchargement SDXL Refiner..."
if [ ! -f "models/checkpoints/sd_xl_refiner_1.0.safetensors" ]; then
    wget -O models/checkpoints/sd_xl_refiner_1.0.safetensors \
        "https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors"
fi

# Téléchargement ControlNet Canny
echo "⬇️ Téléchargement ControlNet Canny..."
if [ ! -f "models/controlnet/sd_xl_canny.safetensors" ]; then
    wget -O models/controlnet/sd_xl_canny.safetensors \
        "https://huggingface.co/diffusers/controlnet-canny-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors"
fi

# Téléchargement ControlNet Depth
echo "⬇️ Téléchargement ControlNet Depth..."
if [ ! -f "models/controlnet/sd_xl_depth.safetensors" ]; then
    wget -O models/controlnet/sd_xl_depth.safetensors \
        "https://huggingface.co/diffusers/controlnet-depth-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors"
fi

# Téléchargement RealESRGAN
echo "⬇️ Téléchargement RealESRGAN..."
if [ ! -f "models/upscale_models/RealESRGAN_x4plus.pth" ]; then
    wget -O models/upscale_models/RealESRGAN_x4plus.pth \
        "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth"
fi

# Installation des extensions utiles
echo "🔌 Installation des extensions..."
mkdir -p custom_nodes

# ComfyUI Manager
if [ ! -d "custom_nodes/ComfyUI-Manager" ]; then
    git clone https://github.com/ltdrdata/ComfyUI-Manager.git custom_nodes/ComfyUI-Manager
fi

# Installation des extensions
cd custom_nodes/ComfyUI-Manager
pip install -r requirements.txt
cd ../..

# Création du script de lancement
echo "📝 Création du script de lancement..."
cat > launch_comfyui.sh << 'EOF'
#!/bin/bash
echo "🚀 Lancement ComfyUI pour Arkalia-LUNA"
python main.py --listen 0.0.0.0 --port 8188 --output ../exports-hyper-ai
EOF

chmod +x launch_comfyui.sh

# Test de l'installation
echo "🧪 Test de l'installation..."
python -c "
import torch
print(f'✅ PyTorch version: {torch.__version__}')
print(f'✅ CUDA disponible: {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'✅ GPU: {torch.cuda.get_device_name(0)}')
"

echo ""
echo "🎉 Installation ComfyUI terminée avec succès !"
echo ""
echo "📋 Prochaines étapes :"
echo "1. Lancez ComfyUI : ./launch_comfyui.sh"
echo "2. Ouvrez http://localhost:8188 dans votre navigateur"
echo "3. Testez la génération avec le workflow Arkalia-LUNA"
echo ""
echo "🧠 ComfyUI + SDXL + ControlNet prêt pour la génération hyper-intelligente !"
