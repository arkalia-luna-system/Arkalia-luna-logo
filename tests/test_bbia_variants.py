"""Tests pour les variantes émotionnelles BBIA"""

import pytest

from src.bbia_variants import (
    BBIA_VARIANTS,
    BBIAVariant,
    BBIAVariantType,
    get_all_bbia_variants,
    get_bbia_variant,
)


class TestBBIAVariants:
    """Tests pour BBIAVariants"""

    def test_get_variant_valid(self):
        """Test récupération variante valide"""
        variant = BBIA_VARIANTS.get_variant("serenity")

        assert isinstance(variant, BBIAVariant)
        assert variant.variant_type == BBIAVariantType.SERENITY
        assert "Sérénité" in variant.name

    def test_get_variant_invalid(self):
        """Test récupération variante invalide"""
        with pytest.raises(ValueError, match="non trouvée"):
            BBIA_VARIANTS.get_variant("invalid_variant")

    def test_list_variant_names(self):
        """Test liste des noms de variantes"""
        names = BBIA_VARIANTS.list_variant_names()

        assert isinstance(names, list)
        assert len(names) == 10
        assert "serenity" in names
        assert "power" in names
        assert "mystery" in names

    def test_get_all_variants(self):
        """Test récupération toutes les variantes"""
        variants = BBIA_VARIANTS.get_all_variants()

        assert isinstance(variants, dict)
        assert len(variants) == 10
        assert "serenity" in variants
        assert "power" in variants

    def test_variant_serenity(self):
        """Test variante Sérénité"""
        variant = BBIA_VARIANTS.get_variant("serenity")

        assert variant.name == "🤖 BBIA Sérénité"
        assert variant.halo_enabled is True
        assert variant.particles_enabled is True
        assert variant.animation_speed == 1.0
        assert variant.glow_intensity == 0.7

    def test_variant_power(self):
        """Test variante Puissance"""
        variant = BBIA_VARIANTS.get_variant("power")

        assert variant.name == "⚡ BBIA Puissance"
        assert variant.animation_speed == 1.5
        assert variant.glow_intensity == 0.9

    def test_variant_to_dict(self):
        """Test conversion variante en dictionnaire"""
        variant = BBIA_VARIANTS.get_variant("serenity")
        variant_dict = variant.to_dict()

        assert isinstance(variant_dict, dict)
        assert "variant_type" in variant_dict
        assert "name" in variant_dict
        assert "colors" in variant_dict
        assert "halo_enabled" in variant_dict
        assert "particles_enabled" in variant_dict

    def test_get_bbia_variant_function(self):
        """Test fonction get_bbia_variant"""
        variant = get_bbia_variant("serenity")

        assert isinstance(variant, BBIAVariant)
        assert variant.variant_type == BBIAVariantType.SERENITY

    def test_get_all_bbia_variants_function(self):
        """Test fonction get_all_bbia_variants"""
        variants = get_all_bbia_variants()

        assert isinstance(variants, dict)
        assert len(variants) == 10
