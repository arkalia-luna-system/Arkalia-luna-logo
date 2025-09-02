"""
🤖 AI Logo Generator Module
Générateur de logos utilisant Stable Diffusion local
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import torch
    from diffusers import StableDiffusionPipeline
    from PIL import Image
except ImportError:
    StableDiffusionPipeline = None
    torch = None
    Image = None

try:
    from .logo_generator import ArkaliaLunaLogo
except ImportError:
    from logo_generator import ArkaliaLunaLogo


class AILogoGenerator(ArkaliaLunaLogo):
    """Générateur de logos utilisant Stable Diffusion local"""

    def __init__(self, output_dir: Optional[Path] = None):
        # Appel du constructeur parent avec répertoire spécialisé
        super().__init__(output_dir or Path("exports-ai"))

        self.logger.info("🤖 AI Logo Generator initialisé avec succès")

        # Configuration IA
        self.ai_pipeline = None
        self.device = "cuda" if torch and torch.cuda.is_available() else "cpu"
        self.model_id = "runwayml/stable-diffusion-v1-5"  # Modèle stable et rapide

        # Initialisation du pipeline IA
        self._initialize_ai_pipeline()

    def generate_svg_logo(self, variant_name: str, size: int = 200) -> Path:
        """Génère un logo IA pour une variante donnée"""
        try:
            self.logger.info(
                f"🤖 Génération IA du logo '{variant_name}' en taille {size}x{size}"
            )

            # Validation de la variante
            if not self.variants_manager.validate_variant(variant_name):
                raise ValueError(f"Variante '{variant_name}' non reconnue")

            # Utilisation de la génération IA
            return self.generate_ai_logo(variant_name, size, "ai")

        except Exception as e:
            self.logger.error(f"❌ Erreur génération IA '{variant_name}': {e}")
            raise

    def _initialize_ai_pipeline(self):
        """Initialise le pipeline Stable Diffusion"""
        try:
            if not StableDiffusionPipeline:
                raise ImportError(
                    "Diffusers non installé. Installez avec: pip install diffusers torch"
                )

            self.logger.info(f"🤖 Chargement du modèle IA: {self.model_id}")
            self.logger.info(f"🖥️ Device: {self.device}")

            # Chargement du pipeline avec optimisations
            self.ai_pipeline = StableDiffusionPipeline.from_pretrained(
                self.model_id,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                use_safetensors=True,
                safety_checker=None,  # Désactiver le filtre NSFW
                requires_safety_checker=False,
            )

            # Optimisations pour la vitesse
            if self.device == "cuda":
                self.ai_pipeline = self.ai_pipeline.to(self.device)
                self.ai_pipeline.enable_attention_slicing()
                self.ai_pipeline.enable_memory_efficient_attention()

            self.logger.info("✅ Pipeline IA chargé avec succès")

        except Exception as e:
            self.logger.error(f"❌ Erreur initialisation IA: {e}")
            self.ai_pipeline = None

    def _create_prompt(self, variant_name: str, generator_style: str = "ai") -> str:
        """Crée un prompt spécialisé pour la variante émotionnelle"""

        # Base du prompt
        base_prompt = "Arkalia-LUNA logo, modern minimalist design, high quality, professional, safe for work, clean design"

        # Prompts spécialisés par variante émotionnelle
        variant_prompts = {
            "serenity": "calm blue tones, peaceful atmosphere, gentle glow, serene and mystical",
            "power": "electric energy, vibrant colors, dynamic movement, powerful and intense",
            "mystery": "dark purple tones, mysterious atmosphere, enigmatic glow, mystical and secretive",
            "awakening": "golden light, wisdom symbols, enlightened energy, awakening and spiritual",
            "creative": "rainbow colors, creative energy, artistic flow, innovative and inspiring",
            "rainy": "grey tones, water droplets, melancholic but elegant, rainy atmosphere",
            "stormy": "dark stormy colors, lightning bolts, explosive energy, dynamic and intense",
            "explosive": "red orange yellow, explosive particles, radial energy, vibrant and energetic",
            "sunny": "warm yellow orange, sun rays, bright and optimistic, cheerful energy",
            "snowy": "white silver tones, crystalline structure, pure and clean, winter atmosphere",
        }

        # Style du générateur
        style_prompts = {
            "ai": "AI-generated, futuristic, technological, neural network patterns",
            "dashboard": "interface design, geometric patterns, modern UI elements",
            "ai_moon": "lunar surface, moon craters, AI neural networks, cosmic technology",
            "advanced": "advanced technology, complex patterns, sophisticated design",
            "ultimate": "cosmic energy, stellar patterns, ultimate power, space technology",
        }

        # Construction du prompt final
        variant_desc = variant_prompts.get(variant_name, "modern and elegant")
        style_desc = style_prompts.get(generator_style, "futuristic and modern")

        final_prompt = f"{base_prompt}, {variant_desc}, {style_desc}, logo design, vector style, clean background, family friendly, appropriate content"

        return final_prompt

    def generate_ai_logo(
        self, variant_name: str, size: int = 200, generator_style: str = "ai"
    ) -> Path:
        """Génère un logo IA pour une variante donnée"""
        try:
            if not self.ai_pipeline:
                raise RuntimeError("Pipeline IA non initialisé")

            self.logger.info(
                f"🤖 Génération IA du logo '{variant_name}' style '{generator_style}' en taille {size}x{size}"
            )

            # Validation de la variante
            if not self.variants_manager.validate_variant(variant_name):
                raise ValueError(f"Variante '{variant_name}' non reconnue")

            # Création du prompt
            prompt = self._create_prompt(variant_name, generator_style)
            self.logger.info(f"📝 Prompt: {prompt}")

            # Génération de l'image
            with torch.no_grad():
                image = self.ai_pipeline(
                    prompt=prompt,
                    height=size,
                    width=size,
                    num_inference_steps=20,  # Rapide mais qualité correcte
                    guidance_scale=7.5,
                    generator=torch.Generator(device=self.device).manual_seed(
                        42
                    ),  # Reproducible
                ).images[0]

            # Construction du chemin de sortie
            output_path = self.output_dir / f"arkalia-luna-ai-{variant_name}-{size}.png"

            # Sauvegarde
            image.save(output_path, "PNG", quality=95)

            self.logger.info(f"✨ Logo IA généré avec succès : {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(f"❌ Erreur génération IA '{variant_name}': {e}")
            raise

    def generate_all_ai_variants(
        self, size: int = 200, generator_style: str = "ai"
    ) -> List[Path]:
        """Génère toutes les variantes en mode IA"""
        try:
            self.logger.info(
                f"🤖 Génération IA de toutes les variantes style '{generator_style}' en taille {size}x{size}"
            )

            generated_files = []
            variants = self.variants_manager.list_variants()

            for variant in variants:
                try:
                    output_path = self.generate_ai_logo(variant, size, generator_style)
                    generated_files.append(output_path)
                    self.logger.info(f"✅ {variant} : {output_path.name}")
                except Exception as e:
                    self.logger.error(f"❌ {variant} : {e}")
                    continue

            self.logger.info(
                f"🎉 Génération IA terminée : {len(generated_files)}/{len(variants)} logos créés"
            )
            return generated_files

        except Exception as e:
            self.logger.error(f"❌ Erreur génération IA globale: {e}")
            raise

    def get_ai_stats(self) -> Dict[str, Any]:
        """Retourne les statistiques IA"""
        return {
            "ai_pipeline_loaded": self.ai_pipeline is not None,
            "device": self.device,
            "model_id": self.model_id,
            "generator_type": "AI",
            "optimizations": [
                "Stable Diffusion v1.5",
                "Attention slicing",
                "Memory efficient attention",
                "Half precision (CUDA)",
                "Reproducible generation",
            ],
        }

    def test_ai_generation(self) -> bool:
        """Teste la génération IA avec un prompt simple"""
        try:
            if not self.ai_pipeline:
                return False

            self.logger.info("🧪 Test de génération IA...")

            # Test simple
            test_image = self.ai_pipeline(
                "simple logo, blue circle, white background",
                height=64,
                width=64,
                num_inference_steps=5,
            ).images[0]

            # Sauvegarde du test
            test_path = self.output_dir / "ai-test.png"
            test_image.save(test_path)

            self.logger.info(f"✅ Test IA réussi : {test_path}")
            return True

        except Exception as e:
            self.logger.error(f"❌ Test IA échoué : {e}")
            return False
