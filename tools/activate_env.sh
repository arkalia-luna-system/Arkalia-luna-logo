#!/bin/bash
# 🌙 Arkalia-LUNA Logo - Activation de l'environnement virtuel

echo "🌙 Activation de l'environnement virtuel Arkalia-LUNA..."

# Activation de l'environnement virtuel
source arkalia-luna-env/bin/activate

# Vérification de l'activation
if [ $? -eq 0 ]; then
    echo "✅ Environnement virtuel activé !"
    echo "🐍 Python: $(which python)"
    echo "📦 Pip: $(which pip)"
    echo ""
    echo "🚀 Commandes disponibles :"
    echo "  • python arkalia-luna-logo.py info          - Voir les variantes"
    echo "  • python arkalia-luna-logo.py generate-all  - Générer tous les logos"
    echo "  • python arkalia-luna-logo.py generate -v serenity  - Logo Sérénité"
    echo "  • python arkalia-luna-logo.py favicon -v power      - Favicon Puissance"
    echo ""
    echo "💡 Pour désactiver : deactivate"
else
    echo "❌ Erreur lors de l'activation de l'environnement virtuel"
    exit 1
fi
