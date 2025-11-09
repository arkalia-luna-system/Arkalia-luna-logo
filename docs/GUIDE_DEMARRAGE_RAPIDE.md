# 🚀 Guide de Démarrage Rapide - Arkalia-LUNA Logo Generator

**Objectif** : Utiliser 100% du potentiel en 10 minutes

---

## ⚡ Démarrage Ultra-Rapide (2 minutes)

### **1. Activer l'environnement**

```bash
cd /Volumes/T7/logo/arkalia-luna-logo
source arkalia-luna-env/bin/activate
```

### **2. Générer votre premier logo**

```bash
# Logo Ultimate (recommandé)
python -m src.cli generate -v serenity -g ultimate -s 200

# Voir tous les générateurs
python -m src.cli generators

# Voir toutes les variantes
python -m src.cli info
```

---

## 🌐 Démarrer l'API FastAPI (3 minutes)

### **Option 1 : Script automatique**

```bash
./scripts/start_api.sh
```

### **Option 2 : Manuel**

```bash
source arkalia-luna-env/bin/activate
python main.py
```

### **Accéder à l'API**

- **Swagger UI** : http://localhost:8000/docs
- **Health** : http://localhost:8000/health
- **Métriques** : http://localhost:8000/metrics

### **Tester l'API**

```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"variant": "serenity", "size": 200, "generator_type": "ultimate"}'
```

---

## 🎨 Explorer Tous les Générateurs (5 minutes)

### **Générateurs Disponibles**

```bash
# Tester chaque générateur
for gen in ultimate cosmic hyper_ai dashboard ai_moon advanced; do
  python -m src.cli generate -v serenity -g $gen -s 200
done
```

### **Générateurs Recommandés**

1. **Ultimate** : Effets cosmiques extrêmes ⭐
2. **Cosmic** : Sphères lumineuses et réseaux neuronaux
3. **Hyper-AI** : Intelligence artificielle avancée
4. **Dashboard** : Style professionnel interface

---

## 🌈 Explorer Toutes les Variantes (5 minutes)

### **Variantes de Base**

```bash
for variant in serenity power mystery awakening creative; do
  python -m src.cli generate -v $variant -g ultimate -s 200
done
```

### **Variantes Dynamiques**

```bash
for variant in rainy stormy explosive sunny snowy; do
  python -m src.cli generate -v $variant -g ultimate -s 200
done
```

---

## 🤖 Scripts d'Automatisation

### **Exploration Automatique**

```bash
./scripts/quick_explore.sh
```

### **Génération de Screenshots**

```bash
python scripts/generate_screenshots.py
```

### **Génération de Tous les Logos**

```bash
python -m src.cli generate-all -s 200
```

---

## 🐳 Docker + Monitoring (Optionnel)

### **Démarrer Docker**

```bash
# Démarrer Docker Desktop d'abord
docker-compose -f docker-compose.prod.yml up -d
```

### **Services Disponibles**

- **API** : http://localhost:8000
- **Grafana** : http://localhost:3000
- **Prometheus** : http://localhost:9090
- **Nginx** : http://localhost:80

---

## 📊 Commandes Utiles

### **Statistiques**

```bash
# Statistiques CLI
python -m src.cli stats

# Statistiques API
curl http://localhost:8000/stats
```

### **Métriques Prometheus**

```bash
curl http://localhost:8000/metrics
```

### **Nettoyage**

```bash
python -m src.cli clean
```

---

## 🎯 Checklist Rapide

- [ ] Environnement virtuel activé
- [ ] Premier logo généré
- [ ] API démarrée
- [ ] Swagger UI accessible
- [ ] Au moins 3 générateurs testés
- [ ] Au moins 5 variantes testées
- [ ] Scripts d'automatisation testés

---

## 🆘 Problèmes Courants

### **Port 8000 occupé**

```bash
# Le script start_api.sh le gère automatiquement
# Ou manuellement :
lsof -ti:8000 | xargs kill -9
```

### **Générateur Cosmic ne fonctionne pas**

✅ **Corrigé** - Devrait fonctionner maintenant

### **AI Generator ne fonctionne pas**

⚠️ Nécessite `diffusers` (dépendance optionnelle) :
```bash
pip install diffusers torch
```

---

## 📚 Documentation Complète

- **README.md** : Vue d'ensemble
- **docs/QUICKSTART.md** : Guide détaillé
- **docs/API.md** : Documentation API
- **docs/AUDIT_UTILISATION_POTENTIEL.md** : Potentiel complet
- **EXPLOITATION_COMPLETE.md** : Résultats des tests
- **RESUME_FINAL.md** : Résumé exécutif

---

**🚀 Prêt à générer des logos exceptionnels !**

**Créé** : Novembre 2025  
**Version** : 2.0.0

