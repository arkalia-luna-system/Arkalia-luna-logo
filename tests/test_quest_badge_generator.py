"""
Tests pour le module QuestBadgeGenerator
"""

from pathlib import Path

from src.quest_badge_generator import QuestBadgeGenerator


class TestQuestBadgeGenerator:
    """Tests pour QuestBadgeGenerator"""

    def test_badge_generator_init(self) -> None:
        """Test initialisation du générateur de badges"""
        generator = QuestBadgeGenerator(output_dir=Path("test_badges"))
        assert generator.output_dir.exists()
        assert generator.variants_manager is not None

    def test_generate_badge_mission(self) -> None:
        """Test génération badge mission"""
        generator = QuestBadgeGenerator(output_dir=Path("test_badges"))
        badge_path = generator.generate_badge(
            badge_type="mission",
            size=128,
            variant="serenity",
            text="Test Mission",
        )
        assert badge_path.exists()
        assert badge_path.suffix == ".svg"

    def test_generate_badge_achievement(self) -> None:
        """Test génération badge achievement"""
        generator = QuestBadgeGenerator(output_dir=Path("test_badges"))
        badge_path = generator.generate_badge(
            badge_type="achievement",
            size=128,
            variant="power",
            text="Test Achievement",
            stars=3,
        )
        assert badge_path.exists()

    def test_generate_badge_level(self) -> None:
        """Test génération badge niveau"""
        generator = QuestBadgeGenerator(output_dir=Path("test_badges"))
        badge_path = generator.generate_badge(
            badge_type="level",
            size=64,
            variant="mystery",
            level=5,
        )
        assert badge_path.exists()

    def test_generate_badge_emotion(self) -> None:
        """Test génération badge émotion"""
        generator = QuestBadgeGenerator(output_dir=Path("test_badges"))
        badge_path = generator.generate_badge(
            badge_type="emotion",
            size=128,
            variant="awakening",
        )
        assert badge_path.exists()

    def test_generate_badge_invalid_type(self) -> None:
        """Test génération badge avec type invalide"""
        generator = QuestBadgeGenerator(output_dir=Path("test_badges"))
        try:
            generator.generate_badge(
                badge_type="invalid",
                size=128,
                variant="serenity",
            )
            assert False, "Devrait lever ValueError"
        except ValueError:
            pass

    def test_generate_badge_invalid_size(self) -> None:
        """Test génération badge avec taille invalide"""
        generator = QuestBadgeGenerator(output_dir=Path("test_badges"))
        try:
            generator.generate_badge(
                badge_type="mission",
                size=512,  # Taille invalide pour mission
                variant="serenity",
            )
            assert False, "Devrait lever ValueError"
        except ValueError:
            pass

    def test_generate_all_badges(self) -> None:
        """Test génération de tous les badges"""
        generator = QuestBadgeGenerator(output_dir=Path("test_badges"))
        badges = generator.generate_all_badges(variant="serenity")
        assert len(badges) > 0

    def test_generate_all_badges_specific_type(self) -> None:
        """Test génération de tous les badges d'un type"""
        generator = QuestBadgeGenerator(output_dir=Path("test_badges"))
        badges = generator.generate_all_badges(variant="serenity", badge_type="mission")
        assert len(badges) == 2  # 2 tailles pour mission
