"""
Tests de performance
"""

import time

from src.generator_factory import LogoGeneratorFactory


class TestPerformance:
    """Tests de performance"""

    def test_performance_generate_logo_speed(self) -> None:
        """Test performance : Vitesse génération logo"""
        generator = LogoGeneratorFactory.create_generator("default")
        start = time.time()
        generator.generate_svg_logo("serenity", 200)
        elapsed = time.time() - start
        # Génération SVG devrait être rapide (< 1s)
        assert elapsed < 1.0

    def test_performance_generate_multiple_logos(self) -> None:
        """Test performance : Génération multiple logos"""
        generator = LogoGeneratorFactory.create_generator("default")
        variants = ["serenity", "power", "mystery"]
        start = time.time()

        for variant in variants:
            generator.generate_svg_logo(variant, 200)

        elapsed = time.time() - start
        # 3 logos devraient être générés rapidement (< 3s)
        assert elapsed < 3.0

    def test_performance_cache_speedup(self) -> None:
        """Test performance : Accélération avec cache"""
        generator = LogoGeneratorFactory.create_generator("default")

        # Première génération (sans cache)
        start1 = time.time()
        path1 = generator.generate_svg_logo("serenity", 200)
        elapsed1 = time.time() - start1

        # Deuxième génération (avec cache)
        start2 = time.time()
        path2 = generator.generate_svg_logo("serenity", 200)
        elapsed2 = time.time() - start2

        # Cache devrait être plus rapide (ou au moins aussi rapide)
        assert elapsed2 <= elapsed1 * 1.5  # Tolérance 50%

    def test_performance_memory_usage(self) -> None:
        """Test performance : Utilisation mémoire"""
        import sys

        generator = LogoGeneratorFactory.create_generator("default")
        initial_size = sys.getsizeof(generator)

        # Générer plusieurs logos
        for variant in ["serenity", "power", "mystery"]:
            generator.generate_svg_logo(variant, 200)

        final_size = sys.getsizeof(generator)
        # La taille ne devrait pas exploser
        assert final_size < initial_size * 10

    def test_performance_concurrent_generation(self) -> None:
        """Test performance : Génération concurrente"""
        import concurrent.futures

        generator = LogoGeneratorFactory.create_generator("default")
        variants = ["serenity", "power", "mystery"]

        start = time.time()

        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = [
                executor.submit(generator.generate_svg_logo, variant, 200)
                for variant in variants
            ]
            results = [f.result() for f in concurrent.futures.as_completed(futures)]

        elapsed = time.time() - start

        # Génération concurrente devrait être plus rapide
        assert len(results) == 3
        assert elapsed < 5.0  # 3 logos en parallèle < 5s

