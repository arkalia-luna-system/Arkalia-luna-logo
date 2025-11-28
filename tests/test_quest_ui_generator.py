"""
Tests pour le module QuestUIGenerator
"""

from pathlib import Path

from src.quest_ui_generator import QuestUIGenerator


class TestQuestUIGenerator:
    """Tests pour QuestUIGenerator"""

    def test_ui_generator_init(self) -> None:
        """Test initialisation du générateur UI"""
        generator = QuestUIGenerator(output_dir=Path("test_ui"))
        assert generator.output_dir.exists()
        assert generator.variants_manager is not None

    def test_generate_ui_button(self) -> None:
        """Test génération bouton"""
        generator = QuestUIGenerator(output_dir=Path("test_ui"))
        element_path = generator.generate_ui_element(
            element_type="button",
            variant="serenity",
            text="Test Button",
        )
        assert element_path.exists()
        assert element_path.suffix == ".svg"

    def test_generate_ui_card(self) -> None:
        """Test génération carte"""
        generator = QuestUIGenerator(output_dir=Path("test_ui"))
        element_path = generator.generate_ui_element(
            element_type="card",
            variant="power",
            text="Test Card",
        )
        assert element_path.exists()

    def test_generate_ui_icon(self) -> None:
        """Test génération icône"""
        generator = QuestUIGenerator(output_dir=Path("test_ui"))
        element_path = generator.generate_ui_element(
            element_type="icon",
            variant="mystery",
            icon_size=64,
            level=5,
        )
        assert element_path.exists()

    def test_generate_ui_indicator(self) -> None:
        """Test génération indicateur"""
        generator = QuestUIGenerator(output_dir=Path("test_ui"))
        element_path = generator.generate_ui_element(
            element_type="indicator",
            variant="awakening",
            score=75,
        )
        assert element_path.exists()

    def test_generate_ui_invalid_type(self) -> None:
        """Test génération avec type invalide"""
        generator = QuestUIGenerator(output_dir=Path("test_ui"))
        try:
            generator.generate_ui_element(
                element_type="invalid",
                variant="serenity",
            )
            assert False, "Devrait lever ValueError"
        except ValueError:
            pass

    def test_generate_all_ui_elements(self) -> None:
        """Test génération de tous les éléments UI"""
        generator = QuestUIGenerator(output_dir=Path("test_ui"))
        elements = generator.generate_all_ui_elements(variant="serenity")
        assert len(elements) > 0

    def test_generate_all_ui_elements_specific_type(self) -> None:
        """Test génération de tous les éléments d'un type"""
        generator = QuestUIGenerator(output_dir=Path("test_ui"))
        elements = generator.generate_all_ui_elements(
            variant="serenity", element_type="button"
        )
        assert len(elements) == 1  # 1 bouton
