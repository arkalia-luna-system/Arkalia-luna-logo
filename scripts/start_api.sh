#!/bin/bash
# 🚀 Script de démarrage de l'API Arkalia-LUNA Logo Generator

cd "$(dirname "$0")/.." || exit 1

echo "🌙 Démarrage de l'API Arkalia-LUNA Logo Generator"
echo "=================================================="
echo ""

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

# Démarrer l'API
echo ""
echo "🚀 Démarrage de l'API sur http://localhost:8000"
echo "📖 Swagger UI : http://localhost:8000/docs"
echo "📊 Métriques : http://localhost:8000/metrics"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter"
echo ""

python main.py

