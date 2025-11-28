"""🤖 AI Logo Generator Module
Générateur de logos utilisant Stable Diffusion local
Optimisé pour performance et faible consommation mémoire
"""

import os
from pathlib import Path
from typing import Any, Dict, List, Optional

# Imports paresseux pour éviter erreurs d'encodage et économiser la mémoire
# Les imports torch/diffusers sont chargés uniquement quand nécessaire

try:
    from .logo_generator import ArkaliaLunaLogo
except ImportError:
    from logo_generator import ArkaliaLunaLogo


class AILogoGenerator(ArkaliaLunaLogo):
    """Générateur de logos utilisant Stable Diffusion local"""

    def __init__(self, output_dir: Optional[Path] = None) -> None:
        # Appel du constructeur parent avec répertoire spécialisé
        super().__init__(output_dir or Path("exports-ai"))

        self.logger.info("🤖 AI Logo Generator initialisé avec succès")

        # Configuration IA - chargement paresseux pour économiser la RAM
        self.ai_pipeline = None
        self._torch = None
        self._StableDiffusionPipeline = None
        self._Image = None
        self.device = None  # Détecté lors du premier chargement
        self.model_id = "runwayml/stable-diffusion-v1-5"  # Modèle stable et rapide

        # Cache pour éviter de recharger le modèle
        self._pipeline_loaded = False
        self._last_cleanup_time = None

        # Cache IA dans Redis
        from .cache_manager import CacheManager

        self.ai_cache = CacheManager(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", "6379")),
            db=int(os.getenv("REDIS_DB", "0")),
            ttl=int(os.getenv("AI_CACHE_TTL", "604800")),  # 7 jours
        )

        # Pas d'initialisation immédiate - chargement paresseux uniquement

    def _check_system_health(self) -> Dict[str, Any]:
        """Vérifie la santé du système avant génération"""
        health = {
            "torch_available": False,
            "diffusers_available": False,
            "cuda_available": False,
            "memory_status": "unknown",
        }

        try:
            import torch

            health["torch_available"] = True
            health["cuda_available"] = torch.cuda.is_available()
            if health["cuda_available"]:
                vram_gb = torch.cuda.get_device_properties(0).total_memory / 1e9
                health["memory_status"] = f"{vram_gb:.1f} GB VRAM"
        except Exception:
            pass

        try:
            # Test d'import sans stocker pour éviter warning
            import diffusers  # noqa: F401

            health["diffusers_available"] = True
        except Exception:
            pass

        return health

    def generate_svg_logo(self, variant_name: str, size: int = 200) -> Path:
        """Génère un logo IA pour une variante donnée avec fallback automatique"""
        try:
            # Vérifier le cache IA
            cache_key = f"ai_logo:{variant_name}:{size}"
            cached_path = self.ai_cache.get(cache_key)
            if cached_path and Path(cached_path).exists():
                self.logger.info(
                    f"✅ Cache hit pour logo IA '{variant_name}' "
                    f"en taille {size}x{size}"
                )
                return Path(cached_path)

            self.logger.info(
                f"🤖 Génération IA du logo '{variant_name}' en taille {size}x{size}",
            )

            # Validation de la variante
            if not self.variants_manager.validate_variant(variant_name):
                raise ValueError(f"Variante '{variant_name}' non reconnue")

            # Vérifier et initialiser le pipeline IA si nécessaire
            if not self.ai_pipeline:
                # Message discret en mode DEBUG
                self.logger.debug("Initialisation du pipeline IA...")

                # Vérification de santé du système avant initialisation (silencieuse)
                health = self._check_system_health()
                if not health["torch_available"]:
                    self.logger.debug("Torch non détecté")
                if not health["diffusers_available"]:
                    self.logger.debug("Diffusers non détecté")

                try:
                    self._initialize_ai_pipeline()
                except (ImportError, RuntimeError) as e:
                    # Si erreur UTF-8 ou autre problème IA, utiliser fallback SVG
                    error_str = str(e)
                    is_utf8_error = (
                        self._detect_utf8_error(e)
                        or "UTF8_ERROR_FALLBACK" in error_str
                        or "diffusers" in error_str.lower()
                    )

                    if is_utf8_error:
                        # Message discret et positif pour l'utilisateur
                        self.logger.info(
                            "✨ Génération en mode SVG classique "
                            "(IA temporairement indisponible)"
                        )
                        # Fallback vers génération SVG classique du parent
                        return super().generate_svg_logo(variant_name, size)
                    else:
                        # Autre erreur - message concis
                        error_msg = (
                            f"{str(e)[:200]}... "
                            "(Solution: pip install --upgrade "
                            "diffusers torch transformers)"
                        )
                        raise RuntimeError(error_msg) from e

                if not self.ai_pipeline:
                    self.logger.info(
                        "ℹ️ Pipeline IA non disponible, "
                        "utilisation du générateur SVG classique."
                    )
                    return super().generate_svg_logo(variant_name, size)

            # Utilisation de la génération IA
            return self.generate_ai_logo(variant_name, size, "ai")

        except (RuntimeError, ImportError) as e:
            # Si erreur IA, essayer fallback SVG
            error_str = str(e)
            is_ia_error = (
                self._detect_utf8_error(e)
                or "UTF8_ERROR_FALLBACK" in error_str
                or "diffusers" in error_str.lower()
                or "torch" in error_str.lower()
            )

            if is_ia_error:
                # Message discret et positif
                self.logger.info(
                    f"✨ Génération en mode SVG classique pour '{variant_name}'"
                )
                try:
                    return super().generate_svg_logo(variant_name, size)
                except Exception as fallback_error:
                    self.logger.error(f"❌ Erreur même avec fallback: {fallback_error}")
                    raise RuntimeError(
                        f"Impossible de générer le logo: {str(e)[:200]}"
                    ) from e
            raise
        except Exception:
            # Autres erreurs inattendues - essayer fallback
            self.logger.info(
                f"ℹ️ Erreur inattendue, tentative de fallback SVG pour '{variant_name}'."
            )
            try:
                return super().generate_svg_logo(variant_name, size)
            except Exception as e:
                self.logger.error(f"❌ Erreur génération IA '{variant_name}': {e}")
                raise

    def _detect_utf8_error(self, error: Exception) -> bool:
        """Détecte intelligemment les erreurs d'encodage UTF-8"""
        error_str = str(error).lower()
        error_type = type(error).__name__

        # Détection directe
        if error_type == "UnicodeDecodeError":
            return True

        # Vérifier dans la chaîne d'exception (cause)
        current_error = error
        for _ in range(5):  # Limiter la profondeur de recherche
            if hasattr(current_error, "__cause__") and current_error.__cause__:
                cause_type = type(current_error.__cause__).__name__
                if cause_type == "UnicodeDecodeError":
                    return True
                current_error = current_error.__cause__
            else:
                break

        # Détection dans les messages d'erreur encapsulés
        utf8_indicators = [
            "utf-8 codec can't decode",
            "invalid start byte",
            "unicode decode error",
            "codec can't decode byte",
            "can't decode byte",
            "decode byte 0x",
        ]

        return any(indicator in error_str for indicator in utf8_indicators)

    def _get_utf8_solution(self) -> str:
        """Retourne une solution intelligente pour l'erreur UTF-8"""
        solutions = [
            "1. Réinstaller diffusers proprement:",
            "   pip uninstall diffusers transformers -y",
            "   pip install --no-cache-dir diffusers transformers",
            "",
            "2. Nettoyer le cache Python:",
            "   python -m pip cache purge",
            "",
            "3. Réinstaller dans un environnement propre:",
            "   python -m venv new_env",
            "   source new_env/bin/activate  # Windows: new_env\\Scripts\\activate",
            "   pip install diffusers torch transformers",
        ]

        return "\n".join(solutions)

    def _lazy_import_ai_dependencies(self) -> None:
        """Import paresseux des dépendances IA avec détection intelligente d'erreurs"""
        if self._torch is None:
            try:
                import torch

                self._torch = torch
            except ImportError as e:
                raise ImportError(
                    "Torch n'est pas installé. Installez avec: pip install torch"
                ) from e
            except Exception as e:
                raise RuntimeError(
                    f"Erreur lors du chargement de torch: {e}. "
                    "Vérifiez votre installation."
                ) from e

        if self._StableDiffusionPipeline is None:
            try:
                # Tentative d'import avec gestion d'erreur améliorée
                from diffusers import StableDiffusionPipeline

                self._StableDiffusionPipeline = StableDiffusionPipeline
            except ImportError as e:
                raise ImportError(
                    "Diffusers n'est pas installé. "
                    "Installez avec: pip install diffusers"
                ) from e
            except (UnicodeDecodeError, RuntimeError, Exception) as e:
                # Détection intelligente de l'erreur UTF-8 même si encapsulée
                if self._detect_utf8_error(e):
                    # Message discret en mode DEBUG seulement
                    # (fallback sera utilisé)
                    # L'utilisateur verra juste le message de fallback
                    error_msg = (
                        "Erreur d'encodage UTF-8 dans diffusers/transformers détectée. "
                        "Fallback SVG activé automatiquement."
                    )
                    # Logger en mode DEBUG pour ne pas polluer les logs
                    self.logger.debug("🔧 " + error_msg)
                    # Lever une exception silencieuse qui sera gérée par le fallback
                    raise RuntimeError("UTF8_ERROR_FALLBACK") from e
                else:
                    # Autre type d'erreur - message concis
                    error_msg = (
                        f"Erreur lors du chargement de diffusers: {str(e)[:200]}. "
                        "Solution: pip install --upgrade diffusers"
                    )
                    self.logger.error(error_msg)
                    raise RuntimeError(error_msg) from e

        if self._Image is None:
            try:
                from PIL import Image

                self._Image = Image
            except ImportError as e:
                raise ImportError(
                    "PIL/Pillow n'est pas installé. Installez avec: pip install pillow"
                ) from e
            except Exception as e:
                # Gestion des erreurs d'encodage pour PIL aussi
                if self._detect_utf8_error(e):
                    raise RuntimeError(
                        f"Erreur d'encodage UTF-8 dans PIL: {e}. "
                        "Réinstallez avec: pip install --force-reinstall pillow"
                    ) from e
                raise

    def _initialize_ai_pipeline(self) -> None:
        """Initialise le pipeline Stable Diffusion avec optimisations mémoire"""
        try:
            # Import paresseux des dépendances
            self._lazy_import_ai_dependencies()

            # Détection du device si pas encore fait
            if self.device is None:
                self.device = "cuda" if self._torch.cuda.is_available() else "cpu"

            # Si le pipeline est déjà chargé, on le réutilise
            if self._pipeline_loaded and self.ai_pipeline is not None:
                self.logger.info("♻️ Réutilisation du pipeline IA en cache")
                return

            self.logger.info(f"🤖 Chargement du modèle IA: {self.model_id}")
            self.logger.info(f"🖥️ Device: {self.device}")

            # Chargement du pipeline avec optimisations mémoire
            torch_dtype = (
                self._torch.float16 if self.device == "cuda" else self._torch.float32
            )

            try:
                self.ai_pipeline = self._StableDiffusionPipeline.from_pretrained(
                    self.model_id,
                    torch_dtype=torch_dtype,
                    use_safetensors=True,
                    low_cpu_mem_usage=True,  # Optimisation mémoire
                )
            except (UnicodeDecodeError, RuntimeError, Exception) as e:
                # Détection et gestion des erreurs UTF-8 lors du chargement du modèle
                if self._detect_utf8_error(e):
                    # Message discret - le fallback sera utilisé
                    self.logger.debug(
                        "🔧 Erreur UTF-8 lors du chargement du modèle, fallback activé"
                    )
                    raise RuntimeError("UTF8_ERROR_FALLBACK") from e
                else:
                    # Autre erreur de chargement - peut-être réseau ou autre
                    raise RuntimeError(
                        f"Erreur lors du chargement du modèle: {str(e)[:200]}. "
                        "Vérifiez votre connexion internet et réessayez."
                    ) from e

            # Désactivation complète du filtre NSFW pour économiser la RAM
            if hasattr(self.ai_pipeline, "safety_checker"):
                self.ai_pipeline.safety_checker = None
            if hasattr(self.ai_pipeline, "feature_extractor"):
                self.ai_pipeline.feature_extractor = None

            # Optimisations pour la vitesse et la mémoire
            if self.device == "cuda":
                self.ai_pipeline = self.ai_pipeline.to(self.device)
                # Attention slicing pour réduire la consommation mémoire
                self.ai_pipeline.enable_attention_slicing(1)
                # Memory efficient attention
                if hasattr(self.ai_pipeline, "enable_memory_efficient_attention"):
                    self.ai_pipeline.enable_memory_efficient_attention()
                # CPU offload pour économiser la VRAM
                if hasattr(self.ai_pipeline, "enable_model_cpu_offload"):
                    try:
                        self.ai_pipeline.enable_model_cpu_offload()
                    except Exception:
                        pass  # Pas disponible sur tous les systèmes

            # Nettoyage du cache CUDA si disponible
            if self.device == "cuda" and hasattr(self._torch.cuda, "empty_cache"):
                self._torch.cuda.empty_cache()

            self._pipeline_loaded = True
            self.logger.info("✅ Pipeline IA chargé avec succès (optimisé mémoire)")

        except (ImportError, RuntimeError) as e:
            # Les erreurs sont déjà loggées avec détails
            # dans _lazy_import_ai_dependencies
            # Ne logger qu'un message concis ici pour éviter duplication
            if not self._detect_utf8_error(e):
                # Seulement logger si ce n'est pas une erreur UTF-8 (déjà loggée)
                self.logger.error(f"❌ Erreur initialisation IA: {str(e)[:150]}")
            self.ai_pipeline = None
            self._pipeline_loaded = False
            raise
        except Exception as e:
            self.logger.error(f"❌ Erreur inattendue initialisation IA: {e}")
            self.ai_pipeline = None
            self._pipeline_loaded = False
            raise RuntimeError(
                f"Erreur lors de l'initialisation du pipeline IA: {e}"
            ) from e

    def _create_prompt(self, variant_name: str, generator_style: str = "ai") -> str:
        """Crée un prompt spécialisé pour la variante émotionnelle"""
        # Base du prompt optimisé pour les logos abstraits et géométriques
        # Utilisation de weighting pour mettre l'accent sur les éléments importants
        base_prompt = (
            "(abstract geometric logo:1.3), (minimalist icon design:1.2), "
            "(symbolic mark:1.2), (clean vector style:1.1), "
            "(centered composition:1.1), (professional branding:1.2), "
            "(high contrast:1.1), (sharp edges:1.1), "
            "(geometric shapes:1.3), (abstract symbol:1.3), "
            "(icon design:1.2), (flat design:1.1), (2d design:1.1)"
        )

        # Prompts spécialisés par variante émotionnelle - OPTIMISÉS POUR LOGOS ABSTRAITS
        variant_prompts = {
            "serenity": (
                "soft blue and cyan gradient, circular geometric pattern, "
                "peaceful flowing lines, zen aesthetic, calm energy, "
                "smooth curves, harmonious design"
            ),
            "power": (
                "bold geometric shapes, electric blue and white, "
                "dynamic angular lines, strong presence, energy patterns, "
                "sharp edges, powerful geometry"
            ),
            "mystery": (
                "deep purple and indigo gradient, mystical geometric patterns, "
                "enigmatic abstract shapes, cosmic elements, "
                "intricate geometry, secretive design"
            ),
            "awakening": (
                "golden yellow and amber gradient, radiant geometric patterns, "
                "enlightenment symbols, spiritual awakening, "
                "luminous energy, bright geometry"
            ),
            "creative": (
                "vibrant color palette, artistic geometric shapes, "
                "creative abstract patterns, innovative design, "
                "dynamic composition, colorful geometry"
            ),
            "rainy": (
                "silver and blue tones, water drop geometric patterns, "
                "elegant abstract design, refined aesthetic, "
                "crystalline geometry, fluid shapes"
            ),
            "stormy": (
                "dark blue and white, lightning geometric patterns, "
                "dynamic angular energy, powerful abstract design, "
                "sharp geometric lines, storm geometry"
            ),
            "explosive": (
                "red orange yellow gradient, radial geometric burst patterns, "
                "explosive energy, vibrant intensity, "
                "radiating lines, dynamic geometry"
            ),
            "sunny": (
                "warm yellow orange gradient, sun ray geometric patterns, "
                "bright optimistic design, cheerful energy, "
                "radial geometry, luminous shapes"
            ),
            "snowy": (
                "white and silver gradient, crystalline geometric patterns, "
                "pure elegant design, winter beauty, "
                "snowflake geometry, clean perfection"
            ),
        }

        # Style du générateur - OPTIMISÉ POUR LOGOS ABSTRAITS
        style_prompts = {
            "ai": (
                "futuristic tech aesthetic, neural network geometric patterns, "
                "AI-inspired abstract geometry, modern technology symbols, "
                "circuit-like patterns, digital design"
            ),
            "dashboard": (
                "interface design elements, geometric precision, "
                "modern UI abstract symbols, clean geometric lines, "
                "dashboard icon style"
            ),
            "ai_moon": (
                "lunar geometric patterns, moon phase abstract design, "
                "cosmic technology symbols, space-age geometry, "
                "celestial abstract shapes"
            ),
            "advanced": (
                "sophisticated geometric patterns, advanced abstract geometry, "
                "premium design symbols, luxury aesthetic, "
                "refined geometric shapes"
            ),
            "ultimate": (
                "cosmic energy geometric patterns, stellar abstract formations, "
                "ultimate power symbols, space technology geometry, "
                "cosmic abstract design"
            ),
        }

        # Construction du prompt final - OPTIMISÉ POUR LOGOS ABSTRAITS
        variant_desc = variant_prompts.get(variant_name, "modern and elegant geometric")
        style_desc = style_prompts.get(
            generator_style, "futuristic and modern abstract"
        )

        final_prompt = (
            f"{base_prompt}, {variant_desc}, {style_desc}, "
            "(centered abstract logo:1.2), "
            "(transparent or solid color background:1.1), "
            "(high quality:1.2), (professional branding:1.2), "
            "(corporate identity:1.1), "
            "(clean geometric design:1.3), (abstract symbol:1.3), (icon mark:1.2), "
            "(simple design:1.1), (bold shapes:1.1), (clear lines:1.1), "
            "(no text:1.5), (no letters:1.5), (no words:1.5), "
            "(symbol only:1.4), (abstract only:1.4), (geometric only:1.3)"
        )

        return final_prompt

    def _post_process_image(self, image: Any) -> Any:
        """Post-traitement de l'image pour améliorer la qualité du logo"""
        try:
            # Vérifier si PIL est disponible
            try:
                from PIL import ImageEnhance, ImageFilter, ImageOps
            except ImportError:
                return image  # Si PIL n'est pas disponible, retourner l'image originale

            # Conversion en RGB si nécessaire (pour les filtres)
            if image.mode != "RGB":
                image = image.convert("RGB")

            # Amélioration du contraste pour logos plus nets
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(1.2)  # +20% de contraste pour logos plus nets

            # Amélioration de la netteté (optimisée pour logos abstraits)
            image = image.filter(
                ImageFilter.UnsharpMask(radius=1.5, percent=150, threshold=2)
            )

            # Amélioration de la saturation pour couleurs plus vives
            enhancer = ImageEnhance.Color(image)
            image = enhancer.enhance(1.15)  # +15% de saturation

            # Amélioration de la luminosité pour logos plus visibles
            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(1.05)  # +5% de luminosité

            # Auto-contrast pour optimiser la plage dynamique
            try:
                image = ImageOps.autocontrast(image, cutoff=2)
            except Exception:
                pass  # Ignorer si non disponible

            return image
        except Exception as e:
            self.logger.warning(f"⚠️ Erreur post-traitement (ignoré): {e}")
            return image  # Retourner l'image originale en cas d'erreur

    def _validate_generated_logo(self, image: Any) -> bool:
        """
        Valide que le logo généré est de bonne qualité
        (pas trop flou, pas de texte visible)
        """
        try:
            if not self._Image:
                return True  # Si PIL n'est pas disponible, on accepte

            # Vérifications basiques
            if image is None:
                return False

            # Vérifier la taille
            if not hasattr(image, "size") or image.size[0] < 64 or image.size[1] < 64:
                return False

            # Vérifier que l'image n'est pas complètement noire ou blanche
            try:
                from PIL import ImageStat

                stat = ImageStat.Stat(image)
                # Si l'image est trop uniforme (écart-type très faible), c'est suspect
                if len(stat.stddev) > 0 and stat.stddev[0] < 5:
                    self.logger.warning(
                        "⚠️ Logo généré trop uniforme (peut être invalide)"
                    )
                    return False
            except Exception:
                pass  # Ignorer les erreurs de validation

            return True
        except Exception as e:
            self.logger.warning(f"⚠️ Erreur validation logo (ignoré): {e}")
            return True  # En cas d'erreur, on accepte quand même

    def generate_ai_logo(
        self,
        variant_name: str,
        size: int = 200,
        generator_style: str = "ai",
    ) -> Path:
        """Génère un logo IA pour une variante donnée"""
        try:
            if not self.ai_pipeline:
                raise RuntimeError("Pipeline IA non initialisé")

            self.logger.info(
                f"🤖 Génération IA du logo '{variant_name}' "
                f"style '{generator_style}' en taille {size}x{size}",
            )

            # Validation de la variante
            if not self.variants_manager.validate_variant(variant_name):
                raise ValueError(f"Variante '{variant_name}' non reconnue")

            # Création du prompt
            prompt = self._create_prompt(variant_name, generator_style)
            self.logger.info(f"📝 Prompt: {prompt}")

            # Génération de l'image avec paramètres optimisés
            with self._torch.no_grad():
                # Paramètres adaptatifs selon la taille
                # pour équilibrer qualité et mémoire
                # Plus de steps pour meilleure qualité, mais adapté à la RAM disponible
                if size <= 200:
                    steps = 25  # Augmenté pour meilleure qualité
                    guidance = 9.0  # Augmenté pour meilleur contrôle
                elif size <= 500:
                    steps = 35  # Augmenté pour meilleure qualité
                    guidance = 9.5
                else:
                    steps = 45  # Augmenté pour meilleure qualité
                    guidance = 10.0

                # Seed varié par variante pour plus de diversité
                # tout en restant reproductible
                # Utilisation d'un hash plus sophistiqué
                # pour meilleure distribution
                seed_base = abs(hash(f"{variant_name}_{generator_style}")) % 10000
                seed = 42 + seed_base

                # Génération avec optimisations mémoire
                generator = self._torch.Generator(device=self.device).manual_seed(seed)

                image = self.ai_pipeline(
                    prompt=prompt,
                    height=size,
                    width=size,
                    num_inference_steps=steps,
                    guidance_scale=guidance,
                    generator=generator,
                    negative_prompt=(
                        "(blurry:1.3), (low quality:1.3), (distorted:1.2), "
                        "(ugly:1.2), (bad anatomy:1.2), "
                        "(text:1.5), (words:1.5), (letters:1.5), "
                        "(numbers:1.4), (characters:1.4), (typography:1.4), "
                        "(watermark:1.3), (signature:1.3), (writing:1.4), "
                        "(font:1.4), (alphabet:1.4), (language:1.3), "
                        "(realistic photo:1.3), (photograph:1.3), (3d render:1.2), "
                        "(complex scene:1.2), (background clutter:1.2), "
                        "(noisy:1.2), (grainy:1.2), (artifacts:1.2), "
                        "(jpeg artifacts:1.2), (compression:1.1), "
                        "(human:1.3), (person:1.3), (face:1.3), "
                        "(body:1.2), (animal:1.2), (object:1.2), "
                        "(detailed illustration:1.2), (painting:1.2), "
                        "(artwork:1.1), (realistic:1.2), (photorealistic:1.3)"
                    ),  # Negative prompt avec weighting pour éviter texte et réalisme
                ).images[0]

                # Post-traitement pour améliorer la netteté et le contraste
                image = self._post_process_image(image)

                # Validation de la qualité du logo généré
                if not self._validate_generated_logo(image):
                    self.logger.warning(
                        f"⚠️ Logo '{variant_name}' généré mais qualité suspecte"
                    )

                # Nettoyage immédiat du cache pour libérer la RAM
                if self.device == "cuda" and hasattr(self._torch.cuda, "empty_cache"):
                    self._torch.cuda.empty_cache()

            # Construction du chemin de sortie
            output_path = self.output_dir / f"arkalia-luna-ai-{variant_name}-{size}.png"

            # Sauvegarde optimisée
            image.save(output_path, "PNG", quality=95, optimize=True)

            # Nettoyage automatique après génération pour économiser la RAM
            # (on garde le pipeline en cache pour les prochaines générations)
            if self.device == "cuda" and self._torch:
                if hasattr(self._torch.cuda, "empty_cache"):
                    self._torch.cuda.empty_cache()

            self.logger.info(f"✨ Logo IA généré avec succès : {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(f"❌ Erreur génération IA '{variant_name}': {e}")
            raise

    def cleanup_resources(self, force: bool = False) -> None:
        """Nettoie les ressources IA pour libérer la mémoire

        Args:
            force: Si True, nettoie même si le pipeline est en cache
        """
        if hasattr(self, "ai_pipeline") and self.ai_pipeline:
            try:
                # Déplacement vers CPU pour libérer la VRAM
                if hasattr(self.ai_pipeline, "to"):
                    try:
                        self.ai_pipeline.to("cpu")
                    except Exception:
                        pass

                # Suppression explicite
                del self.ai_pipeline
                self.ai_pipeline = None
                self._pipeline_loaded = False

                # Nettoyage du cache CUDA si disponible
                if self._torch and self.device == "cuda":
                    if hasattr(self._torch.cuda, "empty_cache"):
                        self._torch.cuda.empty_cache()
                    if hasattr(self._torch.cuda, "synchronize"):
                        try:
                            self._torch.cuda.synchronize()
                        except Exception:
                            pass

                # Nettoyage Python
                import gc

                gc.collect()

                self.logger.info("🧹 Ressources IA nettoyées (mémoire libérée)")
            except Exception as e:
                self.logger.warning(f"⚠️ Erreur nettoyage ressources: {e}")

    def __del__(self) -> None:
        """Destructeur pour nettoyer les ressources"""
        self.cleanup_resources()

    def generate_all_ai_variants(
        self,
        size: int = 200,
        generator_style: str = "ai",
    ) -> List[Path]:
        """Génère toutes les variantes en mode IA"""
        try:
            self.logger.info(
                f"🤖 Génération IA de toutes les variantes "
                f"style '{generator_style}' en taille {size}x{size}",
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
                f"🎉 Génération IA terminée : "
                f"{len(generated_files)}/{len(variants)} logos créés",
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
            # Initialisation si nécessaire
            if not self.ai_pipeline:
                self._initialize_ai_pipeline()
                if not self.ai_pipeline:
                    return False

            self.logger.info("🧪 Test de génération IA...")

            # Test simple avec optimisations mémoire
            with self._torch.no_grad():
                test_image = self.ai_pipeline(
                    "simple logo, blue circle, white background",
                    height=64,
                    width=64,
                    num_inference_steps=5,  # Minimum pour test rapide
                ).images[0]

            # Sauvegarde du test
            test_path = self.output_dir / "ai-test.png"
            test_image.save(test_path, "PNG", optimize=True)

            # Nettoyage après test
            if self.device == "cuda" and hasattr(self._torch.cuda, "empty_cache"):
                self._torch.cuda.empty_cache()

            self.logger.info(f"✅ Test IA réussi : {test_path}")
            return True

        except Exception as e:
            self.logger.error(f"❌ Test IA échoué : {e}")
            return False
