#!/bin/bash
# 🧠 Script de démarrage ComfyUI pour Arkalia-LUNA
# Démarre ComfyUI en arrière-plan avec gestion d'erreurs

set -e

# Couleurs
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
COMFYUI_DIR="comfyui"
COMFYUI_PORT=8188
LOG_FILE="logs/comfyui.log"
PID_FILE="logs/comfyui.pid"

# Vérifier l'environnement virtuel
if [ ! -d "arkalia-luna-env" ]; then
    echo -e "${RED}❌ Environnement virtuel non trouvé${NC}"
    echo "Exécutez depuis la racine du projet : /Volumes/T7/logo/arkalia-luna-logo"
    exit 1
fi

# Activer l'environnement virtuel
source arkalia-luna-env/bin/activate

# Créer le dossier logs si nécessaire
mkdir -p logs

# Fonction pour arrêter les processus existants
stop_existing_processes() {
    echo -e "${YELLOW}🔍 Recherche de processus ComfyUI existants...${NC}"
    
    # Arrêter via fichier PID
    if [ -f "$PID_FILE" ]; then
        OLD_PID=$(cat "$PID_FILE")
        if ps -p "$OLD_PID" > /dev/null 2>&1; then
            echo -e "${YELLOW}Arrêt du processus existant (PID: $OLD_PID)...${NC}"
            kill "$OLD_PID" 2>/dev/null || true
            sleep 1
            if ps -p "$OLD_PID" > /dev/null 2>&1; then
                kill -9 "$OLD_PID" 2>/dev/null || true
            fi
        fi
        rm -f "$PID_FILE"
    fi
    
    # Arrêter tous les processus ComfyUI
    PIDS=$(ps aux | grep "python.*main.py" | grep -E "comfyui|8188" | grep -v grep | awk '{print $2}' | sort -u)
    if [ -n "$PIDS" ]; then
        echo -e "${YELLOW}Arrêt de $(( $(echo "$PIDS" | wc -l | tr -d ' ') )) processus ComfyUI existants...${NC}"
        for PID in $PIDS; do
            kill "$PID" 2>/dev/null || true
        done
        sleep 2
        # Forcer l'arrêt si nécessaire
        for PID in $PIDS; do
            if ps -p "$PID" > /dev/null 2>&1; then
                kill -9 "$PID" 2>/dev/null || true
            fi
        done
    fi
    
    # Arrêter les processus utilisant le port
    PORT_PIDS=$(lsof -ti:$COMFYUI_PORT 2>/dev/null | sort -u)
    if [ -n "$PORT_PIDS" ]; then
        echo -e "${YELLOW}Arrêt des processus utilisant le port $COMFYUI_PORT...${NC}"
        for PID in $PORT_PIDS; do
            kill "$PID" 2>/dev/null || true
        done
        sleep 2
    fi
    
    # Arrêter les processus enfants
    CHILD_PIDS=$(ps aux | grep -E "multiprocessing|spawn_main" | grep -E "arkalia-luna-logo|comfyui" | grep -v grep | awk '{print $2}' | sort -u)
    if [ -n "$CHILD_PIDS" ]; then
        for PID in $CHILD_PIDS; do
            kill "$PID" 2>/dev/null || true
        done
    fi
    
    sleep 2
}

# Arrêter les processus existants avant de démarrer
stop_existing_processes

# Vérifier que le port est maintenant libre
if lsof -ti:$COMFYUI_PORT > /dev/null 2>&1; then
    echo -e "${RED}❌ Le port $COMFYUI_PORT est encore utilisé après nettoyage${NC}"
    echo "Arrêtez manuellement avec : bash scripts/stop_comfyui.sh"
    exit 1
fi

# Vérifier que ComfyUI est installé
if [ ! -f "$COMFYUI_DIR/main.py" ]; then
    echo -e "${RED}❌ ComfyUI non trouvé dans $COMFYUI_DIR${NC}"
    echo "Installez ComfyUI avec : bash scripts/install_comfyui.sh"
    exit 1
fi

# Démarrer ComfyUI en arrière-plan
echo -e "${GREEN}🚀 Démarrage de ComfyUI...${NC}"
cd "$COMFYUI_DIR"

nohup python main.py \
    --listen 0.0.0.0 \
    --port $COMFYUI_PORT \
    --output ../exports-hyper-ai \
    --disable-auto-launch \
    > ../$LOG_FILE 2>&1 &

COMFYUI_PID=$!
echo $COMFYUI_PID > ../$PID_FILE

cd ..

echo -e "${GREEN}✅ ComfyUI démarré (PID: $COMFYUI_PID)${NC}"
echo "📋 Logs : $LOG_FILE"
echo "🌐 URL : http://localhost:$COMFYUI_PORT"
echo ""
echo "⏳ Attente du démarrage complet (10 secondes)..."
sleep 10

# Vérifier que ComfyUI répond
if curl -s -o /dev/null -w "%{http_code}" http://localhost:$COMFYUI_PORT/ | grep -q "200\|000"; then
    echo -e "${GREEN}✅ ComfyUI est accessible sur http://localhost:$COMFYUI_PORT${NC}"
else
    echo -e "${YELLOW}⚠️  ComfyUI démarre... Vérifiez les logs : tail -f $LOG_FILE${NC}"
fi

echo ""
echo "Pour arrêter ComfyUI :"
echo "  kill $COMFYUI_PID"
echo "  ou : bash scripts/stop_comfyui.sh"

