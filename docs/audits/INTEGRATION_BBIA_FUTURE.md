# 🤖 Intégration Future BBIA Branding

**Statut** : Préparation complète - En attente du déplacement dans T7  
**Date** : 2025-11-15  
**Projet actuel** : `/Users/athalia/Desktop/logo bbia/bbia_branding/`  
**Projet futur** : `/Volumes/T7/bbia-branding/`

---

## 📋 Vue d'ensemble

Ce document décrit l'intégration future de BBIA Branding dans Arkalia-LUNA Logo Generator. Tous les modules sont **préparés et prêts** pour l'activation quand BBIA Branding sera déplacé dans T7.

---

## ✅ Modules préparés

### 1. `bbia_palette.py` ✅

**Palette de couleurs officielle BBIA** :
- Bleu primaire : `#0066FF`
- Blanc secondaire : `#FFFFFF`
- Gris tertiaire : `#2C2C2C`
- Variantes (light, dark, off-white)

**Usage** :
```python
from src.bbia_palette import BBIA_PALETTE

# Accès aux couleurs
blue = BBIA_PALETTE.PRIMARY_BLUE
white = BBIA_PALETTE.SECONDARY_WHITE
gray = BBIA_PALETTE.TERTIARY_GRAY

# Conversion RGB
rgb = BBIA_PALETTE.get_primary_rgb()  # (0, 102, 255)
```

### 2. `unified_emotions.py` ✅

**Mapping unifié BBIA ↔ Arkalia-LUNA** :
- 12 émotions BBIA Reachy Sim → 10 variantes Arkalia-LUNA
- Mapping bidirectionnel
- Validation des émotions

**Usage** :
```python
from src.unified_emotions import UNIFIED_EMOTIONS
from src.variants import VariantType

# BBIA → Arkalia-LUNA
variant = UNIFIED_EMOTIONS.bbia_to_arkalia("happy")  # VariantType.CREATIVE

# Arkalia-LUNA → BBIA
emotions = UNIFIED_EMOTIONS.arkalia_to_bbia(VariantType.SERENITY)  # ["neutral", "calm"]
```

**Mapping complet** :
| BBIA | Arkalia-LUNA |
|------|--------------|
| `neutral`, `calm` | `SERENITY` |
| `happy`, `playful` | `CREATIVE` |
| `sad` | `RAINY` |
| `angry` | `STORMY` |
| `surprised` | `AWAKENING` |
| `excited` | `EXPLOSIVE` |
| `curious`, `confused` | `MYSTERY` |
| `focused` | `POWER` |
| `sleepy` | `SNOWY` |

### 3. `bbia_branding_generator.py` ✅

**Générateur BBIA - Squelette préparé** :
- Hérite de `ArkaliaLunaLogo`
- Vérifie la disponibilité de BBIA Branding
- Méthodes préparées pour génération automatique

**Fonctionnalités prévues** :
- ✅ Génération déclinaisons (mark only, vertical, horizontal)
- ✅ Export multi-formats (SVG, PNG 32px, 512px, 1024px)
- ✅ Variantes de fond (clair, sombre, bleu)
- ✅ Respect style guide BBIA

**Activation** :
```python
# Actuellement en mode préparation
generator = BBIABrandingGenerator()
stats = generator.get_bbia_stats()
# {"bbia_branding_available": False, "status": "preparation"}

# Quand BBIA Branding sera dans T7 :
# {"bbia_branding_available": True, "status": "ready"}
```

---

## 🚀 Activation (quand BBIA Branding dans T7)

### Étape 1 : Déplacer BBIA Branding

```bash
# Déplacer depuis Desktop vers T7
mv /Users/athalia/Desktop/logo\ bbia/bbia_branding /Volumes/T7/bbia-branding
```

### Étape 2 : Décommenter dans `generator_factory.py`

