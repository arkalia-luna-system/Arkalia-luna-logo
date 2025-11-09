#!/usr/bin/env python3
"""
Script pour générer des logos avec les nouvelles variantes émotionnelles
"""

import subprocess
from pathlib import Path


def generate_emotional_logos():
    """Génère des logos avec les nouvelles variantes émotionnelles"""

    # Créer le dossier de sortie
    output_dir = Path("exports/emotional")
    output_dir.mkdir(exist_ok=True)

    # Nouvelles variantes émotionnelles
    emotional_variants = [
        "rainy",  # 🌧️ Pluie/Gris
        "stormy",  # ⚡ Orage/Colère
        "explosive",  # 💥 Vive/Explosion
        "sunny",  # ☀️ Ensoleillé
        "snowy",  # ❄️ Neige
    ]

    # Générateurs disponibles
    generators = [
        "default",
        "dashboard",
        "ai_moon",
        "advanced",
        "simple_advanced",
        "ultra_max",
        "realism",
        "ultimate",
    ]

    print("🎨 Génération des logos émotionnels...")
    print(f"📁 Dossier de sortie: {output_dir}")
    total_logos = len(emotional_variants) * len(generators)
    print(
        f"🎯 {len(emotional_variants)} variantes × {len(generators)} "
        f"générateurs = {total_logos} logos"
    )
    print()

    generated_count = 0
    errors = []

    for variant in emotional_variants:
        print(f"🌧️⚡💥☀️❄️ Génération de la variante: {variant}")

        for generator in generators:
            try:
                # Nom du fichier de sortie
                filename = f"{generator}-{variant}-200.svg"
                output_path = output_dir / filename

                # Commande CLI pour générer le logo
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
                    generator,
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
                error_msg = f"Exception pour {generator}-{variant}: {e}"
                print(f"  ❌ {error_msg}")
                errors.append(error_msg)

    print()
    print("📊 Résumé de la génération émotionnelle:")
    print(f"✅ Logos générés: {generated_count}")
    print(f"❌ Erreurs: {len(errors)}")

    if errors:
        print("\n🔍 Erreurs détaillées:")
        for error in errors:
            print(f"  - {error}")

    print(f"\n🎉 Logos émotionnels disponibles dans: {output_dir}")
    return generated_count, errors


if __name__ == "__main__":
    generate_emotional_logos()
