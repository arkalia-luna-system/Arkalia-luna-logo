#!/bin/bash

echo "🧪 Test de validation du titre de PR GitHub Actions"
echo "=================================================="

# Simuler la validation exacte du workflow
validate_pr_title_github() {
    local title="$1"
    echo "   Test: '$title'"
    
    # Validation stricte des titres de PR (copie exacte du workflow)
    # Format 1: type: description (sans scope)
    # Format 2: type(scope): description (avec scope)
    
    # Vérifier si c'est un format sans scope
    if [[ "$title" =~ ^(feat|fix|docs|style|refactor|test|chore|perf|ci|build|revert): ]]; then
      # Vérifier qu'il y a une description après les deux-points
      if [[ "$title" =~ ^(feat|fix|docs|style|refactor|test|chore|perf|ci|build|revert):[[:space:]] ]]; then
        echo "   ✅ Titre de PR valide (sans scope): $title"
        return 0
      fi
    fi
    
    # Vérifier si c'est un format avec scope
    if [[ "$title" =~ ^(feat|fix|docs|style|refactor|test|chore|perf|ci|build|revert)\([a-z_-]+\): ]]; then
      # Vérifier qu'il y a une description après les deux-points
      if [[ "$title" =~ ^(feat|fix|docs|style|refactor|test|chore|perf|ci|build|revert)\([a-z_-]+\):[[:space:]] ]]; then
        echo "   ✅ Titre de PR valide (avec scope): $title"
        return 0
      fi
    fi
    
    # Si on arrive ici, le titre est invalide
    echo "   ❌ Titre de PR invalide: $title"
    echo "   Format attendu: type(scope): description"
    echo "   Formats acceptés:"
    echo "     - feat(logo): ajouter nouveau style"
    echo "     - fix: corriger erreur"
    echo "     - docs: mise à jour README"
    echo "     - style: reformater le code"
    echo "   Règles:"
    echo "     - Le scope doit contenir uniquement des lettres, tirets et underscores"
    echo "     - Il doit y avoir une description après les deux-points"
    return 1
}

echo -e "\n1️⃣ Test du titre du commit actuel:"
validate_pr_title_github "fix(tests): corriger tous les tests avec assert au lieu de return et méthodes manquantes"

echo -e "\n2️⃣ Test d'autres titres valides:"
validate_pr_title_github "feat(logo): ajouter nouveau style mystique"
validate_pr_title_github "fix: corriger erreur de validation"
validate_pr_title_github "docs: mise à jour README avec exemples"
validate_pr_title_github "style: reformater le code avec ruff"
validate_pr_title_github "refactor(svg): optimiser la génération"
validate_pr_title_github "test: ajouter tests pour variants"
validate_pr_title_github "chore: nettoyer les fichiers temporaires"
validate_pr_title_github "perf: optimiser la performance des builders"
validate_pr_title_github "ci: corriger workflow GitHub Actions"
validate_pr_title_github "build: mettre à jour pyproject.toml"
validate_pr_title_github "revert: annuler la dernière modification"

echo -e "\n3️⃣ Test de titres invalides:"
validate_pr_title_github "Ajouter nouveau style" || echo "   ✅ Correctement rejeté"
validate_pr_title_github "fix" || echo "   ✅ Correctement rejeté"
validate_pr_title_github "feat:" || echo "   ✅ Correctement rejeté"
validate_pr_title_github "feat(): description" || echo "   ✅ Correctement rejeté"
validate_pr_title_github "feat(123): description" || echo "   ✅ Correctement rejeté"
validate_pr_title_github "feat(logo) description" || echo "   ✅ Correctement rejeté"

echo -e "\n🎯 Test de validation terminé!"
