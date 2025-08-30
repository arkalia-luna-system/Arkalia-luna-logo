#!/usr/bin/env python3
"""
🌙 Test Simplifié du système ULTRA-MAX Arkalia-LUNA Logo
Teste la génération de logos ULTRA-MAX avec effets EXCEPTIONNELS
"""

import sys
from pathlib import Path

# Ajout du répertoire src au path Python
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from src.svg_builder_ultra_max import UltraMaxSVGBuilder
    from src.variants import LogoVariants

    print("✅ Import des modules ULTRA-MAX réussi !")
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("💡 Assurez-vous que l'environnement virtuel est activé")
    sys.exit(1)


def test_ultra_max_builder():
    """Teste le builder ULTRA-MAX directement"""
    print("\n🚀 Test du Builder ULTRA-MAX Arkalia-LUNA Logo")
    print("=" * 70)

    try:
        # Initialisation des composants
        variants_manager = LogoVariants()
        svg_builder = UltraMaxSVGBuilder(variants_manager)
        print("✅ Builder ULTRA-MAX initialisé")

        # Test de création d'un dessin
        print("\n🎨 Test de création d'un dessin ULTRA-MAX...")
        drawing = svg_builder.create_drawing(200)
        assert drawing is not None, "Le dessin doit être créé"
        print("✅ Dessin ULTRA-MAX créé")

        # Test de construction d'un logo
        print("\n🚀 Test de construction d'un logo ULTRA-MAX...")
        logo = svg_builder.build_ultra_max_logo("serenity", 200)
        assert logo is not None, "Le logo doit être construit"
        print("✅ Logo ULTRA-MAX construit")

        # Test de sauvegarde
        print("\n💾 Test de sauvegarde ULTRA-MAX...")
        output_path = Path("test-ultra-max.svg")
        svg_builder.save_ultra_max_logo("serenity", 200, output_path)
        print(f"✅ Logo ULTRA-MAX sauvegardé : {output_path}")

        # Nettoyage
        if output_path.exists():
            output_path.unlink()
            print("🧹 Fichier de test supprimé")

        print("\n🎉 Tous les tests ULTRA-MAX ont réussi !")
        assert True, "Test réussi"

    except Exception as e:
        print(f"❌ Erreur lors du test : {e}")
        import traceback

        traceback.print_exc()
        assert False, f"Test échoué : {e}"


if __name__ == "__main__":
    success = test_ultra_max_builder()
    sys.exit(0 if success else 1)
