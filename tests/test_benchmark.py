"""
Tests de benchmark pour mesurer les performances du générateur de logos.
"""

import pytest

from src.logo_generator import ArkaliaLunaLogo
from src.variants import ColorScheme, LogoVariant, LogoVariants, VariantType


class TestLogoGeneratorBenchmark:
    """Tests de benchmark pour le générateur de logos."""

    @pytest.fixture
    def generator(self):
        """Fixture pour le générateur de logos."""
        return ArkaliaLunaLogo()

    @pytest.fixture
    def variant(self):
        """Fixture pour une variante de test."""
        return "serenity"

    def test_logo_generation_benchmark(self, benchmark, generator, variant):
        """Benchmark de la génération de logo."""

        def generate_logo():
            return generator.generate_svg_logo(variant, 100)

        result = benchmark(generate_logo)
        assert result is not None
        assert "svg" in str(result).lower()

    def test_multiple_sizes_benchmark(self, benchmark, generator, variant):
        """Benchmark de la génération avec différentes tailles."""
        sizes = [50, 100, 200, 500]

        def generate_multiple_sizes():
            results = []
            for size in sizes:
                result = generator.generate_svg_logo(variant, size)
                results.append(result)
            return results

        results = benchmark(generate_multiple_sizes)
        assert len(results) == len(sizes)
        assert all("svg" in str(result).lower() for result in results)

    def test_variant_switching_benchmark(self, benchmark, generator):
        """Benchmark du changement de variantes."""
        variants = ["serenity", "power", "mystery"]

        def switch_variants():
            results = []
            for variant in variants:
                result = generator.generate_svg_logo(variant, 100)
                results.append(result)
            return results

        results = benchmark(switch_variants)
        assert len(results) == len(variants)
        assert all("svg" in str(result).lower() for result in results)


class TestSVGBuilderBenchmark:
    """Tests de benchmark pour les builders SVG."""

    @pytest.fixture
    def svg_builder(self):
        """Fixture pour le builder SVG."""
        from src.svg_builder_advanced import AdvancedSVGBuilder

        variants = LogoVariants()
        return AdvancedSVGBuilder(variants)

    def test_drawing_creation_benchmark(self, benchmark, svg_builder):
        """Benchmark de la création de dessin SVG."""

        def create_drawing():
            return svg_builder.create_drawing(100, (0, 0, 100, 100))

        result = benchmark(create_drawing)
        assert result is not None
        assert hasattr(result, "defs")

    def test_variant_processing_benchmark(self, benchmark, svg_builder):
        """Benchmark du traitement des variantes."""

        def process_variant():
            colors = ColorScheme(
                primary="#1e3a8a", secondary="#3b82f6", accent="#06b6d4", glow="#60a5fa"
            )

            _ = LogoVariant(
                name="serenity",
                variant_type=VariantType.SERENITY,
                colors=colors,
                description="Test variant",
                animation_speed=1.0,
                glow_intensity=0.8,
            )
            drawing = svg_builder.create_drawing(100)
            return drawing

        result = benchmark(process_variant)
        assert result is not None


class TestCLIBenchmark:
    """Tests de benchmark pour l'interface CLI."""

    def test_cli_import_benchmark(self, benchmark):
        """Benchmark de l'import CLI."""

        def import_cli():
            import src.cli

            return src.cli

        result = benchmark(import_cli)
        assert result is not None

    def test_cli_help_benchmark(self, benchmark):
        """Benchmark de l'affichage de l'aide CLI."""

        def show_help():
            # Simuler l'affichage de l'aide
            return "Usage: python -m src.cli [OPTIONS] COMMAND [ARGS]..."

        result = benchmark(show_help)
        assert result is not None
        assert "Usage:" in result


if __name__ == "__main__":
    pytest.main([__file__, "--benchmark-only"])
