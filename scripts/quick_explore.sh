#!/bin/bash
# 🚀 Script de découverte rapide - Arkalia-LUNA Logo Generator
# Explore toutes les fonctionnalités sous-exploitées

echo "🌙 Arkalia-LUNA Logo Generator - Exploration Rapide"
echo "=================================================="
echo ""

# 1. Lister tous les générateurs
echo "📋 1. Générateurs disponibles :"
python -m src.cli generators
echo ""

# 2. Lister toutes les variantes
echo "📋 2. Variantes disponibles :"
python -m src.cli info
echo ""

# 3. Générer un logo avec chaque générateur avancé
echo "🎨 3. Test des générateurs avancés :"
for gen in ultimate cosmic hyper_ai ai; do
    echo "   → Génération avec $gen..."
    python -m src.cli generate -v serenity -g $gen -s 200 2>/dev/null || echo "      ⚠️  $gen non disponible"
done
echo ""

# 4. Générer toutes les variantes dynamiques
echo "🎨 4. Test des variantes dynamiques :"
for variant in rainy stormy explosive sunny snowy; do
    echo "   → Génération $variant..."
    python -m src.cli generate -v $variant -g ultimate -s 200 2>/dev/null || echo "      ⚠️  $variant non disponible"
done
echo ""

# 5. Statistiques
echo "📊 5. Statistiques :"
python -m src.cli stats
echo ""

# 6. Instructions pour API
echo "🌐 6. Pour démarrer l'API FastAPI :"
echo "   python main.py"
echo "   Puis ouvrir : http://localhost:8000/docs"
echo ""

# 7. Instructions pour Docker
echo "🐳 7. Pour démarrer l'infrastructure Docker :"
echo "   docker-compose -f docker-compose.prod.yml up -d"
echo "   Services :"
echo "   - API : http://localhost:8000"
echo "   - Grafana : http://localhost:3000"
echo "   - Prometheus : http://localhost:9090"
echo ""

echo "✅ Exploration terminée !"
echo "📖 Voir docs/AUDIT_UTILISATION_POTENTIEL.md pour plus de détails"

