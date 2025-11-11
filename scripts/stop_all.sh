#!/bin/bash
# 🛑 Script pour arrêter tous les processus Arkalia-LUNA
# Arrête ComfyUI, API FastAPI, et tous les processus liés

set -e

# Couleurs
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🛑 Arrêt de tous les processus Arkalia-LUNA${NC}"
echo "=========================================="
echo ""

# 1. Arrêter ComfyUI
echo -e "${BLUE}1. Arrêt de ComfyUI...${NC}"
if [ -f "scripts/stop_comfyui.sh" ]; then
    bash scripts/stop_comfyui.sh
else
    # Arrêt manuel
    PIDS=$(ps aux | grep -E "python.*main.py.*comfyui|comfyui" | grep -v grep | awk '{print $2}')
    if [ -n "$PIDS" ]; then
        echo "$PIDS" | xargs kill -9 2>/dev/null || true
        echo -e "${GREEN}   ✅ ComfyUI arrêté${NC}"
    else
        echo -e "${YELLOW}   ℹ️  ComfyUI non démarré${NC}"
    fi
fi

# 2. Arrêter l'API FastAPI
echo ""
echo -e "${BLUE}2. Arrêt de l'API FastAPI...${NC}"
# Chercher les processus main.py
PIDS=$(ps aux | grep -E "python.*main.py|uvicorn.*main:app|fastapi" | grep -v grep | grep -v comfyui | awk '{print $2}')
if [ -n "$PIDS" ]; then
    echo "$PIDS" | xargs kill -9 2>/dev/null || true
    echo -e "${GREEN}   ✅ API FastAPI arrêtée${NC}"
else
    echo -e "${YELLOW}   ℹ️  API FastAPI non démarrée${NC}"
fi

# 3. Libérer les ports
echo ""
echo -e "${BLUE}3. Libération des ports...${NC}"

# Port 8000 (API)
PORT_8000=$(lsof -ti:8000 2>/dev/null)
if [ -n "$PORT_8000" ]; then
    echo "$PORT_8000" | xargs kill -9 2>/dev/null || true
    echo -e "${GREEN}   ✅ Port 8000 libéré${NC}"
else
    echo -e "${YELLOW}   ℹ️  Port 8000 déjà libre${NC}"
fi

# Port 8188 (ComfyUI)
PORT_8188=$(lsof -ti:8188 2>/dev/null)
if [ -n "$PORT_8188" ]; then
    echo "$PORT_8188" | xargs kill -9 2>/dev/null || true
    echo -e "${GREEN}   ✅ Port 8188 libéré${NC}"
else
    echo -e "${YELLOW}   ℹ️  Port 8188 déjà libre${NC}"
fi

# 4. Vérifier les processus restants
echo ""
echo -e "${BLUE}4. Vérification des processus restants...${NC}"
REMAINING=$(ps aux | grep -E "python.*main.py|uvicorn|comfyui|arkalia.*luna" | grep -v grep | grep -v "$$")
if [ -n "$REMAINING" ]; then
    echo -e "${YELLOW}   ⚠️  Processus restants trouvés :${NC}"
    echo "$REMAINING" | awk '{print "      PID:", $2, "-", $11, $12, $13}'
    echo ""
    read -p "   Voulez-vous les arrêter ? (o/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Oo]$ ]]; then
        echo "$REMAINING" | awk '{print $2}' | xargs kill -9 2>/dev/null || true
        echo -e "${GREEN}   ✅ Processus arrêtés${NC}"
    fi
else
    echo -e "${GREEN}   ✅ Aucun processus restant${NC}"
fi

# 5. Résumé
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Tous les processus Arkalia-LUNA ont été arrêtés${NC}"
echo ""
echo -e "${BLUE}📋 Pour redémarrer :${NC}"
echo "   • ComfyUI : bash scripts/start_comfyui.sh"
echo "   • API : bash scripts/start_api.sh"
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

