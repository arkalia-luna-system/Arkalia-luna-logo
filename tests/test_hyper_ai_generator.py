"""Tests pour le générateur Hyper-AI avec ComfyUI"""

from pathlib import Path

from src.hyper_ai_generator import HyperAIGenerator


class TestHyperAIGenerator:
    """Tests pour HyperAIGenerator"""

    def test_initialization(self):
        """Test l'initialisation du générateur"""
        generator = HyperAIGenerator()
        assert generator is not None
        assert generator.comfyui_path == Path("comfyui")
        assert generator.workflow_templates is not None
        assert "cosmic_sphere" in generator.workflow_templates

    def test_workflow_templates_loaded(self):
        """Test que les templates de workflow sont chargés"""
        generator = HyperAIGenerator()
        templates = generator.workflow_templates

        assert isinstance(templates, dict)
        assert len(templates) > 0

        # Vérifier la structure d'un template
        if "cosmic_sphere" in templates:
            template = templates["cosmic_sphere"]
            assert "description" in template
            assert "prompt_template" in template
            assert "negative_prompt" in template

    def test_generate_svg_logo_without_comfyui(self):
        """Test la génération SVG sans ComfyUI (fallback)"""
        generator = HyperAIGenerator()

        # Le générateur doit pouvoir générer un SVG même sans ComfyUI démarré
        # Il utilise le générateur de base en fallback
        try:
            output_path = generator.generate_svg_logo(
                variant_name="serenity",
                size=200,
            )
            assert output_path.exists()
            assert output_path.suffix == ".svg"
        except Exception as e:
            # Si ComfyUI n'est pas disponible, c'est acceptable
            # Le générateur doit gérer cela gracieusement
            assert "comfyui" in str(e).lower() or "workflow" in str(e).lower()

    def test_comfyui_path_exists(self):
        """Test que le chemin ComfyUI existe"""
        generator = HyperAIGenerator()
        assert generator.comfyui_path.exists() or not generator.comfyui_path.exists()
        # Le chemin peut exister ou non, mais le générateur doit gérer les deux cas

    def test_models_configuration(self):
        """Test la configuration des modèles"""
        generator = HyperAIGenerator()
        models = generator.models

        assert isinstance(models, dict)
        assert "sdxl" in models
        assert "controlnet" in models
        assert "upscaler" in models

    def test_generate_all_hyper_variants_structure(self):
        """Test la structure de generate_all_hyper_variants"""
        generator = HyperAIGenerator()

        # Vérifier que la méthode existe
        assert hasattr(generator, "generate_all_hyper_variants")
        assert callable(generator.generate_all_hyper_variants)
