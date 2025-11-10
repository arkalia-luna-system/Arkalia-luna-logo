#!/bin/bash
# 🛑 Script d'arrêt ComfyUI pour Arkalia-LUNA
# Arrête tous les processus ComfyUI et libère le port 8188

set -e

# Couleurs
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

COMFYUI_PORT=8188
PID_FILE="logs/comfyui.pid"

echo "🛑 Arrêt de tous les processus ComfyUI..."

# 1. Arrêter via fichier PID si existe
if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if ps -p "$PID" > /dev/null 2>&1; then
        echo -e "${YELLOW}Arrêt du processus PID: $PID${NC}"
        kill "$PID" 2>/dev/null || true
        sleep 1
        # Forcer l'arrêt si nécessaire
        if ps -p "$PID" > /dev/null 2>&1; then
            echo -e "${YELLOW}Forçage de l'arrêt...${NC}"
            kill -9 "$PID" 2>/dev/null || true
        fi
        rm -f "$PID_FILE"
    else
        rm -f "$PID_FILE"
    fi
fi

# 2. Arrêter tous les processus ComfyUI trouvés
PIDS=$(ps aux | grep "python.*main.py" | grep -E "comfyui|8188" | grep -v grep | awk '{print $2}' | sort -u)
if [ -n "$PIDS" ]; then
    for PID in $PIDS; do
        echo -e "${YELLOW}Arrêt du processus ComfyUI (PID: $PID)...${NC}"
        kill "$PID" 2>/dev/null || true
        sleep 1
        if ps -p "$PID" > /dev/null 2>&1; then
            kill -9 "$PID" 2>/dev/null || true
        fi
    done
fi

# 3. Arrêter les processus utilisant le port 8188
PORT_PIDS=$(lsof -ti:$COMFYUI_PORT 2>/dev/null | sort -u)
if [ -n "$PORT_PIDS" ]; then
    for PID in $PORT_PIDS; do
        echo -e "${YELLOW}Arrêt du processus utilisant le port $COMFYUI_PORT (PID: $PID)...${NC}"
        kill "$PID" 2>/dev/null || true
        sleep 1
        if ps -p "$PID" > /dev/null 2>&1; then
            kill -9 "$PID" 2>/dev/null || true
        fi
    done
fi

# 4. Arrêter les processus enfants (multiprocessing)
CHILD_PIDS=$(ps aux | grep -E "multiprocessing|spawn_main" | grep -E "arkalia-luna-logo|comfyui" | grep -v grep | awk '{print $2}' | sort -u)
if [ -n "$CHILD_PIDS" ]; then
    for PID in $CHILD_PIDS; do
        echo -e "${YELLOW}Arrêt du processus enfant (PID: $PID)...${NC}"
        kill "$PID" 2>/dev/null || true
    done
fi

# Attendre un peu pour que les processus se terminent
sleep 2

# Vérifier qu'il ne reste plus de processus
REMAINING=$(ps aux | grep -E "python.*main.py|comfyui" | grep -v grep | wc -l | tr -d ' ')
if [ "$REMAINING" -eq 0 ]; then
    echo -e "${GREEN}✅ Tous les processus ComfyUI ont été arrêtés${NC}"
else
    echo -e "${YELLOW}⚠️  Il reste $REMAINING processus. Vérifiez avec : ps aux | grep comfyui${NC}"
fi

# Vérifier que le port est libre
if lsof -ti:$COMFYUI_PORT > /dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  Le port $COMFYUI_PORT est encore utilisé${NC}"
else
    echo -e "${GREEN}✅ Le port $COMFYUI_PORT est maintenant libre${NC}"
fi

