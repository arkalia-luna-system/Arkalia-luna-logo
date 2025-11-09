#!/bin/bash

# 🚀 Script d'Initialisation GitHub - Arkalia-LUNA Logo Generator
# Ce script configure le repository GitHub avec la structure de branches professionnelle

set -e  # Arrêt en cas d'erreur

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Fonction d'affichage
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Vérification des prérequis
check_prerequisites() {
    print_status "Vérification des prérequis..."
    
    # Vérifier Git
    if ! command -v git &> /dev/null; then
        print_error "Git n'est pas installé. Veuillez l'installer d'abord."
        exit 1
    fi
    
    # Vérifier Python
    if ! command -v python3 &> /dev/null; then
        print_error "Python3 n'est pas installé. Veuillez l'installer d'abord."
        exit 1
    fi
    
    # Vérifier Make
    if ! command -v make &> /dev/null; then
        print_warning "Make n'est pas installé. Certaines commandes ne fonctionneront pas."
    fi
    
    print_success "Prérequis vérifiés"
}

# Vérification de l'état Git
check_git_status() {
    print_status "Vérification de l'état Git..."
    
    if [ ! -d ".git" ]; then
        print_error "Ce répertoire n'est pas un repository Git."
        print_status "Initialisation du repository Git..."
        git init
    fi
    
    # Vérifier s'il y a des changements non commités
    if [ -n "$(git status --porcelain)" ]; then
        # Détecter si on est en mode interactif
        if [ -t 0 ]; then
            # Mode interactif : demander à l'utilisateur
            print_warning "Il y a des changements non commités. Voulez-vous les commiter ? (y/n)"
            read -r response
            if [[ "$response" =~ ^[Yy]$ ]]; then
                git add .
                git commit -m "chore(ci): configuration initiale GitHub"
            else
                print_error "Veuillez commiter ou stasher vos changements avant de continuer."
                exit 1
            fi
        else
            # Mode non-interactif : continuer sans commiter automatiquement
            print_warning "Il y a des changements non commités (mode non-interactif détecté)."
            print_status "Les changements ne seront pas commités automatiquement."
            print_status "Vous pouvez les commiter manuellement plus tard si nécessaire."
        fi
    fi
    
    print_success "État Git vérifié"
}

# Configuration des branches
setup_branches() {
    print_status "Configuration des branches..."
    
    # Vérifier la branche actuelle
    current_branch=$(git branch --show-current)
    print_status "Branche actuelle : $current_branch"
    
    # Créer la branche develop si elle n'existe pas
    if ! git branch | grep -q "develop"; then
        print_status "Création de la branche develop..."
        git checkout -b develop
        print_success "Branche develop créée"
    else
        print_status "Branche develop existe déjà, passage dessus..."
        git checkout develop
    fi
    
    # Retourner sur la branche principale
    if [ "$current_branch" != "main" ] && [ "$current_branch" != "master" ]; then
        git checkout "$current_branch"
    fi
    
    print_success "Branches configurées"
}

# Configuration des remotes
setup_remotes() {
    print_status "Configuration des remotes..."
    
    # Vérifier si origin existe
    if ! git remote | grep -q "origin"; then
        print_status "Configuration du remote origin..."
        # Détecter si on est en mode interactif
        if [ -t 0 ]; then
            # Mode interactif : demander à l'utilisateur
            echo "Veuillez entrer l'URL du repository GitHub :"
            echo "Exemple : https://github.com/username/arkalia-luna-logo.git"
            read -r github_url
            
            if [ -n "$github_url" ]; then
                git remote add origin "$github_url"
                print_success "Remote origin configuré : $github_url"
            else
                print_warning "Aucune URL fournie, remote origin non configuré"
            fi
        else
            # Mode non-interactif : skip la configuration du remote
            print_warning "Mode non-interactif détecté. Remote origin non configuré."
            print_status "Vous pouvez configurer le remote manuellement avec :"
            print_status "  git remote add origin <url>"
        fi
    else
        print_status "Remote origin existe déjà"
        git remote -v
    fi
}

