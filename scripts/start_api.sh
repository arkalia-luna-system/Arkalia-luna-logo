#!/bin/bash
# 🚀 Script de démarrage de l'API Arkalia-LUNA Logo Generator

cd "$(dirname "$0")/.." || exit 1

echo "🌙 Démarrage de l'API Arkalia-LUNA Logo Generator"
echo "=================================================="
echo ""

# Vérifier et arrêter les processus existants sur le port 8000
PORT=8000
EXISTING_PID=$(lsof -ti:$PORT 2>/dev/null)

if [ -n "$EXISTING_PID" ]; then
    echo "⚠️  Processus existant détecté sur le port $PORT (PID: $EXISTING_PID)"
    echo "🛑 Arrêt du processus existant..."
    kill -9 "$EXISTING_PID" 2>/dev/null
    sleep 2
    echo "✅ Processus arrêté"
    echo ""
fi

# Vérifier les processus Python main.py
PYTHON_PIDS=$(ps aux | grep "python.*main.py" | grep -v grep | awk '{print $2}')

if [ -n "$PYTHON_PIDS" ]; then
    echo "⚠️  Processus Python main.py détectés (PIDs: $PYTHON_PIDS)"
    echo "🛑 Arrêt des processus..."
    echo "$PYTHON_PIDS" | xargs kill -9 2>/dev/null
    sleep 2
    echo "✅ Processus arrêtés"
    echo ""
fi

# Activer l'environnement virtuel
if [ -d "arkalia-luna-env" ]; then
    echo "✅ Activation de l'environnement virtuel..."
    source arkalia-luna-env/bin/activate
else
    echo "⚠️  Environnement virtuel non trouvé. Création..."
    python3 -m venv arkalia-luna-env
    source arkalia-luna-env/bin/activate
    pip install -e .
fi

# Vérifier les dépendances
echo "🔍 Vérification des dépendances..."
python -c "import fastapi, slowapi, uvicorn" 2>/dev/null || {
    echo "📦 Installation des dépendances manquantes..."
    pip install fastapi uvicorn slowapi
}

# Vérifier que le port est libre
if lsof -ti:$PORT >/dev/null 2>&1; then
    echo "❌ Erreur : Le port $PORT est toujours occupé"
    echo "   Utilisez : lsof -ti:$PORT | xargs kill -9"
    exit 1
fi

# Démarrer l'API
echo ""
echo "🚀 Démarrage de l'API sur http://localhost:$PORT"
echo "📖 Swagger UI : http://localhost:$PORT/docs"
echo "📊 Métriques : http://localhost:$PORT/metrics"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter"
echo ""

python main.py

