#!/usr/bin/env python3
"""
🌙 Test du système LUNE IA Arkalia-LUNA Logo
Teste la génération de logos LUNE IA VIVANTE ultra-réalistes
"""

import sys
from pathlib import Path

# Ajout du répertoire src au path Python
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from src.ai_moon_generator import AIMoonLogoGenerator

    print("✅ Import du générateur LUNE IA réussi !")
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("💡 Assurez-vous que l'environnement virtuel est activé")
    sys.exit(1)


def test_ai_moon_generation():
    """Teste la génération LUNE IA"""
    print("\n🌙 Test de la génération LUNE IA Arkalia-LUNA Logo")
    print("=" * 70)

    try:
        # Initialisation du générateur LUNE IA
        generator = AIMoonLogoGenerator()
        print("✅ Générateur LUNE IA initialisé")
        print(f"📁 Répertoire de sortie : {generator.get_output_directory()}")

        # Test de génération d'un logo LUNE IA
        print("\n🎨 Test de génération d'un logo LUNE IA...")
        output_path = generator.generate_ai_moon_logo("serenity", 200)
        print(f"✅ Logo LUNE IA généré : {output_path}")

        # Test de génération de toutes les variantes
        print("\n🚀 Test de génération de toutes les variantes LUNE IA...")
        all_logos = generator.generate_all_ai_moon_variants(200)
        print(f"✅ {len(all_logos)} logos LUNE IA générés")

        # Test de création de favicons LUNE IA
        print("\n🎯 Test de création de favicons LUNE IA...")
        favicon_path = generator.create_ai_moon_favicon("serenity", 32)
        print(f"✅ Favicon LUNE IA créé : {favicon_path}")

        # Affichage des statistiques
        print("\n📊 Statistiques de génération LUNE IA :")
        stats = generator.get_generation_stats()
        for key, value in stats.items():
            print(f"  • {key}: {value}")

        print("\n🎉 Tous les tests LUNE IA ont réussi !")
        assert True, "Test réussi"

    except Exception as e:
        print(f"❌ Erreur lors du test : {e}")
        assert False, f"Test échoué : {e}"


if __name__ == "__main__":
    success = test_ai_moon_generation()
    sys.exit(0 if success else 1)
