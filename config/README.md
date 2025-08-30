# ⚙️ Configuration - Arkalia-LUNA Logo Generator

## 📁 **Organisation des Fichiers de Configuration**

Ce dossier contient tous les fichiers de configuration du projet, organisés de manière professionnelle pour faciliter la maintenance et la configuration.

## 🗂️ **Structure des Fichiers**

```
config/
├── README.md                    # Ce fichier - Guide de configuration
├── pyproject.toml              # Configuration principale du projet Python
├── pytest.ini                  # Configuration des tests pytest
├── .pre-commit-config.yaml     # Configuration des hooks pre-commit
└── Makefile                    # Makefile pour les commandes de développement
```

## 🔧 **Fichiers de Configuration**

### **1. pyproject.toml**
Configuration principale du projet Python avec :
- Métadonnées du package
- Dépendances et dépendances optionnelles
- Configuration des outils (Black, Ruff, MyPy)
- Configuration pytest et coverage

### **2. pytest.ini**
Configuration des tests avec :
- Marqueurs de tests
- Options par défaut
- Configuration des chemins de tests

### **3. .pre-commit-config.yaml**
Configuration des hooks pre-commit pour :
- Formatage automatique avec Black
- Linting avec Ruff
- Vérification des types avec MyPy
- Vérifications de sécurité

### **4. Makefile**
Commandes de développement simplifiées :
- Tests et qualité du code
- Génération de logos
- Nettoyage et maintenance

## 🚀 **Utilisation**

### **Installation des Hooks Pre-commit**
```bash
# Depuis la racine du projet
pre-commit install --config-file config/.pre-commit-config.yaml
```

### **Utilisation du Makefile**
```bash
# Depuis la racine du projet
make -f config/Makefile help
make -f config/Makefile quick-start
```

### **Configuration Pytest**
```bash
# Depuis la racine du projet
pytest --config-file config/pytest.ini
```

## 📝 **Personnalisation**

### **Modifier la Configuration**
1. **pyproject.toml** : Métadonnées et dépendances
2. **pytest.ini** : Comportement des tests
3. **.pre-commit-config.yaml** : Hooks de qualité
4. **Makefile** : Commandes personnalisées

### **Ajouter de Nouveaux Outils**
1. Ajouter la configuration dans le fichier approprié
2. Mettre à jour ce README
3. Tester la configuration
4. Commiter les changements

## 🔍 **Vérification de la Configuration**

### **Test de la Configuration Pre-commit**
```bash
pre-commit run --config-file config/.pre-commit-config.yaml --all-files
```

### **Test de la Configuration Pytest**
```bash
pytest --config-file config/pytest.ini --collect-only
```

### **Test du Makefile**
```bash
make -f config/Makefile help
```

## 🚨 **Dépannage**

### **Problèmes Courants**

#### **1. Pre-commit ne fonctionne pas**
```bash
# Réinstaller les hooks
pre-commit uninstall
pre-commit install --config-file config/.pre-commit-config.yaml
```

#### **2. Pytest utilise la mauvaise configuration**
```bash
# Spécifier explicitement le fichier de configuration
pytest --config-file config/pytest.ini
```

#### **3. Makefile non trouvé**
```bash
# Utiliser le chemin complet
make -f config/Makefile
```

### **Logs de Débogage**
```bash
# Pre-commit avec logs détaillés
pre-commit run --config-file config/.pre-commit-config.yaml --all-files -v

# Pytest avec logs détaillés
pytest --config-file config/pytest.ini -v -s
```

## 📚 **Documentation Associée**

- **[API.md](../docs/API.md)** : Documentation de l'API
- **[ARCHITECTURE.md](../docs/ARCHITECTURE.md)** : Architecture technique
- **[CONTRIBUTING.md](../docs/CONTRIBUTING.md)** : Guide de contribution
- **[CI-README.md](../docs/CI-README.md)** : Configuration CI/CD

## 🔄 **Maintenance**

### **Mise à Jour des Outils**
```bash
# Mettre à jour pre-commit
pre-commit autoupdate --config-file config/.pre-commit-config.yaml

# Mettre à jour les dépendances
pip install --upgrade -r requirements.txt
```

### **Validation de la Configuration**
```bash
# Vérifier la syntaxe des fichiers
python -c "import tomllib; tomllib.load(open('config/pyproject.toml', 'rb'))"
python -c "import yaml; yaml.safe_load(open('config/.pre-commit-config.yaml', 'r'))"
```

---

**⚙️ Configuration organisée et maintenue - Version 2.0.0**

*Dernière mise à jour : 2024-12-19*
