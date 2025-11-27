"""🌙 CLI Module pour Arkalia-LUNA Logo Generator
Interface en ligne de commande pour la génération de logos
"""

import sys
from pathlib import Path
from typing import Optional

import click
from click import Context
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.table import Table
from rich.text import Text

from .generator_factory import LogoGeneratorFactory
from .logo_generator import ArkaliaLunaLogo

# Configuration Rich
console = Console()


def print_banner() -> None:
    """Affiche la bannière Arkalia-LUNA"""
    banner = Text()
    banner.append("🌙 ", style="bold blue")
    banner.append("Arkalia-LUNA Logo Generator", style="bold white")
    banner.append(" v2.0.0", style="dim white")

    panel = Panel(banner, border_style="blue", padding=(1, 2))
    console.print(panel)


def print_error(message: str) -> None:
    """Affiche une erreur formatée"""
    console.print(f"[bold red]❌ Erreur :[/bold red] {message}")


def print_success(message: str) -> None:
    """Affiche un succès formaté"""
    console.print(f"[bold green]✅ Succès :[/bold green] {message}")


def print_info(message: str) -> None:
    """Affiche une information formatée"""
    console.print(f"[bold blue]Info :[/bold blue] {message}")


@click.group()
@click.option(
    "--output-dir",
    "-o",
    type=click.Path(),
    help="Répertoire de sortie personnalisé",
)
@click.option("--verbose", "-v", is_flag=True, help="Mode verbeux")
@click.pass_context
def cli(ctx: Context, output_dir: Optional[str], verbose: bool) -> None:
    """🌙 Arkalia-LUNA Logo Generator - Interface CLI professionnelle"""
    ctx.ensure_object(dict)

    # Configuration du contexte
    ctx.obj["output_dir"] = Path(output_dir) if output_dir else Path("exports")
    ctx.obj["verbose"] = verbose

    # Affichage de la bannière
    print_banner()

    # Initialisation du générateur
    try:
        ctx.obj["generator"] = ArkaliaLunaLogo(ctx.obj["output_dir"])
        if verbose:
            print_info(f"Répertoire de sortie : {ctx.obj['output_dir']}")
    except Exception as e:
        print_error(f"Impossible d'initialiser le générateur : {e}")
        sys.exit(1)


@cli.command()
@click.pass_context
def generators(ctx: Context) -> None:
    """Affiche les générateurs disponibles"""
    try:
        available_generators = LogoGeneratorFactory.get_available_generators()

        # Création du tableau
        table = Table(title="🔧 Générateurs Arkalia-LUNA Disponibles")
        table.add_column("Type", style="cyan", no_wrap=True)
        table.add_column("Nom", style="magenta")
        table.add_column("Description", style="green")

        for generator_type, generator_info in available_generators.items():
            table.add_row(
                generator_type,
                generator_info.get("name", "N/A"),
                generator_info.get("description", "N/A"),
            )

        console.print(table)

    except Exception as e:
        print_error(f"Impossible d'afficher les générateurs : {e}")
        sys.exit(1)


@cli.command()
@click.pass_context
def info(ctx: Context) -> None:
    """Affiche les informations sur toutes les variantes disponibles"""
    try:
        generator = ctx.obj["generator"]
        variants_manager = generator.variants_manager

        # Création du tableau
        table = Table(title="🌙 Variantes Émotionnelles Arkalia-LUNA")
        table.add_column("Variante", style="cyan", no_wrap=True)
        table.add_column("Nom", style="magenta")
        table.add_column("Description", style="green")
        table.add_column("Vitesse", style="yellow")
        table.add_column("Intensité", style="red")

        for variant_name in variants_manager.list_variants():
            variant = variants_manager.get_variant(variant_name)
            table.add_row(
                variant_name,
                variant.name,
                variant.description,
                f"{variant.animation_speed}x",
                f"{variant.glow_intensity:.1f}",
            )

        console.print(table)

    except Exception as e:
        print_error(f"Impossible d'afficher les informations : {e}")
        sys.exit(1)


