#!/bin/bash

echo "🧹 Nettoyage sécurisé des fichiers cachés macOS..."

# Vérification de sécurité - on ne supprime que dans le projet actuel
if [[ ! -f "setup.py" ]] && [[ ! -f "pyproject.toml" ]]; then
    echo "❌ ERREUR: Ce script doit être exécuté depuis la racine du projet Arkalia-LUNA"
    echo "   Dossier actuel: $(pwd)"
    exit 1
fi

echo "📍 Dossier de travail: $(pwd)"
echo "🔍 Vérification des fichiers à supprimer..."

# Comptage des fichiers cachés avant suppression
hidden_files=$(find . -name "._*" -o -name ".!*" -o -name ".DS_Store" | wc -l)
echo "📊 Fichiers cachés macOS trouvés: $hidden_files"

if [ $hidden_files -gt 0 ]; then
    echo "🗑️  Suppression des fichiers cachés macOS..."
    
    # Suppression sécurisée des fichiers cachés macOS
    find . -name "._*" -type f -delete
    find . -name ".!*" -type f -delete
    find . -name ".DS_Store" -type f -delete
    
    echo "✅ Fichiers cachés supprimés"
else
    echo "✨ Aucun fichier caché trouvé"
fi

# Suppression sécurisée des dossiers egg-info (uniquement s'ils existent)
if [ -d "src" ]; then
    egg_info_dirs=$(find src -name "*.egg-info" -type d 2>/dev/null | wc -l)
    if [ $egg_info_dirs -gt 0 ]; then
        echo "🗑️  Suppression des dossiers egg-info..."
        find src -name "*.egg-info" -type d -exec rm -rf {} + 2>/dev/null
        echo "✅ Dossiers egg-info supprimés"
    else
        echo "✨ Aucun dossier egg-info trouvé"
    fi
fi

# Suppression sécurisée des dossiers de build (uniquement s'ils existent)
if [ -d "build" ]; then
    echo "🗑️  Suppression du dossier build..."
    rm -rf build/
    echo "✅ Dossier build supprimé"
fi

if [ -d "dist" ]; then
    echo "🗑️  Suppression du dossier dist..."
    rm -rf dist/
    echo "✅ Dossier dist supprimé"
fi

# Vérification finale
echo ""
echo "🔍 Vérification finale..."
remaining_hidden=$(find . -name "._*" -o -name ".!*" -o -name ".DS_Store" 2>/dev/null | wc -l)
echo "📊 Fichiers cachés restants: $remaining_hidden"

if [ $remaining_hidden -eq 0 ]; then
    echo "🎉 Nettoyage terminé avec succès !"
else
    echo "⚠️  Attention: $remaining_hidden fichiers cachés restent"
    echo "   Utilisez 'find . -name \"._*\"' pour les localiser"
fi

echo ""
echo "📁 Contenu du dossier après nettoyage:"
ls -la | head -20
