#!/usr/bin/env python3
"""
🤖 Script de génération automatique des déclinaisons BBIA
Génère toutes les déclinaisons dimensionnelles
(Square 1:1, Landscape 16:9, Portrait 9:16)
Préparé pour intégration future avec /Volumes/T7/bbia-branding/
"""

import sys
from pathlib import Path

# Ajouter le répertoire src au path
sys.path.insert(0, str(Path(__file__).parent.parent))


def generate_square_1_1(
    source_svg: Path, output_dir: Path, sizes: Optional[List[int]] = None
):
    """
    Génère les déclinaisons Square 1:1 (réseaux sociaux)

    Args:
        source_svg: Chemin vers le SVG source
        output_dir: Répertoire de sortie
        sizes: Liste des tailles à générer
    """
    print(f"📐 Génération Square 1:1 depuis {source_svg.name}")

    # TODO: Implémenter la génération réelle
    # 1. Lire le SVG source
    # 2. Redimensionner en carré 1:1
    # 3. Exporter en PNG aux tailles spécifiées
    # 4. Exporter en WebP pour optimisation

    for size in sizes:
        output_path = output_dir / f"bbia_square_1_1_{size}x{size}.png"
        print(f"   ✅ {output_path.name} (à générer)")

    print(f"   📁 Dossier : {output_dir}")


def generate_landscape_16_9(source_svg: Path, output_dir: Path, width: int = 1920):
    """
    Génère les déclinaisons Landscape 16:9 (site, GitHub)

    Args:
        source_svg: Chemin vers le SVG source
        output_dir: Répertoire de sortie
        width: Largeur cible (hauteur calculée automatiquement)
    """
    height = int(width * 9 / 16)
    print(f"📐 Génération Landscape 16:9 ({width}x{height}) depuis {source_svg.name}")

    # TODO: Implémenter la génération réelle
    # 1. Lire le SVG source
    # 2. Redimensionner en 16:9
    # 3. Exporter en PNG, JPG, WebP

    formats = ["png", "jpg", "webp"]
    for fmt in formats:
        output_path = output_dir / f"bbia_landscape_16_9_{width}x{height}.{fmt}"
        print(f"   ✅ {output_path.name} (à générer)")

    print(f"   📁 Dossier : {output_dir}")


def generate_portrait_9_16(source_svg: Path, output_dir: Path, height: int = 1920):
    """
    Génère les déclinaisons Portrait 9:16 (optionnel)

    Args:
        source_svg: Chemin vers le SVG source
        output_dir: Répertoire de sortie
        height: Hauteur cible (largeur calculée automatiquement)
    """
    width = int(height * 9 / 16)
    print(f"📐 Génération Portrait 9:16 ({width}x{height}) depuis {source_svg.name}")

    # TODO: Implémenter la génération réelle
    # 1. Lire le SVG source
    # 2. Redimensionner en 9:16
    # 3. Exporter en PNG, JPG, WebP

    formats = ["png", "jpg", "webp"]
    for fmt in formats:
        output_path = output_dir / f"bbia_portrait_9_16_{width}x{height}.{fmt}"
        print(f"   ✅ {output_path.name} (à générer)")

    print(f"   📁 Dossier : {output_dir}")


def generate_all_declinations(bbia_branding_path: Path):
    """
    Génère toutes les déclinaisons BBIA

    Args:
        bbia_branding_path: Chemin vers le projet BBIA Branding
    """
    logo_2d_final = bbia_branding_path / "logo_2d" / "final"
    variants_dir = bbia_branding_path / "variants"

    # Vérifier que le projet existe
    if not bbia_branding_path.exists():
        print(f"⚠️  Projet BBIA Branding non trouvé : {bbia_branding_path}")
        print("   Le script sera activé quand BBIA Branding sera déplacé dans T7")
        return

    # Créer les dossiers de sortie
    square_dir = variants_dir / "square_1_1"
    landscape_dir = variants_dir / "landscape_16_9"
    portrait_dir = variants_dir / "portrait_9_16"

    square_dir.mkdir(parents=True, exist_ok=True)
    landscape_dir.mkdir(parents=True, exist_ok=True)
    portrait_dir.mkdir(parents=True, exist_ok=True)

    # Fichiers sources disponibles
    source_files = [
        logo_2d_final / "bbia_mark_only_v2.svg",
        logo_2d_final / "bbia_logo_vertical_v2.svg",
        logo_2d_final / "bbia_logo_horizontal.svg",
    ]

    print("=" * 70)
    print("🤖 GÉNÉRATION DÉCLINAISONS BBIA")
    print("=" * 70)
    print(f"📁 Source : {logo_2d_final}")
    print(f"📁 Sortie : {variants_dir}")
    print()

    # Générer pour chaque source
    for source_svg in source_files:
        if not source_svg.exists():
            print(f"⚠️  Fichier source non trouvé : {source_svg.name}")
            continue

        print(f"\n📄 Traitement : {source_svg.name}")
        print("-" * 70)

        # Square 1:1
        generate_square_1_1(source_svg, square_dir)

        # Landscape 16:9
        generate_landscape_16_9(source_svg, landscape_dir)

        # Portrait 9:16
        generate_portrait_9_16(source_svg, portrait_dir)

    print("\n" + "=" * 70)
    print("✅ GÉNÉRATION TERMINÉE")
    print("=" * 70)
    print("\n💡 Note : Ce script est en mode préparation.")
    print("   L'implémentation réelle sera ajoutée quand BBIA Branding sera dans T7.")


if __name__ == "__main__":
    # Chemin futur vers BBIA Branding
    bbia_branding_path = Path("/Volumes/T7/bbia-branding")

    # Si le projet est encore sur Desktop, utiliser ce chemin
    desktop_path = Path("/Users/athalia/Desktop/logo bbia/bbia_branding")
    if desktop_path.exists():
        bbia_branding_path = desktop_path
        print("📁 Utilisation du projet sur Desktop (temporaire)")

    generate_all_declinations(bbia_branding_path)
