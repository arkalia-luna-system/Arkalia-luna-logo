"""
🧪 Tests pour le module variants
"""

import sys
from pathlib import Path

import pytest

# Ajout du chemin src pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from variants import ColorScheme, LogoVariant, LogoVariants, VariantType


class TestColorScheme:
    """Tests pour la classe ColorScheme"""

    def test_color_scheme_creation(self):
        """Test de création d'un schéma de couleurs"""
        colors = ColorScheme(
            primary="#1e3a8a", secondary="#3b82f6", accent="#06b6d4", glow="#60a5fa"
        )

        assert colors.primary == "#1e3a8a"
        assert colors.secondary == "#3b82f6"
        assert colors.accent == "#06b6d4"
        assert colors.glow == "#60a5fa"

    def test_color_scheme_to_dict(self):
        """Test de conversion en dictionnaire"""
        colors = ColorScheme(
            primary="#1e3a8a", secondary="#3b82f6", accent="#06b6d4", glow="#60a5fa"
        )

        color_dict = colors.to_dict()
        assert isinstance(color_dict, dict)
        assert color_dict["primary"] == "#1e3a8a"
        assert color_dict["secondary"] == "#3b82f6"
        assert color_dict["accent"] == "#06b6d4"
        assert color_dict["glow"] == "#60a5fa"


class TestLogoVariant:
    """Tests pour la classe LogoVariant"""

    def test_logo_variant_creation(self):
        """Test de création d'une variante de logo"""
        colors = ColorScheme(
            primary="#1e3a8a", secondary="#3b82f6", accent="#06b6d4", glow="#60a5fa"
        )

        variant = LogoVariant(
            variant_type=VariantType.SERENITY,
            name="🌙 Sérénité",
            description="Halo doux, pulsations lentes",
            colors=colors,
            animation_speed=1.0,
            glow_intensity=0.7,
        )

        assert variant.variant_type == VariantType.SERENITY
        assert variant.name == "🌙 Sérénité"
        assert variant.animation_speed == 1.0
        assert variant.glow_intensity == 0.7

    def test_logo_variant_to_dict(self):
        """Test de conversion en dictionnaire"""
        colors = ColorScheme(
            primary="#1e3a8a", secondary="#3b82f6", accent="#06b6d4", glow="#60a5fa"
        )

        variant = LogoVariant(
            variant_type=VariantType.SERENITY,
            name="🌙 Sérénité",
            description="Halo doux, pulsations lentes",
            colors=colors,
            animation_speed=1.0,
            glow_intensity=0.7,
        )

        variant_dict = variant.to_dict()
        assert isinstance(variant_dict, dict)
        assert variant_dict["variant_type"] == "serenity"
        assert variant_dict["name"] == "🌙 Sérénité"
        assert variant_dict["animation_speed"] == 1.0


class TestLogoVariants:
    """Tests pour la classe LogoVariants"""

    def test_variants_manager_creation(self):
        """Test de création du gestionnaire de variantes"""
        variants_manager = LogoVariants()
        assert variants_manager is not None

    def test_get_all_variants(self):
        """Test de récupération de toutes les variantes"""
        variants_manager = LogoVariants()
        all_variants = variants_manager.get_all_variants()

        assert isinstance(all_variants, dict)
        assert len(all_variants) == 10  # 10 variantes définies

        expected_variants = [
            "serenity",
            "power",
            "mystery",
            "awakening",
            "creative",
            "rainy",
            "stormy",
            "explosive",
            "sunny",
            "snowy",
        ]
        for variant_name in expected_variants:
            assert variant_name in all_variants

    def test_get_variant_valid(self):
        """Test de récupération d'une variante valide"""
        variants_manager = LogoVariants()
        serenity_variant = variants_manager.get_variant("serenity")

        assert serenity_variant is not None
        assert serenity_variant.variant_type == VariantType.SERENITY
        assert serenity_variant.name == "🌙 Sérénité"

    def test_get_variant_invalid(self):
        """Test de récupération d'une variante invalide"""
        variants_manager = LogoVariants()

        with pytest.raises(ValueError) as exc_info:
            variants_manager.get_variant("invalid_variant")

        assert "Variante 'invalid_variant' non reconnue" in str(exc_info.value)

    def test_list_variants(self):
        """Test de liste des variantes disponibles"""
        variants_manager = LogoVariants()
        variant_list = variants_manager.list_variants()

        assert isinstance(variant_list, list)
        assert len(variant_list) == 10

        expected_variants = [
            "serenity",
            "power",
            "mystery",
            "awakening",
            "creative",
            "rainy",
            "stormy",
            "explosive",
            "sunny",
            "snowy",
        ]
        for variant_name in expected_variants:
            assert variant_name in variant_list

    def test_validate_variant_valid(self):
        """Test de validation d'une variante valide"""
        variants_manager = LogoVariants()
        assert variants_manager.validate_variant("serenity") is True

    def test_validate_variant_invalid(self):
        """Test de validation d'une variante invalide"""
        variants_manager = LogoVariants()
        assert variants_manager.validate_variant("invalid_variant") is False

    def test_get_variant_info(self):
        """Test de récupération des informations d'une variante"""
        variants_manager = LogoVariants()
        variant_info = variants_manager.get_variant_info("serenity")

        assert isinstance(variant_info, dict)
        assert variant_info["variant_type"] == "serenity"
        assert variant_info["name"] == "🌙 Sérénité"
        assert "colors" in variant_info
        assert "animation_speed" in variant_info
        assert "glow_intensity" in variant_info


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
