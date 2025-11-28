"""
Tests pour le générateur Quest
"""

import pytest

from src.generator_factory import LogoGeneratorFactory
from src.quest_branding_generator import QuestBrandingGenerator
from src.quest_palette import QUEST_PALETTE, get_quest_palette


class TestQuestPalette:
    """Tests pour la palette Quest"""

    def test_palette_instance(self):
        """Test que la palette Quest est une instance valide"""
        assert QUEST_PALETTE is not None
        assert QUEST_PALETTE.PRIMARY == "#667eea"
        assert QUEST_PALETTE.SECONDARY == "#764ba2"

    def test_palette_to_dict(self):
        """Test conversion palette en dictionnaire"""
        palette_dict = QUEST_PALETTE.to_dict()
        assert "primary" in palette_dict
        assert "secondary" in palette_dict
        assert palette_dict["primary"] == "#667eea"

    def test_get_quest_palette(self):
        """Test fonction get_quest_palette"""
        palette = get_quest_palette()
        assert palette == QUEST_PALETTE

    def test_get_rgb(self):
        """Test conversion hex en RGB"""
        rgb = QUEST_PALETTE.get_rgb("#667eea")
        assert rgb == (102, 126, 234)

    def test_get_primary_rgb(self):
        """Test récupération RGB primaire"""
        rgb = QUEST_PALETTE.get_primary_rgb()
        assert len(rgb) == 3
        assert all(isinstance(c, int) for c in rgb)


class TestQuestBrandingGenerator:
    """Tests pour le générateur Quest"""

    @pytest.fixture
    def quest_generator(self, tmp_path):
        """Fixture pour créer un générateur Quest"""
        output_dir = tmp_path / "exports" / "quest"
        output_dir.parent.mkdir(parents=True, exist_ok=True)
        return QuestBrandingGenerator(output_dir)

    def test_generator_initialization(self, quest_generator):
        """Test initialisation du générateur"""
        assert quest_generator is not None
        assert quest_generator.palette == QUEST_PALETTE
        assert quest_generator.variants_manager is not None

    def test_generate_svg_logo_mark_only(self, quest_generator):
        """Test génération logo mark_only"""
        output_path = quest_generator.generate_svg_logo(
            "mark_only", size=200, emotion_variant="serenity", style="ultimate"
        )
        assert output_path.exists()
        assert output_path.suffix == ".svg"
        assert "quest-mark_only" in output_path.name

    def test_generate_svg_logo_vertical(self, quest_generator):
        """Test génération logo vertical"""
        output_path = quest_generator.generate_svg_logo(
            "vertical", size=200, emotion_variant="serenity", style="ultimate"
        )
        assert output_path.exists()
        assert output_path.suffix == ".svg"
        assert "quest-vertical" in output_path.name

    def test_generate_svg_logo_horizontal(self, quest_generator):
        """Test génération logo horizontal"""
        output_path = quest_generator.generate_svg_logo(
            "horizontal", size=200, emotion_variant="serenity", style="ultimate"
        )
        assert output_path.exists()
        assert output_path.suffix == ".svg"
        assert "quest-horizontal" in output_path.name

    def test_generate_all_declinations(self, quest_generator):
        """Test génération toutes les déclinaisons"""
        generated_files = quest_generator.generate_all_declinations(
            sizes=[200], formats=["svg"], emotion_variant="serenity", style="ultimate"
        )
        assert len(generated_files) == 3  # mark_only, vertical, horizontal
        for file_path in generated_files:
            assert file_path.exists()

    def test_generate_all_emotion_variants(self, quest_generator):
        """Test génération toutes les variantes émotionnelles"""
        generated_files = quest_generator.generate_all_emotion_variants(
            "mark_only", size=200, formats=["svg"], style="ultimate"
        )
        assert len(generated_files) > 0
        for file_path in generated_files:
            assert file_path.exists()

    def test_get_quest_stats(self, quest_generator):
        """Test récupération statistiques Quest"""
        stats = quest_generator.get_quest_stats()
        assert "status" in stats
        assert stats["status"] == "ready"
        assert "available_variants" in stats
        assert "recommended_styles" in stats
        assert "palette" in stats


class TestQuestFactoryIntegration:
    """Tests d'intégration avec la Factory"""

    def test_factory_create_quest_generator(self, tmp_path):
        """Test création générateur Quest via Factory"""
        output_dir = tmp_path / "exports" / "quest"
        output_dir.parent.mkdir(parents=True, exist_ok=True)
        generator = LogoGeneratorFactory.create_generator(
            "quest", output_dir=output_dir
        )
        assert isinstance(generator, QuestBrandingGenerator)

    def test_factory_get_available_generators(self):
        """Test que Quest est dans les générateurs disponibles"""
        generators = LogoGeneratorFactory.get_available_generators()
        assert "quest" in generators
        assert "name" in generators["quest"]
        assert "description" in generators["quest"]
