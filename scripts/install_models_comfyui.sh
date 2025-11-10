#!/bin/bash
# 🔧 Script d'installation de modèles ComfyUI
# Déplace les modèles téléchargés vers les bons dossiers

set -e

# Couleurs
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

COMFYUI_DIR="comfyui"
DOWNLOADS_DIR="$HOME/Downloads"

echo -e "${BLUE}🔧 Installation de modèles ComfyUI${NC}"
echo "=========================================="
echo ""

# Vérifier que ComfyUI existe
if [ ! -d "$COMFYUI_DIR" ]; then
    echo -e "${RED}❌ ComfyUI non trouvé dans $COMFYUI_DIR${NC}"
    echo "   Lancez d'abord : bash scripts/install_comfyui.sh"
    exit 1
fi

# Créer les dossiers nécessaires
echo -e "${BLUE}📁 Création des dossiers de modèles...${NC}"
mkdir -p "$COMFYUI_DIR/models/checkpoints"
mkdir -p "$COMFYUI_DIR/models/controlnet"
mkdir -p "$COMFYUI_DIR/models/vae"
mkdir -p "$COMFYUI_DIR/models/loras"
mkdir -p "$COMFYUI_DIR/models/upscale_models"
mkdir -p "$COMFYUI_DIR/models/clip"
mkdir -p "$COMFYUI_DIR/models/embeddings"

echo -e "${GREEN}✅ Dossiers créés${NC}"
echo ""

# Fonction pour déplacer un modèle
move_model() {
    local source_file="$1"
    local dest_dir="$2"
    local model_name=$(basename "$source_file")
    
    if [ -f "$source_file" ]; then
        echo -e "${YELLOW}📦 Déplacement : $model_name${NC}"
        mv "$source_file" "$dest_dir/"
        echo -e "${GREEN}   ✅ Déplacé vers $dest_dir/$model_name${NC}"
        return 0
    else
        return 1
    fi
}

# Chercher les modèles dans Téléchargements
echo -e "${BLUE}🔍 Recherche de modèles dans $DOWNLOADS_DIR...${NC}"
echo ""

FOUND_ANY=false

# Checkpoints (modèles principaux)
echo -e "${BLUE}📋 Checkpoints (modèles principaux) :${NC}"
for pattern in "*.safetensors" "*.ckpt" "*.pt" "*.pth"; do
    for file in "$DOWNLOADS_DIR"/*${pattern}; do
        if [ -f "$file" ] 2>/dev/null; then
            # Vérifier si c'est un checkpoint (gros fichiers généralement)
            size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
            if [ "$size" -gt 1000000000 ]; then  # > 1GB
                move_model "$file" "$COMFYUI_DIR/models/checkpoints"
                FOUND_ANY=true
            fi
        fi
    done
done

# ControlNet
echo ""
echo -e "${BLUE}🎯 ControlNet :${NC}"
for pattern in "*controlnet*.safetensors" "*controlnet*.ckpt" "*canny*.safetensors" "*depth*.safetensors"; do
    for file in "$DOWNLOADS_DIR"/*${pattern}; do
        if [ -f "$file" ] 2>/dev/null; then
            move_model "$file" "$COMFYUI_DIR/models/controlnet"
            FOUND_ANY=true
        fi
    done
done

# VAE
echo ""
echo -e "${BLUE}🎨 VAE :${NC}"
for pattern in "*vae*.safetensors" "*vae*.ckpt" "*vae*.pt"; do
    for file in "$DOWNLOADS_DIR"/*${pattern}; do
        if [ -f "$file" ] 2>/dev/null; then
            move_model "$file" "$COMFYUI_DIR/models/vae"
            FOUND_ANY=true
        fi
    done
done

# LoRA
echo ""
echo -e "${BLUE}🎭 LoRA :${NC}"
for pattern in "*lora*.safetensors" "*lora*.ckpt" "*lora*.pt"; do
    for file in "$DOWNLOADS_DIR"/*${pattern}; do
        if [ -f "$file" ] 2>/dev/null; then
            move_model "$file" "$COMFYUI_DIR/models/loras"
            FOUND_ANY=true
        fi
    done
done

# Upscale
echo ""
echo -e "${BLUE}🔍 Upscale :${NC}"
for pattern in "*esrgan*.pth" "*upscale*.pth" "*real*.pth"; do
    for file in "$DOWNLOADS_DIR"/*${pattern}; do
        if [ -f "$file" ] 2>/dev/null; then
            move_model "$file" "$COMFYUI_DIR/models/upscale_models"
            FOUND_ANY=true
        fi
    done
done

# Afficher les modèles déjà installés
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📊 Modèles actuellement installés :${NC}"
echo ""

# Checkpoints
echo -e "${GREEN}📋 Checkpoints :${NC}"
if [ -n "$(ls -A $COMFYUI_DIR/models/checkpoints/*.safetensors $COMFYUI_DIR/models/checkpoints/*.ckpt 2>/dev/null)" ]; then
    ls -lh "$COMFYUI_DIR/models/checkpoints"/*.{safetensors,ckpt} 2>/dev/null | awk '{print "   ✅", $9, "(" $5 ")"}'
else
    echo -e "${YELLOW}   ⚠️  Aucun checkpoint trouvé${NC}"
fi

# ControlNet
echo ""
echo -e "${GREEN}🎯 ControlNet :${NC}"
if [ -n "$(ls -A $COMFYUI_DIR/models/controlnet/*.safetensors $COMFYUI_DIR/models/controlnet/*.ckpt 2>/dev/null)" ]; then
    ls -lh "$COMFYUI_DIR/models/controlnet"/*.{safetensors,ckpt} 2>/dev/null | awk '{print "   ✅", $9, "(" $5 ")"}'
else
    echo -e "${YELLOW}   ⚠️  Aucun ControlNet trouvé${NC}"
fi

# VAE
echo ""
echo -e "${GREEN}🎨 VAE :${NC}"
if [ -n "$(ls -A $COMFYUI_DIR/models/vae/*.safetensors $COMFYUI_DIR/models/vae/*.ckpt 2>/dev/null)" ]; then
    ls -lh "$COMFYUI_DIR/models/vae"/*.{safetensors,ckpt} 2>/dev/null | awk '{print "   ✅", $9, "(" $5 ")"}'
else
    echo -e "${YELLOW}   ⚠️  Aucun VAE trouvé${NC}"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

if [ "$FOUND_ANY" = false ]; then
    echo ""
    echo -e "${YELLOW}⚠️  Aucun modèle trouvé dans $DOWNLOADS_DIR${NC}"
    echo ""
    echo -e "${BLUE}💡 Pour installer manuellement :${NC}"
    echo "   1. Téléchargez le modèle"
    echo "   2. Déplacez-le dans le bon dossier :"
    echo "      • Checkpoints → $COMFYUI_DIR/models/checkpoints/"
    echo "      • ControlNet → $COMFYUI_DIR/models/controlnet/"
    echo "      • VAE → $COMFYUI_DIR/models/vae/"
    echo "      • LoRA → $COMFYUI_DIR/models/loras/"
    echo "   3. Redémarrez ComfyUI"
else
    echo ""
    echo -e "${GREEN}✅ Modèles déplacés avec succès !${NC}"
    echo ""
    echo -e "${BLUE}💡 Prochaines étapes :${NC}"
    echo "   1. Redémarrez ComfyUI : bash scripts/stop_comfyui.sh && bash scripts/start_comfyui.sh"
    echo "   2. Rafraîchissez l'interface web (F5)"
    echo "   3. Les modèles devraient apparaître dans la liste"
fi

echo ""

