#!/usr/bin/env python3
"""
🌙 Arkalia-LUNA Logo Generator
Générateur de logo techno-mystique avec variantes émotionnelles
"""

from pathlib import Path
from typing import List

import click
import svgwrite
from dotenv import load_dotenv
from PIL import Image, ImageDraw
from rich.console import Console
from rich.progress import track
from rich.table import Table

# Configuration
load_dotenv()
console = Console()


class ArkaliaLunaLogo:
    """Générateur de logo Arkalia-LUNA avec variantes émotionnelles"""

    def __init__(self):
        self.variants = {
            "serenity": {
                "name": "🌙 Sérénité",
                "colors": {
                    "primary": "#1e3a8a",
                    "secondary": "#3b82f6",
                    "accent": "#06b6d4",
                    "glow": "#60a5fa",
                },
                "description": "Halo doux, pulsations lentes, ambiance calme et mystique",
            },
            "power": {
                "name": "⚡ Puissance",
                "colors": {
                    "primary": "#1e40af",
                    "secondary": "#7c3aed",
                    "accent": "#ec4899",
                    "glow": "#a855f7",
                },
                "description": "Halo vibrant, réseau accéléré, énergie intense",
            },
            "mystery": {
                "name": "🔮 Mystère",
                "colors": {
                    "primary": "#312e81",
                    "secondary": "#4c1d95",
                    "accent": "#7c2d12",
                    "glow": "#581c87",
                },
                "description": "Brumes mouvantes, réseau irrégulier, ambiance mystérieuse",
            },
            "awakening": {
                "name": "✨ Éveil/Sagesse",
                "colors": {
                    "primary": "#0f766e",
                    "secondary": "#059669",
                    "accent": "#d97706",
                    "glow": "#10b981",
                },
                "description": "Halo rayonnant, Λ-core clair, sagesse éclairée",
            },
            "creative": {
                "name": "🎇 Énergie créative",
                "colors": {
                    "primary": "#1e40af",
                    "secondary": "#06b6d4",
                    "accent": "#ec4899",
                    "glow": "#f59e0b",
                },
                "description": "Flux rapides, reflets multicolores, créativité débordante",
            },
        }

        self.output_dir = Path("exports")
        self.output_dir.mkdir(exist_ok=True)

    def generate_svg_logo(self, variant: str, size: int = 200) -> str:
        """Génère le logo SVG pour une variante donnée"""
        if variant not in self.variants:
            raise ValueError(f"Variante '{variant}' non reconnue")

        colors = self.variants[variant]["colors"]

        # Création du SVG
        dwg = svgwrite.Drawing(size=(size, size), viewBox=f"0 0 {size} {size}")

        # Définitions (gradients, filtres)
        defs = dwg.defs()

        # Gradient pour la lune
        moon_gradient = dwg.radialGradient(
            id=f"moonGradient-{variant}", cx="50%", cy="50%", r="50%"
        )
        moon_gradient.add_stop_color(offset="0%", color=colors["primary"])
        moon_gradient.add_stop_color(offset="50%", color=colors["secondary"])
        moon_gradient.add_stop_color(offset="100%", color=colors["accent"])
        defs.add(moon_gradient)

        # Filtre de lueur
        glow_filter = dwg.filter(id=f"glow-{variant}")
        fe_gaussian_blur = dwg.feGaussianBlur(stdDeviation="2")
        glow_filter.add(fe_gaussian_blur)
        defs.add(glow_filter)

        # Halo respirant
        halo = dwg.circle(
            center=(size // 2, size // 2),
            r=size // 2 - 10,
            fill="none",
            stroke=colors["glow"],
            stroke_width=2,
            opacity=0.7,
            filter=f"url(#glow-{variant})",
        )
        dwg.add(halo)

        # Lune principale
        moon = dwg.circle(
            center=(size // 2, size // 2),
            r=size // 3,
            fill=f"url(#moonGradient-{variant})",
            filter=f"url(#glow-{variant})",
        )
        dwg.add(moon)

        # Réseau neuronal
        network_group = dwg.g(fill="none", stroke=colors["accent"], stroke_width=2)

        # Réseau principal
        network_paths = [
            f"M{size//3} {size//2} Q{size//2} {size//3} {2*size//3} {size//2}",
            f"M{size//3 + 10} {size//2 - 10} Q{size//2} {size//3 - 10} {2*size//3 - 10} {size//2 - 10}",
            f"M{size//3 + 20} {size//2 + 10} Q{size//2} {size//3 + 10} {2*size//3 - 20} {size//2 + 10}",
        ]

        for path_data in network_paths:
            path = dwg.path(d=path_data, opacity=0.8)
            network_group.add(path)

        dwg.add(network_group)

        # Λ-core cristallin
        lambda_core = dwg.g(fill=colors["glow"])

        # Forme Λ
        lambda_shape = dwg.path(
            d=f"M{size//2 - 10} {size//2 - 15} L{size//2} {size//2 - 5} L{size//2 + 10} {size//2 - 15} L{size//2} {size//2} Z"
        )
        lambda_core.add(lambda_shape)

        # Rayonnement central
        core_glow = dwg.circle(
            center=(size // 2, size // 2 - 5), r=5, fill=colors["glow"], opacity=0.9
        )
        lambda_core.add(core_glow)

        dwg.add(lambda_core)

        return dwg

    def generate_all_variants(self, size: int = 200) -> List[str]:
        """Génère toutes les variantes du logo"""
        console.print(
            "[bold blue]🎨 Génération de toutes les variantes Arkalia-LUNA...[/bold blue]"
        )

        generated_files = []

        for variant in track(self.variants.keys(), description="Génération des logos"):
            try:
                svg = self.generate_svg_logo(variant, size)
                filename = f"arkalia-luna-{variant}.svg"
                svg.saveas(filename)

                generated_files.append(filename)
                console.print(
                    f"[green]✅[/green] {self.variants[variant]['name']} généré : {filename}"
                )

            except Exception as e:
                console.print(f"[red]❌[/red] Erreur pour {variant}: {e}")

        return generated_files

    def show_variants_info(self):
        """Affiche les informations sur toutes les variantes"""
        table = Table(title="🌙 Variantes Émotionnelles Arkalia-LUNA")

        table.add_column("Variante", style="cyan", no_wrap=True)
        table.add_column("Nom", style="magenta")
        table.add_column("Description", style="green")
        table.add_column("Couleurs", style="yellow")

        for key, variant in self.variants.items():
            colors_str = ", ".join([f"{k}: {v}" for k, v in variant["colors"].items()])
            table.add_row(key, variant["name"], variant["description"], colors_str)

        console.print(table)

    def create_favicon(self, variant: str = "serenity", size: int = 32) -> str:
        """Crée un favicon pour la variante donnée"""
        colors = self.variants[variant]["colors"]

        # Création de l'image PIL
        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Lune principale
        center = size // 2
        radius = size // 3

        # Gradient simple (cercle avec couleur principale)
        draw.ellipse(
            [center - radius, center - radius, center + radius, center + radius],
            fill=colors["primary"],
        )

        # Λ-core simplifié
        draw.polygon(
            [center - 3, center - 5, center, center + 3, center - 3, center - 5],
            fill=colors["glow"],
        )

        filename = f"favicon-{variant}.png"
        img.save(filename, "PNG")

        return filename


@click.group()
def cli():
    """🌙 Arkalia-LUNA Logo Generator CLI"""
    pass


@cli.command()
@click.option("--variant", "-v", default="serenity", help="Variante émotionnelle")
@click.option("--size", "-s", default=200, help="Taille du logo en pixels")
def generate(variant: str, size: int):
    """Génère un logo pour une variante spécifique"""
    logo_gen = ArkaliaLunaLogo()

    try:
        svg = logo_gen.generate_svg_logo(variant, size)
        filename = f"arkalia-luna-{variant}.svg"
        svg.saveas(filename)

        console.print("[bold green]✅ Logo généré avec succès ![/bold green]")
        console.print(f"📁 Fichier : {filename}")
        console.print(f"🎨 Variante : {logo_gen.variants[variant]['name']}")
        console.print(f"📏 Taille : {size}x{size} pixels")

    except Exception as e:
        console.print(f"[bold red]❌ Erreur : {e}[/bold red]")


@cli.command()
@click.option("--size", "-s", default=200, help="Taille des logos en pixels")
def generate_all(size: int):
    """Génère toutes les variantes du logo"""
    logo_gen = ArkaliaLunaLogo()
    generated_files = logo_gen.generate_all_variants(size)

    console.print("\n[bold green]🎉 Génération terminée ![/bold green]")
    console.print(f"📁 {len(generated_files)} logos générés :")

    for filename in generated_files:
        console.print(f"  • {filename}")


@cli.command()
def info():
    """Affiche les informations sur toutes les variantes"""
    logo_gen = ArkaliaLunaLogo()
    logo_gen.show_variants_info()


@cli.command()
@click.option("--variant", "-v", default="serenity", help="Variante émotionnelle")
@click.option("--size", "-s", default=32, help="Taille du favicon en pixels")
def favicon(variant: str, size: int):
    """Crée un favicon pour une variante"""
    logo_gen = ArkaliaLunaLogo()

    try:
        filename = logo_gen.create_favicon(variant, size)
        console.print("[bold green]✅ Favicon généré ![/bold green]")
        console.print(f"📁 Fichier : {filename}")
        console.print(f"🎨 Variante : {logo_gen.variants[variant]['name']}")
        console.print(f"📏 Taille : {size}x{size} pixels")

    except Exception as e:
        console.print(f"[bold red]❌ Erreur : {e}[/bold red]")


if __name__ == "__main__":
    cli()
