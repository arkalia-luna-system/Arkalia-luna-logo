#!/usr/bin/env python3
"""
Script pour générer des logos de démonstration pour le GIF animé
"""

import json
import time
from pathlib import Path

import requests

# Configuration
API_BASE = "http://localhost:8000"
OUTPUT_DIR = Path("exports/demo-gif")


def generate_logo(variant, size=200, generator_type="simple"):
    """Génère un logo via l'API"""
    url = f"{API_BASE}/generate"
    data = {"variant": variant, "size": size, "generator_type": generator_type}

    print(f"🎨 Génération logo {variant}...")
    start_time = time.time()

    response = requests.post(url, json=data)
    end_time = time.time()

    if response.status_code == 200:
        result = response.json()
        duration = end_time - start_time
        print(f"✅ {variant} généré en {duration:.3f}s")
        return result
    else:
        print(f"❌ Erreur génération {variant}: {response.status_code}")
        return None


def main():
    """Génère une série de logos pour le GIF"""
    print("🎬 Génération des logos pour le GIF animé...")

    # Créer le dossier de sortie
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Variantes à générer (dans l'ordre du GIF)
    variants = [
        "serenity",  # 1. Sérénité - calme
        "power",  # 2. Puissance - énergique
        "mystery",  # 3. Mystère - mystérieux
        "awakening",  # 4. Éveil - lumineux
        "creative",  # 5. Créatif - coloré
    ]

    results = []

    for i, variant in enumerate(variants, 1):
        print(f"\n📸 Logo {i}/5: {variant}")
        result = generate_logo(variant)
        if result:
            results.append(
                {
                    "variant": variant,
                    "file": result["file_path"],
                    "duration": result["generation_time"],
                }
            )

        # Pause entre les générations pour l'animation
        time.sleep(0.5)

    # Résumé
    print(f"\n🎉 {len(results)} logos générés avec succès !")
    print("📁 Fichiers dans exports/demo-gif/")

    # Sauvegarder la liste pour référence
    with open(OUTPUT_DIR / "generated_logos.json", "w") as f:
        json.dump(results, f, indent=2)

    return results


if __name__ == "__main__":
    main()
