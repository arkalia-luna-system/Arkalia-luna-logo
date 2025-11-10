#!/usr/bin/env python3
"""🌙 Test du système Dashboard Arkalia-LUNA Logo
Teste la génération de logos style dashboard/networking synthétique
"""

import sys
from pathlib import Path

# Ajout du répertoire src au path Python
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from src.dashboard_generator import DashboardLogoGenerator

    print("✅ Import du générateur dashboard réussi !")
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("💡 Assurez-vous que l'environnement virtuel est activé")
    sys.exit(1)


def test_dashboard_generation():
    """Teste la génération dashboard"""
    print("\n🚀 Test de la génération Dashboard Arkalia-LUNA Logo")
    print("=" * 65)

    try:
        # Initialisation du générateur dashboard
        generator = DashboardLogoGenerator()
        print("✅ Générateur dashboard initialisé")
        print(f"📁 Répertoire de sortie : {generator.get_output_directory()}")

        # Test de génération d'un logo dashboard
        print("\n🎨 Test de génération d'un logo dashboard...")
        output_path = generator.generate_dashboard_logo("serenity", 200)
        print(f"✅ Logo dashboard généré : {output_path}")

        # Test de génération de toutes les variantes
        print("\n🚀 Test de génération de toutes les variantes dashboard...")
        all_logos = generator.generate_all_dashboard_variants(200)
        print(f"✅ {len(all_logos)} logos dashboard générés")

        # Test de création de favicons dashboard
        print("\n🎯 Test de création de favicons dashboard...")
        favicon_path = generator.create_dashboard_favicon("serenity", 32)
        print(f"✅ Favicon dashboard créé : {favicon_path}")

        # Affichage des statistiques
        print("\n📊 Statistiques de génération dashboard :")
        stats = generator.get_generation_stats()
        for key, value in stats.items():
            print(f"  • {key}: {value}")

        print("\n🎉 Tous les tests dashboard ont réussi !")
        assert True, "Test réussi"

    except Exception as e:
        print(f"❌ Erreur lors du test : {e}")
        assert False, f"Test échoué : {e}"


if __name__ == "__main__":
    success = test_dashboard_generation()
    sys.exit(0 if success else 1)
