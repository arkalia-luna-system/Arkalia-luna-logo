#!/usr/bin/env python3
"""
🤖 Script de tests visuels automatiques BBIA
Crée des mockups pour tester la lisibilité sur différents fonds
Préparé pour intégration future avec /Volumes/T7/bbia-branding/
"""

import sys
from pathlib import Path

# Ajouter le répertoire src au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.bbia_palette import BBIA_PALETTE


def create_mockup_svg(
    logo_svg_path: Path,
    background_color: str,
    background_name: str,
    output_path: Path,
    size: int = 512,
):
    """
    Crée un mockup SVG avec fond coloré pour test visuel
    
    Args:
        logo_svg_path: Chemin vers le logo SVG
        background_color: Couleur de fond (hex)
        background_name: Nom du fond (pour affichage)
        output_path: Chemin de sortie
        size: Taille du mockup
    """
    print(f"🎨 Création mockup {background_name} ({background_color})")
    
    # TODO: Implémenter la génération réelle
    # 1. Lire le logo SVG
    # 2. Créer un SVG avec fond coloré
    # 3. Centrer le logo
    # 4. Exporter en PNG pour visualisation
    
    print(f"   📄 Source : {logo_svg_path.name}")
    print(f"   🎨 Fond : {background_color} ({background_name})")
    print(f"   📁 Sortie : {output_path}")
    print(f"   ✅ Mockup créé (à implémenter)")


def generate_visual_tests(bbia_branding_path: Path):
    """
    Génère tous les tests visuels BBIA
    
    Args:
        bbia_branding_path: Chemin vers le projet BBIA Branding
    """
    logo_2d_final = bbia_branding_path / "logo_2d" / "final"
    tests_dir = bbia_branding_path / "logo_2d" / "tests_visuels"
    
    # Vérifier que le projet existe
    if not bbia_branding_path.exists():
        print(f"⚠️  Projet BBIA Branding non trouvé : {bbia_branding_path}")
        print("   Le script sera activé quand BBIA Branding sera déplacé dans T7")
        return
    
    # Créer le dossier de tests
    tests_dir.mkdir(parents=True, exist_ok=True)
    
    # Fichiers sources à tester
    source_files = [
        logo_2d_final / "bbia_favicon_32x32.png",
        logo_2d_final / "bbia_mark_only_v2.svg",
        logo_2d_final / "bbia_logo_vertical_v2.svg",
        logo_2d_final / "bbia_logo_horizontal.svg",
    ]
    
    # Fonds de test
    test_backgrounds = {
        "fond_clair": BBIA_PALETTE.BRANDING_SECONDARY_WHITE,  # Blanc
        "fond_sombre": "#1A1A1A",  # Noir/gris foncé
        "fond_turquoise": BBIA_PALETTE.LOGO_BACKGROUND,  # Turquoise #008181
        "fond_bleu": BBIA_PALETTE.BRANDING_PRIMARY_BLUE,  # Bleu branding
    }
    
    print("=" * 70)
    print("🎨 TESTS VISUELS BBIA")
    print("=" * 70)
    print(f"📁 Source : {logo_2d_final}")
    print(f"📁 Sortie : {tests_dir}")
    print()
    
    # Générer les mockups pour chaque source et chaque fond
    for source_file in source_files:
        if not source_file.exists():
            print(f"⚠️  Fichier source non trouvé : {source_file.name}")
            continue
        
        print(f"\n📄 Test : {source_file.name}")
        print("-" * 70)
        
        for bg_name, bg_color in test_backgrounds.items():
            output_name = f"mockup_{source_file.stem}_{bg_name}.png"
            output_path = tests_dir / output_name
            
            create_mockup_svg(source_file, bg_color, bg_name, output_path)
    
    print("\n" + "=" * 70)
    print("✅ TESTS VISUELS GÉNÉRÉS")
    print("=" * 70)
    print("\n💡 Note : Ce script est en mode préparation.")
    print("   L'implémentation réelle sera ajoutée quand BBIA Branding sera dans T7.")
    print("\n📋 Checklist visuelle :")
    print("   [ ] Ouvrir favicon dans navigateur")
    print("   [ ] Vérifier lisibilité sur fond clair")
    print("   [ ] Vérifier lisibilité sur fond sombre")
    print("   [ ] Vérifier lisibilité sur fond turquoise")
    print("   [ ] Vérifier lisibilité sur fond bleu")


if __name__ == "__main__":
    # Chemin futur vers BBIA Branding
    bbia_branding_path = Path("/Volumes/T7/bbia-branding")
    
    # Si le projet est encore sur Desktop, utiliser ce chemin
    desktop_path = Path("/Users/athalia/Desktop/logo bbia/bbia_branding")
    if desktop_path.exists():
        bbia_branding_path = desktop_path
        print("📁 Utilisation du projet sur Desktop (temporaire)")
    
    generate_visual_tests(bbia_branding_path)