@cli.command()
@click.option("--variant", "-v", required=True, help="Nom de la variante")
@click.option("--size", "-s", default=200, help="Taille du logo en pixels")
@click.option(
    "--generator",
    "-g",
    default="default",
    help=(
        "Type de générateur (default, advanced, ultimate, ai_moon, "
        "dashboard, ultra_max, realism_max, simple_advanced)"
    ),
)
@click.option("--output", "-o", type=click.Path(), help="Chemin de sortie personnalisé")
@click.pass_context
def generate(
    ctx: Context, variant: str, size: int, generator: str, output: Optional[str]
) -> None:
    """Génère un logo SVG pour une variante spécifique"""
    try:
        # Création du générateur spécialisé via la factory
        specialized_generator = LogoGeneratorFactory.create_generator(
            generator_type=generator,
            output_dir=ctx.obj["output_dir"],
        )

        # Validation de la variante
        if not specialized_generator.validate_variant(variant):
            print_error(f"Variante '{variant}' non reconnue")
            variants_list = ", ".join(specialized_generator.list_all_variants())
            console.print(f"Variantes disponibles : {variants_list}")
            sys.exit(1)

        # Génération du logo avec le générateur spécialisé
        with console.status(
            f"[bold blue]Génération du logo '{variant}' "
            f"avec générateur '{generator}'...",
        ):
            output_path = specialized_generator.generate_svg_logo(variant, size)

        print_success("Logo généré avec succès !")
        console.print(f"📁 Fichier : {output_path}")
        console.print(f"🎨 Variante : {variant}")
        console.print(f"🔧 Générateur : {generator}")
        console.print(f"📏 Taille : {size}x{size} pixels")

        # Déplacement si chemin personnalisé spécifié
        if output:
            custom_path = Path(output)
            custom_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.rename(custom_path)
            console.print(f"📁 Déplacé vers : {custom_path}")

    except Exception as e:
        print_error(f"Impossible de générer le logo : {e}")
        sys.exit(1)


@cli.command()
@click.option("--size", "-s", default=200, help="Taille des logos en pixels")
@click.option(
    "--parallel",
    "-p",
    is_flag=True,
    help="Génération parallèle (si supportée)",
)
@click.pass_context
def generate_all(ctx: Context, size: int, parallel: bool) -> None:
    """Génère toutes les variantes du logo"""
    try:
        generator = ctx.obj["generator"]
        variants = generator.list_all_variants()

        console.print(
            f"[bold blue]🎨 Génération de {len(variants)} variantes "
            f"en taille {size}x{size}...[/bold blue]",
        )

        # Génération avec barre de progression
        generated_files = []
        for variant in track(variants, description="Génération des logos"):
            try:
                output_path = generator.generate_svg_logo(variant, size)
                generated_files.append(output_path)
                console.print(f"[green]✅[/green] {variant} : {output_path.name}")
            except Exception as e:
                console.print(f"[red]❌[/red] {variant} : {e}")

        # Résumé
        console.print("\n[bold green]🎉 Génération terminée ![/bold green]")
        console.print(f"📁 {len(generated_files)}/{len(variants)} logos générés")
        console.print(f"📂 Répertoire : {generator.get_output_directory()}")

        # Affichage des fichiers
        if generated_files:
            console.print("\n📋 Fichiers générés :")
            for file_path in generated_files:
                console.print(f"  • {file_path.name}")

    except Exception as e:
        print_error(f"Impossible de générer tous les logos : {e}")
        sys.exit(1)


@cli.command()
@click.option("--variant", "-v", required=True, help="Nom de la variante")
@click.option("--size", "-s", default=32, help="Taille du favicon en pixels")
@click.option("--output", "-o", type=click.Path(), help="Chemin de sortie personnalisé")
@click.pass_context
def favicon(ctx: Context, variant: str, size: int, output: Optional[str]) -> None:
    """Crée un favicon PNG pour une variante"""
    try:
        generator = ctx.obj["generator"]

        # Validation de la variante
        if not generator.validate_variant(variant):
            print_error(f"Variante '{variant}' non reconnue")
            console.print(
                f"Variantes disponibles : {', '.join(generator.list_all_variants())}",
            )
            sys.exit(1)

        # Création du favicon
        with console.status(f"[bold blue]Création du favicon '{variant}'..."):
            output_path = generator.create_favicon(variant, size)

        print_success("Favicon généré avec succès !")
        console.print(f"📁 Fichier : {output_path}")
        console.print(f"🎨 Variante : {variant}")
        console.print(f"📏 Taille : {size}x{size} pixels")

        # Déplacement si chemin personnalisé spécifié
        if output:
            custom_path = Path(output)
            custom_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.rename(custom_path)
            console.print(f"📁 Déplacé vers : {custom_path}")

    except Exception as e:
        print_error(f"Impossible de créer le favicon : {e}")
        sys.exit(1)


@cli.command()
@click.option("--size", "-s", default=32, help="Taille des favicons en pixels")
@click.pass_context
def favicon_all(ctx: Context, size: int) -> None:
    """Crée des favicons pour toutes les variantes"""
    try:
        generator = ctx.obj["generator"]
        variants = generator.list_all_variants()

        console.print(
            f"[bold blue]🎨 Création de {len(variants)} favicons "
            f"en taille {size}x{size}...[/bold blue]",
        )

        # Création avec barre de progression
        generated_files = []
        for variant in track(variants, description="Création des favicons"):
            try:
                output_path = generator.create_favicon(variant, size)
                generated_files.append(output_path)
                console.print(f"[green]✅[/green] {variant} : {output_path.name}")
            except Exception as e:
                console.print(f"[red]❌[/red] {variant} : {e}")

        # Résumé
        console.print("\n[bold green]🎉 Création des favicons terminée ![/bold green]")
        console.print(f"📁 {len(generated_files)}/{len(variants)} favicons créés")

    except Exception as e:
        print_error(f"Impossible de créer tous les favicons : {e}")
        sys.exit(1)


