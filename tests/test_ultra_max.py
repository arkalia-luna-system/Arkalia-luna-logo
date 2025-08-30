#!/usr/bin/env python3
"""
🌙 Test du système ULTRA-MAX Arkalia-LUNA Logo
Teste la génération de logos ULTRA-MAX avec effets EXCEPTIONNELS
"""

import sys
from pathlib import Path

# Ajout du répertoire src au path Python
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from src.ultra_max_generator import UltraMaxLogoGenerator

    print("✅ Import du générateur ULTRA-MAX réussi !")
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("💡 Assurez-vous que l'environnement virtuel est activé")
    sys.exit(1)


def test_ultra_max_generation():
    """Teste la génération ULTRA-MAX"""
    print("\n🚀 Test de la génération ULTRA-MAX Arkalia-LUNA Logo")
    print("=" * 70)

    try:
        # Initialisation du générateur ULTRA-MAX
        generator = UltraMaxLogoGenerator()
        print("✅ Générateur ULTRA-MAX initialisé")
        print(f"📁 Répertoire de sortie : {generator.get_output_directory()}")

        # Test de génération d'un logo ULTRA-MAX
        print("\n🎨 Test de génération d'un logo ULTRA-MAX...")
        output_path = generator.generate_ultra_max_logo("serenity", 200)
        print(f"✅ Logo ULTRA-MAX généré : {output_path}")

        # Test de génération de toutes les variantes
        print("\n🚀 Test de génération de toutes les variantes ULTRA-MAX...")
        all_logos = generator.generate_all_ultra_max_variants(200)
        print(f"✅ {len(all_logos)} logos ULTRA-MAX générés")

        # Test de création de favicons ULTRA-MAX
        print("\n🎯 Test de création de favicons ULTRA-MAX...")
        all_favicons = generator.create_all_ultra_max_favicons(32)
        print(f"✅ {len(all_favicons)} favicons ULTRA-MAX créés")

        # Affichage des statistiques
        print("\n📊 Statistiques de génération ULTRA-MAX :")
        stats = generator.get_ultra_max_generation_stats()
        for key, value in stats.items():
            print(f"  • {key}: {value}")

        # Comparaison avec toutes les versions
        print("\n🔍 Comparaison avec toutes les versions :")
        comparison = generator.compare_with_all_versions()
        for key, value in comparison.items():
            print(f"  • {key}: {value}")

        print("\n🎉 Tous les tests ULTRA-MAX ont réussi !")
        return True

    except Exception as e:
        print(f"❌ Erreur lors du test : {e}")
        return False


if __name__ == "__main__":
    success = test_ultra_max_generation()
    sys.exit(0 if success else 1)
