#!/usr/bin/env python3
import os
import subprocess


def convert_svg_to_png():
    """Convertit les SVG en PNG avec rsvg-convert"""

    svg_dir = "exports-ultimate"

    # Vérifier si rsvg-convert est disponible
    try:
        subprocess.run(["rsvg-convert", "--version"], capture_output=True, check=True)
        print("✅ rsvg-convert disponible")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ rsvg-convert non disponible, utilisation de cairosvg")
        use_cairosvg = True
    else:
        use_cairosvg = False

    # Lister tous les fichiers SVG
    svg_files = [
        f for f in os.listdir(svg_dir) if f.endswith(".svg") and "ultimate" in f
    ]
    print(f"🔍 {len(svg_files)} fichiers SVG trouvés")

    for svg_file in svg_files:
        if "ultimate" in svg_file and not svg_file.startswith("favicon"):
            png_name = svg_file.replace(".svg", ".png")
            svg_path = os.path.join(svg_dir, svg_file)
            png_path = os.path.join(svg_dir, png_name)

            print(f"🔄 Conversion de {svg_file} vers {png_name}")

            try:
                if use_cairosvg:
                    # Utiliser cairosvg
                    import cairosvg

                    cairosvg.svg2png(
                        url=svg_path,
                        write_to=png_path,
                        output_width=200,
                        output_height=200,
                    )
                else:
                    # Utiliser rsvg-convert
                    subprocess.run(
                        [
                            "rsvg-convert",
                            "-w",
                            "200",
                            "-h",
                            "200",
                            svg_path,
                            "-o",
                            png_path,
                        ],
                        check=True,
                    )

                print(f"✅ {png_name} créé avec succès")

            except Exception as e:
                print(f"❌ Erreur lors de la conversion de {svg_file}: {e}")

    print("\n🎉 Conversion terminée !")


if __name__ == "__main__":
    convert_svg_to_png()