# Configuration des hooks pre-commit
setup_pre_commit() {
    print_status "Configuration des hooks pre-commit..."
    
    if command -v make &> /dev/null; then
        print_status "Installation des hooks pre-commit..."
        make pre-commit-install
        print_success "Hooks pre-commit installés"
    else
        print_warning "Make non disponible, installation manuelle des hooks..."
        print_status "Exécutez : pip install pre-commit && pre-commit install"
    fi
}

# Tests de validation
run_validation_tests() {
    print_status "Exécution des tests de validation..."
    
    if command -v make &> /dev/null; then
        print_status "Tests de qualité..."
        make quality-check || {
            print_warning "Certains tests de qualité ont échoué, mais la configuration continue..."
        }
        
        print_status "Tests unitaires..."
        make test || {
            print_warning "Certains tests ont échoué, mais la configuration continue..."
        }
    else
        print_warning "Make non disponible, tests non exécutés"
    fi
    
    print_success "Tests de validation terminés"
}

# Configuration des branches protégées (instructions)
show_branch_protection_instructions() {
    print_status "Configuration des branches protégées..."
    
    cat << 'EOF'

🌿 CONFIGURATION DES BRANCHES PROTÉGÉES

Pour configurer la protection des branches sur GitHub :

1. Allez sur GitHub → Settings → Branches
2. Ajoutez une règle pour 'main' :
   ✅ Require a pull request before merging
   ✅ Require approvals (2 reviewers)
   ✅ Require status checks to pass before merging
   ✅ Require branches to be up to date before merging
   ✅ Include administrators

3. Ajoutez une règle pour 'develop' :
   ✅ Require a pull request before merging
   ✅ Require approvals (1 reviewer)
   ✅ Require status checks to pass before merging
   ✅ Require branches to be up to date before merging

4. Status checks requis :
   ✅ quality
   ✅ test
   ✅ build

EOF
}

# Configuration des labels GitHub
show_labels_instructions() {
    print_status "Configuration des labels GitHub..."
    
    cat << 'EOF'

🏷️ CONFIGURATION DES LABELS

Pour configurer les labels sur GitHub :

1. Allez sur GitHub → Issues → Labels
2. Cliquez sur "New label" pour chaque label
3. Ou utilisez l'API GitHub pour créer tous les labels d'un coup

Labels principaux à créer :
- bug (rouge)
- enhancement (bleu)
- documentation (bleu)
- good first issue (violet)
- help wanted (vert)
- priority: critical/high/medium/low
- component: logo-generation/cli/web-interface/tests/docs
- status: needs-triage/in-progress/ready-for-review

EOF
}

# Instructions finales
show_final_instructions() {
    print_status "Configuration terminée !"
    
    cat << 'EOF'

🚀 PROCHAINES ÉTAPES

1. Poussez vos branches sur GitHub :
   git push -u origin main
   git push -u origin develop

2. Activez GitHub Actions dans Settings → Actions

3. Configurez les branches protégées (voir instructions ci-dessus)

4. Créez votre première Pull Request :
   git checkout -b feature/initial-setup
   # ... modifications ...
   git commit -m "feat(ci): configuration initiale GitHub"
   git push origin feature/initial-setup

5. Créez la PR sur GitHub vers develop

6. Pour la première release :
   git checkout develop
   git checkout -b release/v2.0.0
   # ... finalisation ...
   git commit -m "chore(release): préparer release v2.0.0"
   git push origin release/v2.0.0
   # Créer PR release/v2.0.0 → main

📚 DOCUMENTATION DISPONIBLE

- .github/BRANCHES.md : Gestion des branches
- .github/DEPLOYMENT.md : Guide de déploiement
- docs/CONTRIBUTING.md : Guide de contribution
- docs/ARCHITECTURE.md : Architecture technique

🎯 COMMANDES UTILES

make test          # Tests complets
make quality-check # Qualité complète
make format        # Formatage du code
make lint          # Vérification du style

EOF
}

# Fonction principale
main() {
    echo "🚀 Configuration GitHub - Arkalia-LUNA Logo Generator"
    echo "=================================================="
    echo ""
    
    check_prerequisites
    check_git_status
    setup_branches
    setup_remotes
    setup_pre_commit
    run_validation_tests
    show_branch_protection_instructions
    show_labels_instructions
    show_final_instructions
    
    print_success "Configuration GitHub terminée avec succès !"
}

# Exécution du script
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
