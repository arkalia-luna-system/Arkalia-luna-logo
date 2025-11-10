#!/usr/bin/env python3
"""🌙 Test du système avancé Arkalia-LUNA Logo
Teste la génération de logos ultra-avancés
"""

import sys
from pathlib import Path

# Ajout du répertoire src au path Python
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from src.advanced_logo_generator import AdvancedArkaliaLunaLogo

    print("✅ Import du générateur avancé réussi !")
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("💡 Assurez-vous que l'environnement virtuel est activé")
    sys.exit(1)


def test_advanced_generation():
    """Teste la génération avancée"""
    print("\n🚀 Test de la génération avancée Arkalia-LUNA Logo")
    print("=" * 60)

    try:
        # Initialisation du générateur avancé
        generator = AdvancedArkaliaLunaLogo()
        print("✅ Générateur avancé initialisé")
        print(f"📁 Répertoire de sortie : {generator.get_output_directory()}")

        # Test de génération d'un logo avancé
        print("\n🎨 Test de génération d'un logo avancé...")
        output_path = generator.generate_advanced_svg_logo("serenity", 200)
        print(f"✅ Logo avancé généré : {output_path}")

        # Test de génération de toutes les variantes
        print("\n🚀 Test de génération de toutes les variantes avancées...")
        all_logos = generator.generate_all_advanced_variants(200)
        print(f"✅ {len(all_logos)} logos avancés générés")

        # Test de création de favicons avancés
        print("\n🎯 Test de création de favicons avancés...")
        favicon_path = generator.create_advanced_favicon("serenity", 32)
        print(f"✅ Favicon avancé créé : {favicon_path}")

        # Affichage des statistiques
        print("\n📊 Statistiques de génération avancée :")
        stats = generator.get_advanced_stats()
        for key, value in stats.items():
            print(f"  • {key}: {value}")

        print("\n🎉 Tous les tests avancés ont réussi !")
        assert True, "Test réussi"

    except Exception as e:
        print(f"❌ Erreur lors du test : {e}")
        assert False, f"Test échoué : {e}"


if __name__ == "__main__":
    success = test_advanced_generation()
    sys.exit(0 if success else 1)
