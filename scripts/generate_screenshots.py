#!/usr/bin/env python3
"""
Script pour générer des screenshots comparatifs des 8 styles de logos
"""

import subprocess
from pathlib import Path


def generate_screenshots():
    """Génère des screenshots de tous les styles et variantes"""

    # Créer le dossier de sortie
    output_dir = Path("exports/screenshots")
    output_dir.mkdir(exist_ok=True)

    # Styles disponibles (correspondant aux générateurs)
    styles = [
        "default",  # Logo de base (simple)
        "dashboard",  # Dashboard
        "ai_moon",  # AI-Moon
        "advanced",  # Advanced
        "simple_advanced",  # Simple-Advanced
        "ultra_max",  # Ultra-Max
        "realism",  # Realism Max (pas realism_max)
        "ultimate",  # Ultimate
    ]

    # Variantes émotionnelles
    variants = [
        "serenity",  # Sérénité
        "power",  # Puissance
        "mystery",  # Mystère
        "awakening",  # Éveil/Sagesse
        "creative",  # Énergie créative
    ]

    print("🎨 Génération des screenshots comparatifs...")
    print(f"📁 Dossier de sortie: {output_dir}")
    print(
        f"🎯 {len(styles)} styles × {len(variants)} variantes = {len(styles) * len(variants)} logos"
    )
    print()

    generated_count = 0
    errors = []

    for style in styles:
        print(f"🔄 Génération du style: {style}")

        for variant in variants:
            try:
                # Nom du fichier de sortie (mapping pour affichage)
                style_display = "simple" if style == "default" else style
                filename = f"{style_display}-{variant}-200.svg"
                output_path = output_dir / filename

                # Commande CLI pour générer le logo avec le générateur spécialisé
                cmd = [
                    "python",
                    "-m",
                    "src.cli",
                    "generate",
                    "--variant",
                    variant,
                    "--size",
                    "200",
                    "--generator",
                    style,
                    "--output",
                    str(output_path),
                ]

                # Exécuter la commande
                result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")

                if result.returncode == 0:
                    print(f"  ✅ {filename}")
                    generated_count += 1
                else:
                    error_msg = f"Erreur CLI pour {filename}: {result.stderr}"
                    print(f"  ❌ {error_msg}")
                    errors.append(error_msg)

            except Exception as e:
                error_msg = f"Exception pour {style}-{variant}: {e}"
                print(f"  ❌ {error_msg}")
                errors.append(error_msg)

    print()
    print("📊 Résumé de la génération:")
    print(f"✅ Logos générés: {generated_count}")
    print(f"❌ Erreurs: {len(errors)}")

    if errors:
        print("\n🔍 Erreurs détaillées:")
        for error in errors:
            print(f"  - {error}")

    print(f"\n🎉 Screenshots disponibles dans: {output_dir}")
    return generated_count, errors


if __name__ == "__main__":
    generate_screenshots()