@cli.command()
@click.pass_context
def stats(ctx: Context) -> None:
    """Affiche les statistiques de génération"""
    try:
        generator = ctx.obj["generator"]
        stats = generator.get_generation_stats()

        # Création du tableau des stats
        table = Table(title="📊 Statistiques de Génération")
        table.add_column("Métrique", style="cyan")
        table.add_column("Valeur", style="green")

        table.add_row("Total fichiers", str(stats["total_files"]))
        table.add_row("Logos SVG", str(stats["svg_logos"]))
        table.add_row("Favicons PNG", str(stats["png_favicons"]))
        table.add_row("Répertoire sortie", stats["output_directory"])
        table.add_row("Variantes disponibles", str(stats["available_variants"]))

        console.print(table)

    except Exception as e:
        print_error(f"Impossible de récupérer les statistiques : {e}")
        sys.exit(1)


@cli.command()
@click.option(
    "--logo",
    type=click.Path(exists=True, path_type=Path),
    help="Chemin vers le logo SVG/PNG Arkalia CIA",
)
@click.option(
    "--screenshots-dir",
    type=click.Path(exists=True, path_type=Path),
    default=Path("docs/screenshots/android"),
    help="Répertoire contenant les screenshots source",
)
@click.option(
    "--output-dir",
    type=click.Path(path_type=Path),
    default=Path("playstore-assets"),
    help="Répertoire de sortie pour les assets",
)
@click.option(
    "--feature-only",
    is_flag=True,
    help="Générer uniquement la feature graphic",
)
@click.option(
    "--screenshots-only",
    is_flag=True,
    help="Optimiser uniquement les screenshots",
)
@click.option(
    "--bg-color",
    default="#FFFFFF",
    help="Couleur de fond pour la feature graphic (hex)",
)
def playstore(
    logo: Optional[Path],
    screenshots_dir: Path,
    output_dir: Path,
    feature_only: bool,
    screenshots_only: bool,
    bg_color: str,
) -> None:
    """Génère les assets nécessaires pour Google Play Store"""
    try:
        from .playstore_assets_generator import PlayStoreAssetsGenerator

        console.print("[bold blue]📱 Génération des assets Play Store...[/bold blue]")

        generator = PlayStoreAssetsGenerator(
            output_dir=output_dir,
            logo_path=logo,
            screenshots_dir=screenshots_dir,
        )

        # Générer selon les options
        generate_feature = not screenshots_only
        generate_screenshots = not feature_only

        assets = generator.generate_all_assets(
            feature_graphic=generate_feature,
            screenshots=generate_screenshots,
            background_color=bg_color,
        )

        # Afficher le résumé
        table = Table(
            title="Assets générés", show_header=True, header_style="bold blue"
        )
        table.add_column("Type", style="cyan")
        table.add_column("Fichier", style="green")

        if assets["feature_graphic"]:
            table.add_row("Feature Graphic", assets["feature_graphic"])

        for screenshot in assets["screenshots"]:
            table.add_row("Screenshot", screenshot)

        console.print(table)

        if assets["feature_graphic"] or assets["screenshots"]:
            print_success(f"Assets générés dans : {assets['output_dir']}")
        else:
            print_error("Aucun asset généré. Vérifiez les chemins et options.")

    except ImportError as e:
        print_error(f"Module requis manquant : {e}")
        console.print(
            "[yellow]Installez les dépendances avec : pip install pillow cairosvg[/yellow]"
        )
        sys.exit(1)
    except Exception as e:
        print_error(f"Impossible de générer les assets : {e}")
        sys.exit(1)


@cli.command()
@click.option("--confirm", is_flag=True, help="Confirmation automatique")
@click.pass_context
def clean(ctx: Context, confirm: bool) -> None:
    """Nettoie tous les fichiers générés"""
    try:
        generator = ctx.obj["generator"]

        if not confirm:
            console.print(
                "[bold yellow]⚠️  Attention :[/bold yellow] "
                "Cette action supprimera tous les fichiers générés.",
            )
            if not click.confirm("Continuer ?"):
                console.print("Opération annulée.")
                return

        with console.status("[bold blue]Nettoyage en cours..."):
            count = generator.cleanup_generated_files()

        print_success(f"Nettoyage terminé ! {count} fichiers supprimés.")

    except Exception as e:
        print_error(f"Impossible de nettoyer : {e}")
        sys.exit(1)


@cli.command()
@click.pass_context
def version(ctx: Context) -> None:
    """Affiche la version du générateur"""
    from . import __version__

    console.print(
        f"[bold blue]🌙 Arkalia-LUNA Logo Generator v{__version__}[/bold blue]",
    )


def main() -> None:
    """Point d'entrée principal"""
    try:
        cli()
    except KeyboardInterrupt:
        console.print("\n[yellow]Opération interrompue par l'utilisateur.[/yellow]")
        sys.exit(0)
    except Exception as e:
        print_error(f"Erreur fatale : {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
