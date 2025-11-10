#!/usr/bin/env python3
"""🌙 Test du système avancé simplifié Arkalia-LUNA Logo
Teste la génération de logos avancés simplifiés
"""

import sys
from pathlib import Path

# Ajout du répertoire src au path Python
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from src.simple_advanced_generator import SimpleAdvancedLogoGenerator

    print("✅ Import du générateur avancé simplifié réussi !")
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("💡 Assurez-vous que l'environnement virtuel est activé")
    sys.exit(1)


def test_simple_advanced_generation():
    """Teste la génération avancée simplifiée"""
    print("\n🚀 Test de la génération avancée simplifiée Arkalia-LUNA Logo")
    print("=" * 70)

    try:
        # Initialisation du générateur avancé simplifié
        generator = SimpleAdvancedLogoGenerator()
        print("✅ Générateur avancé simplifié initialisé")
        print(f"📁 Répertoire de sortie : {generator.get_output_directory()}")

        # Test de génération d'un logo avancé simplifié
        print("\n🎨 Test de génération d'un logo avancé simplifié...")
        output_path = generator.generate_simple_advanced_logo("serenity", 200)
        print(f"✅ Logo avancé simplifié généré : {output_path}")

        # Test de génération de toutes les variantes
        print("\n🚀 Test de génération de toutes les variantes avancées simplifiées...")
        all_logos = generator.generate_all_simple_advanced_variants(200)
        print(f"✅ {len(all_logos)} logos avancés simplifiés générés")

        # Test de création de favicons avancés simplifiés
        print("\n🎯 Test de création de favicons avancés simplifiés...")
        favicon_path = generator.create_simple_advanced_favicon("serenity", 32)
        print(f"✅ Favicon avancé simplifié créé : {favicon_path}")

        # Affichage des statistiques
        print("\n📊 Statistiques de génération avancée simplifiée :")
        stats = generator.get_generation_stats()
        for key, value in stats.items():
            print(f"  • {key}: {value}")

        print("\n🎉 Tous les tests avancés simplifiés ont réussi !")
        assert True, "Test réussi"

    except Exception as e:
        print(f"❌ Erreur lors du test : {e}")
        assert False, f"Test échoué : {e}"


if __name__ == "__main__":
    success = test_simple_advanced_generation()
    sys.exit(0 if success else 1)
