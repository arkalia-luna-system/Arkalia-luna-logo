#!/bin/bash
# 🔍 Script de vérification ComfyUI pour Arkalia-LUNA
# Vérifie que ComfyUI fonctionne correctement

# Couleurs
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

COMFYUI_PORT=8188
PID_FILE="logs/comfyui.pid"

echo -e "${BLUE}🔍 Vérification de ComfyUI...${NC}"
echo ""

# 1. Vérifier le processus
echo -e "${BLUE}1. Vérification du processus...${NC}"
if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if ps -p "$PID" > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Processus ComfyUI actif (PID: $PID)${NC}"
    else
        echo -e "${RED}❌ Processus ComfyUI non trouvé (PID: $PID)${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  Fichier PID non trouvé${NC}"
fi

# Vérifier tous les processus ComfyUI
PIDS=$(ps aux | grep "python.*main.py" | grep -E "comfyui|8188" | grep -v grep | awk '{print $2}' | sort -u)
if [ -n "$PIDS" ]; then
    echo -e "${GREEN}✅ Processus ComfyUI trouvés : $(echo $PIDS | tr '\n' ' ')${NC}"
else
    echo -e "${RED}❌ Aucun processus ComfyUI trouvé${NC}"
fi

echo ""

# 2. Vérifier le port
echo -e "${BLUE}2. Vérification du port $COMFYUI_PORT...${NC}"
PORT_PIDS=$(lsof -ti:$COMFYUI_PORT 2>/dev/null | sort -u)
if [ -n "$PORT_PIDS" ]; then
    echo -e "${GREEN}✅ Port $COMFYUI_PORT utilisé par : $(echo $PORT_PIDS | tr '\n' ' ')${NC}"
else
    echo -e "${RED}❌ Port $COMFYUI_PORT libre (ComfyUI non démarré)${NC}"
fi

echo ""

# 3. Vérifier l'accessibilité HTTP
echo -e "${BLUE}3. Vérification de l'accessibilité HTTP...${NC}"
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:$COMFYUI_PORT/ 2>/dev/null)
if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ ComfyUI répond correctement (HTTP $HTTP_CODE)${NC}"
    echo -e "${GREEN}   🌐 Interface accessible sur : http://localhost:$COMFYUI_PORT${NC}"
elif [ "$HTTP_CODE" = "000" ]; then
    echo -e "${YELLOW}⚠️  ComfyUI démarre... (HTTP $HTTP_CODE)${NC}"
else
    echo -e "${RED}❌ ComfyUI ne répond pas (HTTP $HTTP_CODE)${NC}"
fi

echo ""

# 4. Vérifier les logs
echo -e "${BLUE}4. Dernières lignes des logs...${NC}"
if [ -f "logs/comfyui.log" ]; then
    echo -e "${BLUE}   Dernières lignes :${NC}"
    tail -3 logs/comfyui.log 2>/dev/null | sed 's/^/   /'
else
    echo -e "${YELLOW}⚠️  Fichier de logs non trouvé${NC}"
fi

echo ""

# 5. Résumé
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
if [ -n "$PIDS" ] && [ -n "$PORT_PIDS" ] && [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ ComfyUI fonctionne correctement !${NC}"
    echo ""
    echo -e "${GREEN}📋 Actions disponibles :${NC}"
    echo "   • Ouvrir l'interface : http://localhost:$COMFYUI_PORT"
    echo "   • Voir les logs : tail -f logs/comfyui.log"
    echo "   • Arrêter : bash scripts/stop_comfyui.sh"
    echo "   • Redémarrer : bash scripts/start_comfyui.sh"
elif [ -n "$PIDS" ] || [ -n "$PORT_PIDS" ]; then
    echo -e "${YELLOW}⚠️  ComfyUI semble démarrer...${NC}"
    echo "   Attendez quelques secondes et relancez : bash scripts/check_comfyui.sh"
else
    echo -e "${RED}❌ ComfyUI n'est pas démarré${NC}"
    echo ""
    echo -e "${YELLOW}📋 Pour démarrer ComfyUI :${NC}"
    echo "   bash scripts/start_comfyui.sh"
fi
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