```python
# Dans src/generator_factory.py

# AVANT (commenté)
# from .bbia_branding_generator import BBIABrandingGenerator

# APRÈS (décommenté)
from .bbia_branding_generator import BBIABrandingGenerator

# Dans GENERATOR_TYPES
GENERATOR_TYPES = {
    # ... autres générateurs ...
    "bbia": BBIABrandingGenerator,  # ✅ Activé
}

# Dans get_available_generators()
"bbia": {
    "name": "BBIA Branding",
    "description": "🤖 Générateur BBIA - Automatisation branding",
},
```

### Étape 3 : Implémenter la génération réelle

Dans `bbia_branding_generator.py`, compléter la méthode `generate_svg_logo()` :

```python
def generate_svg_logo(self, variant_name: str, size: int = 200) -> Path:
    """Génère un logo SVG BBIA"""
    # 1. Lire le SVG source BBIA
    source_svg = self.bbia_logo_2d_path / f"bbia_logo_{variant_name}_v2.svg"
    
    # 2. Appliquer transformations selon variant_name
    # - mark_only : Symbole seul
    # - vertical : Symbole + texte vertical
    # - horizontal : Symbole + texte horizontal
    
    # 3. Appliquer palette BBIA
    # - Fond clair : Bleu + Gris
    # - Fond sombre : Blanc
    # - Fond bleu : Blanc uniquement
    
    # 4. Exporter SVG + PNG
    # - SVG vectoriel
    # - PNG aux tailles requises (32px, 512px, 1024px)
    
    return output_path
```

### Étape 4 : Tester

```bash
# Test du générateur BBIA
python -m src.cli generate --generator bbia --variant mark_only --size 512

# Génération toutes déclinaisons
python -c "from src.bbia_branding_generator import BBIABrandingGenerator; gen = BBIABrandingGenerator(); gen.generate_all_declinations()"
```

---

## 📊 Architecture préparée

```
arkalia-luna-logo/
├── src/
│   ├── bbia_palette.py              ✅ Palette BBIA
│   ├── unified_emotions.py          ✅ Mapping émotions
│   ├── bbia_branding_generator.py  ✅ Générateur (squelette)
│   └── generator_factory.py        ⏳ À décommenter
│
└── docs/
    └── INTEGRATION_BBIA_FUTURE.md   ✅ Ce document
```

---

## 🔗 Intégration avec BBIA Reachy Sim

Quand BBIA Branding sera activé, l'intégration avec BBIA Reachy Sim sera possible :

```python
from src.unified_emotions import UNIFIED_EMOTIONS
from src.bbia_branding_generator import BBIABrandingGenerator

# Synchroniser émotion robot → logo
robot_emotion = "happy"  # Depuis BBIA Reachy Sim
variant = UNIFIED_EMOTIONS.bbia_to_arkalia(robot_emotion)  # CREATIVE

# Générer logo correspondant
generator = BBIABrandingGenerator()
logo = generator.generate_svg_logo("mark_only", 512)
```

---

## ✅ Checklist activation

- [ ] BBIA Branding déplacé dans `/Volumes/T7/bbia-branding/`
- [ ] Décommenter imports dans `generator_factory.py`
- [ ] Décommenter `"bbia"` dans `GENERATOR_TYPES`
- [ ] Décommenter description dans `get_available_generators()`
- [ ] Implémenter `generate_svg_logo()` dans `bbia_branding_generator.py`
- [ ] Tester génération mark_only
- [ ] Tester génération vertical
- [ ] Tester génération horizontal
- [ ] Tester export multi-formats
- [ ] Tester variantes de fond
- [ ] Valider respect style guide BBIA

---

## 📝 Notes

- **Séparation actuelle** : BBIA Branding reste sur Desktop pour éviter conflits avec BBIA Reachy Sim
- **BBIA Reachy Sim** : Déjà parfaite, en attente du robot réel
- **Intégration future** : Tous les modules sont prêts, activation en 5 minutes quand déplacé

---

**Dernière mise à jour** : 2025-11-15  
**Statut** : ✅ Préparation complète - Prêt pour activation

