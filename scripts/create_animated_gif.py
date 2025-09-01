#!/usr/bin/env python3
"""
Script pour créer un GIF animé montrant la génération de logos
"""

import json
import subprocess
from pathlib import Path


def create_gif_from_svgs():
    """Crée un GIF animé à partir des SVGs générés"""

    # Dossier de sortie
    output_dir = Path("exports/demo-gif")
    output_dir.mkdir(exist_ok=True)

    # Lire la liste des logos générés
    logos_file = output_dir / "generated_logos.json"
    if not logos_file.exists():
        print("❌ Fichier generated_logos.json non trouvé")
        return False

    with open(logos_file) as f:
        logos = json.load(f)

    print(f"🎬 Création du GIF animé avec {len(logos)} logos...")

    # Convertir les SVGs en PNG pour le GIF
    png_files = []

    for i, logo in enumerate(logos):
        svg_file = Path(logo["file"])
        png_file = output_dir / f"frame_{i:02d}_{logo['variant']}.png"

        print(f"🖼️  Conversion {logo['variant']} -> PNG...")

        # Convertir SVG en PNG avec rsvg-convert ou Inkscape
        try:
            # Essayer rsvg-convert d'abord
            cmd = [
                "rsvg-convert",
                "-w",
                "400",  # Largeur
                "-h",
                "400",  # Hauteur
                "-o",
                str(png_file),
                str(svg_file),
            ]
            subprocess.run(cmd, check=True, capture_output=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            try:
                # Essayer Inkscape
                cmd = [
                    "inkscape",
                    "--export-type=png",
                    f"--export-filename={png_file}",
                    "--export-width=400",
                    "--export-height=400",
                    str(svg_file),
                ]
                subprocess.run(cmd, check=True, capture_output=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                print(f"❌ Impossible de convertir {svg_file}")
                continue

        png_files.append(png_file)

    if not png_files:
        print("❌ Aucun PNG généré")
        return False

    # Créer le GIF animé avec FFmpeg
    gif_file = output_dir / "arkalia-luna-logo-demo.gif"

    print("🎬 Création du GIF animé...")

    # Créer une liste de fichiers pour FFmpeg
    file_list = output_dir / "file_list.txt"
    with open(file_list, "w") as f:
        for png_file in png_files:
            f.write(f"file '{png_file.absolute()}'\n")
            f.write("duration 1.5\n")  # 1.5 secondes par frame

    # Commande FFmpeg pour créer le GIF
    cmd = [
        "ffmpeg",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(file_list),
        "-vf",
        "fps=10,scale=400:400:flags=lanczos,palettegen",
        "-y",  # Overwrite output
        str(gif_file),
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✅ GIF créé : {gif_file}")

        # Nettoyer les fichiers temporaires
        file_list.unlink()
        for png_file in png_files:
            png_file.unlink()

        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur FFmpeg : {e}")
        return False


def create_simple_gif():
    """Crée un GIF simple avec les logos existants"""

    print("🎬 Création d'un GIF simple...")

    # Utiliser les logos existants dans exports/
    logo_files = [
        "exports/arkalia-luna-serenity-200.svg",
        "exports/arkalia-luna-power-200.svg",
        "exports/arkalia-luna-mystery-200.svg",
        "exports/arkalia-luna-dashboard-awakening-200.svg",
        "exports/arkalia-luna-dashboard-creative-200.svg",
    ]

    output_dir = Path("exports/demo-gif")
    output_dir.mkdir(exist_ok=True)

    # Convertir en PNG
    png_files = []
    for i, logo_file in enumerate(logo_files):
        if Path(logo_file).exists():
            png_file = output_dir / f"frame_{i:02d}.png"

            # Convertir avec rsvg-convert
            try:
                cmd = [
                    "rsvg-convert",
                    "-w",
                    "400",
                    "-h",
                    "400",
                    "-o",
                    str(png_file),
                    logo_file,
                ]
                subprocess.run(cmd, check=True, capture_output=True)
                png_files.append(png_file)
                print(f"✅ Frame {i+1} converti")
            except Exception as e:
                print(f"❌ Erreur conversion frame {i+1}: {e}")

    if png_files:
        # Créer le GIF
        gif_file = output_dir / "arkalia-luna-demo.gif"

        # Commande FFmpeg simple
        cmd = [
            "ffmpeg",
            "-framerate",
            "0.5",  # 2 secondes par frame
            "-i",
            str(output_dir / "frame_%02d.png"),
            "-vf",
            "scale=400:400:flags=lanczos",
            "-y",
            str(gif_file),
        ]

        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"🎉 GIF créé : {gif_file}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur FFmpeg : {e}")

    return False


def main():
    """Fonction principale"""
    print("🎬 Création du GIF animé Arkalia-LUNA...")

    # Essayer d'abord la méthode complète
    if create_gif_from_svgs():
        print("✅ GIF créé avec succès !")
    else:
        print("⚠️  Méthode complète échouée, essai méthode simple...")
        if create_simple_gif():
            print("✅ GIF simple créé !")
        else:
            print("❌ Impossible de créer le GIF")


if __name__ == "__main__":
    main()
