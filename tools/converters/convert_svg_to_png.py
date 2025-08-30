#!/usr/bin/env python3
"""
Conversion des logos SVG ULTIMES en PNG
"""

import os
from pathlib import Path
from PIL import Image
import cairosvg


def convert_svg_to_png():
    """Convertit tous les logos SVG ULTIMES en PNG"""

    svg_dir = Path("exports-ultimate")
    if not svg_dir.exists():
        print("❌ Répertoire exports-ultimate non trouvé")
        return

    # Trouver tous les fichiers SVG
    svg_files = list(svg_dir.glob("*.svg"))
    print(f"🔍 {len(svg_files)} fichiers SVG trouvés")

    for svg_file in svg_files:
        if "ultimate" in svg_file.name:
            png_name = svg_file.stem + ".png"
            png_path = svg_dir / png_name

            print(f"🔄 Conversion de {svg_file.name} vers {png_name}")

            try:
                # Convertir SVG vers PNG avec cairosvg
                cairosvg.svg2png(
                    url=str(svg_file),
                    write_to=str(png_path),
                    output_width=200,
                    output_height=200,
                )
                print(f"✅ {png_name} créé avec succès")

            except Exception as e:
                print(f"❌ Erreur lors de la conversion de {svg_file.name}: {e}")

    print("\n🎉 Conversion terminée !")


if __name__ == "__main__":
    convert_svg_to_png()
