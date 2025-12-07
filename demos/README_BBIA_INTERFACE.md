# 🤖 BBIA OS - Live Interface

Interface visage vivante pour BBIA (Reachy Mini) - Version dynamique et interactive.

## 🎯 Description

Cette interface HTML/CSS/JS permet de contrôler le visage de BBIA en temps réel. C'est une interface **légère, performante et réactive** qui peut être intégrée dans n'importe quel projet web ou application.

## 🚀 Utilisation

### Via CLI

```bash
# Ouvrir l'interface dans le navigateur
python -m src.cli bbia-interface
```

### Manuellement

Ouvrir le fichier `demos/bbia_interface.html` dans votre navigateur.

## 🎮 Modes Disponibles

- **Neutre** : État par défaut, BBIA en ligne
- **Joyeux** : Tête légèrement penchée, yeux dilatés
- **Curieux** : Tête penchée à -25° (Reachy Tilt), yeux regardent sur le côté
- **Écoute** : Tête légèrement penchée, yeux verts
- **Veille** : Tête basse, yeux presque fermés
- **Erreur** : Tête basse, yeux rouges

## 💻 Contrôle depuis JavaScript

L'interface expose un objet global `bbia` pour contrôle programmatique :

```javascript
// Changer l'humeur
bbia.setMood('curious');
bbia.setMood('happy');
bbia.setMood('listening');
bbia.setMood('sleep');
bbia.setMood('error');
bbia.setMood('neutral');
```

## 🐍 Intégration avec Python (Flask/Streamlit)

### Exemple Flask

```python
from flask import Flask, render_template_string, jsonify
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    with open('demos/bbia_interface.html', 'r') as f:
        return f.read()

@app.route('/api/bbia/mood/<mood>')
def set_mood(mood):
    # Logique métier ici
    return jsonify({'status': 'ok', 'mood': mood})

if __name__ == '__main__':
    webbrowser.open('http://localhost:5000')
    app.run(debug=True)
```

### Exemple Streamlit

```python
import streamlit as st
from pathlib import Path

# Charger l'interface HTML
interface_path = Path("demos/bbia_interface.html")
html_content = interface_path.read_text()

# Afficher dans Streamlit
st.components.v1.html(html_content, height=600)

# Contrôle via JavaScript
mood = st.selectbox("Mode BBIA", ['neutral', 'happy', 'curious', 'listening', 'sleep', 'error'])
st.markdown(f"""
<script>
    if (window.bbia) {{
        window.bbia.setMood('{mood}');
    }}
</script>
""", unsafe_allow_html=True)
```

## 🎨 Caractéristiques

- ✅ **Léger** : Un seul fichier HTML, pas de dépendances
- ✅ **Performant** : Animations CSS natives, pas de vidéo
- ✅ **Réactif** : Contrôle en temps réel via JavaScript
- ✅ **Scalable** : SVG vectoriel, net à toutes les tailles
- ✅ **Modulaire** : Facile à intégrer dans n'importe quel projet

## 🔧 Personnalisation

### Couleurs

Modifier les variables CSS dans `:root` :

```css
:root {
    --bbia-white: #f0f0f0;
    --bbia-dark: #1a1a1a;
    --bbia-blue: #00e5ff;
    --bbia-eye: #000;
}
```

### Animations

Les animations sont définies dans le CSS :

- `@keyframes breathe` : Animation de respiration
- `@keyframes spin` : Rotation des cercles HUD

### Nouveaux Modes

Ajouter un nouveau mode dans `BbiaController.setMood()` :

```javascript
case 'nouveau_mode':
    this.head.style.transform = 'rotate(15deg)';
    this.pupilL.style.fill = '#FF00FF';
    break;
```

## 📁 Structure

```
demos/
└── bbia_interface.html    # Interface complète (HTML + CSS + JS)
```

## 🔗 Intégration avec bbia-sim

Pour intégrer avec votre simulateur Python :

1. **Via WebSocket** : Envoyer les commandes depuis Python vers le front-end
2. **Via API REST** : Flask/FastAPI qui contrôle l'interface
3. **Via Streamlit** : Intégration directe dans l'app Streamlit

## 📝 Notes

- L'interface cligne automatiquement les yeux toutes les 4-6 secondes
- Les transitions sont fluides grâce aux transitions CSS
- Le mode "sleep" et "error" désactivent le clignement automatique
- L'objet `bbia` est exposé globalement pour contrôle externe

---

**Dernière mise à jour** : 7 décembre 2025

