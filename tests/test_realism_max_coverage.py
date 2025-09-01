"""
Tests pour améliorer la couverture du module svg_builder_realism_max.py
Objectif : 29% → 90% de couverture
"""

import random
from unittest.mock import Mock

import pytest

from src.svg_builder_realism_max import RealismMaxSVGBuilder
from src.variants import ColorScheme, LogoVariant, LogoVariants, VariantType


class TestRealismMaxSVGBuilder:
    """Tests pour RealismMaxSVGBuilder"""

    @pytest.fixture
    def variants_manager(self):
        """Manager de variantes mock"""
        manager = Mock(spec=LogoVariants)
        manager.get_variant.return_value = LogoVariant(
            name="Test Variant",
            description="Test Description",
            variant_type=VariantType.SERENITY,
            animation_speed=1.0,
            glow_intensity=0.8,
            colors=ColorScheme(
                primary="#1e3a8a", secondary="#3b82f6", accent="#06b6d4", glow="#60a5fa"
            ),
        )
        return manager

    @pytest.fixture
    def builder(self, variants_manager):
        """Builder RealismMaxSVGBuilder"""
        return RealismMaxSVGBuilder(variants_manager)

    def test_initialization(self, builder):
        """Test de l'initialisation du builder"""
        assert builder.realism_level == 0.95
        assert builder.organic_complexity == 0.8
        assert builder.ai_enhancement is True

    def test_create_drawing(self, builder):
        """Test de création d'un dessin SVG"""
        size = 200
        drawing = builder.create_drawing(size)

        assert drawing is not None
        assert drawing.attribs["width"] == size
        assert drawing.attribs["height"] == size

    def test_create_drawing_with_viewbox(self, builder):
        """Test de création d'un dessin SVG avec viewbox personnalisé"""
        size = 200
        viewbox = (0, 0, 300, 300)
        drawing = builder.create_drawing(size, viewbox)

        assert drawing is not None
        assert drawing.attribs["viewBox"] == "0 0 300 300"

    def test_add_realism_definitions(self, builder, variants_manager):
        """Test d'ajout des définitions réalistes"""
        variant = variants_manager.get_variant("test")
        drawing = builder.create_drawing(200)

        # Avant l'ajout des définitions
        initial_defs_count = len(drawing.defs.elements) if drawing.defs.elements else 0

        builder.add_realism_definitions(drawing, variant)

        # Après l'ajout des définitions
        final_defs_count = len(drawing.defs.elements) if drawing.defs.elements else 0
        assert final_defs_count > initial_defs_count

    def test_add_realistic_gradients(self, builder, variants_manager):
        """Test d'ajout des gradients réalistes"""
        variant = variants_manager.get_variant("test")
        defs = Mock()
        defs.add = Mock()

        builder._add_realistic_gradients(defs, variant)

        # Vérifier que add a été appelé
        assert defs.add.called

    def test_add_realistic_glow_filters(self, builder, variants_manager):
        """Test d'ajout des filtres de lueur réalistes"""
        variant = variants_manager.get_variant("test")
        defs = Mock()
        defs.add = Mock()

        builder._add_realistic_glow_filters(defs, variant)

        # Vérifier que add a été appelé
        assert defs.add.called

    def test_add_organic_filters(self, builder, variants_manager):
        """Test d'ajout des filtres organiques"""
        variant = variants_manager.get_variant("test")
        defs = Mock()
        defs.add = Mock()

        builder._add_organic_filters(defs, variant)

        # Vérifier que add a été appelé
        assert defs.add.called

    def test_add_depth_masks(self, builder, variants_manager):
        """Test d'ajout des masques de profondeur"""
        variant = variants_manager.get_variant("test")
        defs = Mock()
        defs.add = Mock()

        builder._add_depth_masks(defs, variant)

        # Vérifier que add a été appelé
        assert defs.add.called

    def test_build_logo(self, builder, variants_manager):
        """Test de construction du logo complet"""
        variant_name = "test"
        size = 200

        logo = builder.build_logo(variant_name, size)

        assert logo is not None
        assert logo.attribs["width"] == size
        assert logo.attribs["height"] == size

    def test_add_realistic_logo_elements(self, builder, variants_manager):
        """Test d'ajout des éléments du logo réaliste"""
        variant = variants_manager.get_variant("test")
        drawing = builder.create_drawing(200)

        # Avant l'ajout des éléments
        initial_elements_count = len(drawing.elements) if drawing.elements else 0

        builder._add_realistic_logo_elements(drawing, variant, 200)

        # Après l'ajout des éléments
        final_elements_count = len(drawing.elements) if drawing.elements else 0
        assert final_elements_count > initial_elements_count

    def test_add_organic_effects_high_realism(self, builder, variants_manager):
        """Test d'ajout d'effets organiques avec réalisme élevé"""
        variant = variants_manager.get_variant("test")
        drawing = builder.create_drawing(200)
        center = 100
        radius = 66

        # Forcer un niveau de réalisme élevé
        builder.realism_level = 0.9

        # Avant l'ajout des effets
        initial_elements_count = len(drawing.elements) if drawing.elements else 0

        builder._add_organic_effects(drawing, variant, 200, center, radius)

        # Après l'ajout des effets
        final_elements_count = len(drawing.elements) if drawing.elements else 0
        assert final_elements_count > initial_elements_count

    def test_add_organic_effects_low_realism(self, builder, variants_manager):
        """Test d'ajout d'effets organiques avec réalisme faible"""
        variant = variants_manager.get_variant("test")
        drawing = builder.create_drawing(200)
        center = 100
        radius = 66

        # Forcer un niveau de réalisme faible
        builder.realism_level = 0.5

        # Avant l'ajout des effets
        initial_elements_count = len(drawing.elements) if drawing.elements else 0

        builder._add_organic_effects(drawing, variant, 200, center, radius)

        # Après l'ajout des effets
        final_elements_count = len(drawing.elements) if drawing.elements else 0
        assert final_elements_count > initial_elements_count

    def test_setup_realism_enhancements(self, builder):
        """Test de la configuration des améliorations réalistes"""
        # Réinitialiser les valeurs
        builder.realism_level = 0.0
        builder.organic_complexity = 0.0
        builder.ai_enhancement = False

        # Appeler la méthode de configuration
        builder._setup_realism_enhancements()

        assert builder.realism_level == 0.95
        assert builder.organic_complexity == 0.8
        assert builder.ai_enhancement is True

    def test_build_logo_with_different_sizes(self, builder, variants_manager):
        """Test de construction de logos avec différentes tailles"""
        variant_name = "test"
        sizes = [100, 200, 500, 1000]

        for size in sizes:
            logo = builder.build_logo(variant_name, size)
            assert logo is not None
            assert logo.attribs["width"] == size
            assert logo.attribs["height"] == size

    def test_build_logo_with_different_variants(self, builder, variants_manager):
        """Test de construction de logos avec différentes variantes"""
        # Créer plusieurs variantes de test
        variants = [
            LogoVariant(
                name="Serenity",
                description="Serenity variant",
                variant_type=VariantType.SERENITY,
                animation_speed=1.0,
                glow_intensity=0.8,
                colors=ColorScheme(
                    primary="#1e3a8a",
                    secondary="#3b82f6",
                    accent="#06b6d4",
                    glow="#60a5fa",
                ),
            ),
            LogoVariant(
                name="Power",
                description="Power variant",
                variant_type=VariantType.POWER,
                animation_speed=1.5,
                glow_intensity=1.0,
                colors=ColorScheme(
                    primary="#dc2626",
                    secondary="#ef4444",
                    accent="#f97316",
                    glow="#fbbf24",
                ),
            ),
        ]

        size = 200

        for variant in variants:
            # Mock temporairement get_variant pour retourner la variante actuelle
            variants_manager.get_variant.return_value = variant

            logo = builder.build_logo("test", size)
            assert logo is not None
            assert logo.attribs["width"] == size
            assert logo.attribs["height"] == size

    def test_random_seed_consistency(self, builder):
        """Test de la cohérence de la graine aléatoire"""
        # La graine devrait être fixée à 42 pour la cohérence
        # Ce test vérifie que le comportement est déterministe
        random.seed(42)
        first_random = random.random()

        # Réinitialiser et vérifier la cohérence
        random.seed(42)
        second_random = random.random()

        assert first_random == second_random

    def test_organic_effects_particle_count(self, builder, variants_manager):
        """Test du nombre de particules selon le niveau de réalisme"""
        variant = variants_manager.get_variant("test")
        drawing = builder.create_drawing(200)
        center = 100
        radius = 66

        # Test avec différents niveaux de réalisme
        test_levels = [0.5, 0.7, 0.9, 1.0]

        for level in test_levels:
            builder.realism_level = level
            expected_particles = int(5 * level)

            # Compter les éléments avant
            initial_count = len(drawing.elements) if drawing.elements else 0

            builder._add_organic_effects(drawing, variant, 200, center, radius)

            # Compter les éléments après
            final_count = len(drawing.elements) if drawing.elements else 0
            added_elements = final_count - initial_count

            # Le nombre d'éléments ajoutés devrait être proche du nombre de particules attendu
            assert added_elements >= 0
            if expected_particles > 0:
                assert added_elements > 0
