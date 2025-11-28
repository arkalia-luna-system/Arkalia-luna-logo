"""
🎨 Streamlit Demo - Arkalia-LUNA Logo Generator
Interface web interactive pour génération de logos
"""

import sys
from pathlib import Path

import streamlit as st  # type: ignore[import-untyped]

# Ajouter src au path
sys.path.insert(0, str(Path(__file__).parent))

from src.generator_factory import LogoGeneratorFactory

# Configuration de la page
st.set_page_config(
    page_title="Arkalia-LUNA Logo Generator",
    page_icon="🌙",
    layout="wide",
)

# Titre
st.title("🌙 Arkalia-LUNA Logo Generator")
st.markdown("Générateur de logos avec variantes émotionnelles et IA")

# Sidebar
st.sidebar.header("⚙️ Configuration")

# Sélection du générateur
generator_types = LogoGeneratorFactory.get_available_generators()
generator_names = [gen["name"] for gen in generator_types]
selected_generator = st.sidebar.selectbox(
    "Générateur",
    generator_names,
    index=0,
)

# Sélection de la variante
generator = LogoGeneratorFactory.create_generator(selected_generator.lower())
variants = generator.list_all_variants()
selected_variant = st.sidebar.selectbox("Variante émotionnelle", variants, index=0)

# Sélection de la taille
size = st.sidebar.slider("Taille (pixels)", 128, 1024, 512, 64)

# Bouton de génération
if st.sidebar.button("🎨 Générer le logo", type="primary"):
    with st.spinner("Génération en cours..."):
        try:
            output_path = generator.generate_svg_logo(selected_variant, size)
            st.session_state["last_logo"] = str(output_path)
            st.session_state["last_variant"] = selected_variant
            st.success(f"✅ Logo généré : {output_path.name}")
        except Exception as e:
            st.error(f"❌ Erreur : {e}")

# Affichage du logo
if "last_logo" in st.session_state:
    st.header("📸 Logo généré")
    logo_path = Path(st.session_state["last_logo"])

    if logo_path.exists():
        if logo_path.suffix == ".svg":
            # Afficher SVG
            svg_content = logo_path.read_text(encoding="utf-8")
            st.markdown(
                f'<div style="text-align: center;">{svg_content}</div>',
                unsafe_allow_html=True,
            )
        else:
            # Afficher image
            st.image(str(logo_path), width=size)

        # Informations
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Variante", st.session_state.get("last_variant", "N/A"))
        with col2:
            st.metric("Taille", f"{size}×{size}")
        with col3:
            st.metric("Fichier", logo_path.name)

        # Téléchargement
        with open(logo_path, "rb") as f:
            st.download_button(
                "📥 Télécharger",
                f.read(),
                file_name=logo_path.name,
                mime="image/svg+xml" if logo_path.suffix == ".svg" else "image/png",
            )
    else:
        st.warning("⚠️ Fichier logo introuvable")

# Informations
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Statistiques")
stats = generator.get_stats()
if stats:
    st.sidebar.metric("Variantes disponibles", len(variants))
    st.sidebar.metric("Générateurs disponibles", len(generator_names))

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "🌙 Arkalia-LUNA Logo Generator v2.0.0"
    "</div>",
    unsafe_allow_html=True,
)
