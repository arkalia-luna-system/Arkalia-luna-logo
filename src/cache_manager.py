"""
💾 Cache Manager Module
Gestionnaire de cache Redis pour optimiser les performances
"""

import hashlib
import json
import logging
from pathlib import Path
from typing import Any, Optional

try:
    import redis  # type: ignore[import-untyped,import-not-found]
except ImportError:
    redis = None  # type: ignore[assignment]

logger = logging.getLogger(__name__)


class CacheManager:
    """
    Gestionnaire de cache Redis pour les logos générés

    Fonctionnalités :
    - Cache des logos SVG générés
    - Cache des résultats de génération IA
    - Invalidation automatique
    - Fallback si Redis indisponible
    """

    def __init__(
        self,
        redis_host: str = "localhost",
        redis_port: int = 6379,
        redis_db: int = 0,
        enabled: bool = True,
    ) -> None:
        """
        Initialise le gestionnaire de cache

        Args:
            redis_host: Hôte Redis
            redis_port: Port Redis
            redis_db: Base de données Redis
            enabled: Activer le cache
        """
        self.enabled = enabled and redis is not None
        self.redis_client: Optional[Any] = None

        if self.enabled:
            try:
                self.redis_client = redis.Redis(
                    host=redis_host,
                    port=redis_port,
                    db=redis_db,
                    decode_responses=True,
                    socket_connect_timeout=2,
                    socket_timeout=2,
                )
                # Test de connexion
                self.redis_client.ping()
                logger.info(
                    f"✅ Cache Redis connecté : {redis_host}:{redis_port}/{redis_db}"
                )
            except Exception as e:
                logger.warning(f"⚠️ Redis indisponible, cache désactivé : {e}")
                self.enabled = False
                self.redis_client = None
        else:
            if not enabled:
                logger.info("Cache Redis désactivé (paramètre enabled=False)")
            elif redis is None:
                logger.info("Cache Redis désactivé (module redis non installé)")

    def _generate_cache_key(
        self,
        generator_type: str,
        variant: str,
        size: int,
        emotion_variant: Optional[str] = None,
        **kwargs: Any,
    ) -> str:
        """
        Génère une clé de cache unique

        Args:
            generator_type: Type de générateur
            variant: Variante du logo
            size: Taille
            emotion_variant: Variante émotionnelle optionnelle
            **kwargs: Paramètres supplémentaires

        Returns:
            Clé de cache
        """
        cache_data = {
            "generator": generator_type,
            "variant": variant,
            "size": size,
            "emotion": emotion_variant,
            **kwargs,
        }
        cache_str = json.dumps(cache_data, sort_keys=True)
        cache_hash = hashlib.md5(cache_str.encode()).hexdigest()
        return f"arkalia:logo:{cache_hash}"

    def get_cached_logo_path(
        self,
        generator_type: str,
        variant: str,
        size: int,
        emotion_variant: Optional[str] = None,
        **kwargs: Any,
    ) -> Optional[Path]:
        """
        Récupère le chemin d'un logo depuis le cache

        Args:
            generator_type: Type de générateur
            variant: Variante du logo
            size: Taille
            emotion_variant: Variante émotionnelle optionnelle
            **kwargs: Paramètres supplémentaires

        Returns:
            Chemin du logo si trouvé, None sinon
        """
        if not self.enabled or not self.redis_client:
            return None

        try:
            cache_key = self._generate_cache_key(
                generator_type, variant, size, emotion_variant, **kwargs
            )
            cached_path = self.redis_client.get(cache_key)

            if cached_path:
                logo_path = Path(cached_path)
                if logo_path.exists():
                    logger.debug(f"✅ Cache hit : {cache_key}")
                    return logo_path
                else:
                    # Fichier supprimé, invalider le cache
                    self.redis_client.delete(cache_key)
                    logger.debug(f"🗑️ Cache invalidé (fichier manquant) : {cache_key}")

            return None
        except Exception as e:
            logger.warning(f"Erreur lecture cache Redis : {e}")
            return None

    def cache_logo_path(
        self,
        logo_path: Path,
        generator_type: str,
        variant: str,
        size: int,
        emotion_variant: Optional[str] = None,
        ttl: int = 86400,  # 24 heures par défaut
        **kwargs: Any,
    ) -> bool:
        """
        Met en cache le chemin d'un logo généré

        Args:
            logo_path: Chemin du logo généré
            generator_type: Type de générateur
            variant: Variante du logo
            size: Taille
            emotion_variant: Variante émotionnelle optionnelle
            ttl: Time to live en secondes (défaut: 24h)
            **kwargs: Paramètres supplémentaires

        Returns:
            True si mis en cache, False sinon
        """
        if not self.enabled or not self.redis_client:
            return False

        try:
            cache_key = self._generate_cache_key(
                generator_type, variant, size, emotion_variant, **kwargs
            )
            self.redis_client.setex(cache_key, ttl, str(logo_path.absolute()))
            logger.debug(f"💾 Cache mis à jour : {cache_key}")
            return True
        except Exception as e:
            logger.warning(f"Erreur écriture cache Redis : {e}")
            return False

    def invalidate_cache(
        self,
        generator_type: Optional[str] = None,
        variant: Optional[str] = None,
    ) -> int:
        """
        Invalide le cache selon des critères

        Args:
            generator_type: Type de générateur (None = tous)
            variant: Variante (None = toutes)

        Returns:
            Nombre de clés invalidées
        """
        if not self.enabled or not self.redis_client:
            return 0

        try:
            pattern = "arkalia:logo:*"
            keys = self.redis_client.keys(pattern)

            if not keys:
                return 0

            # Filtrer selon les critères
            if generator_type or variant:
                filtered_keys = []
                for key in keys:
                    cached_data = self.redis_client.get(key)
                    if cached_data:
                        # Vérifier les critères (simplifié)
                        if generator_type and generator_type not in cached_data:
                            continue
                        if variant and variant not in cached_data:
                            continue
                        filtered_keys.append(key)
                keys = filtered_keys

            if keys:
                deleted = self.redis_client.delete(*keys)
                logger.info(f"🗑️ Cache invalidé : {deleted} clé(s)")
                return deleted

            return 0
        except Exception as e:
            logger.warning(f"Erreur invalidation cache Redis : {e}")
            return 0

    def get_cache_stats(self) -> dict[str, Any]:
        """
        Retourne les statistiques du cache

        Returns:
            Statistiques du cache
        """
        if not self.enabled or not self.redis_client:
            return {
                "enabled": False,
                "connected": False,
                "keys_count": 0,
            }

        try:
            pattern = "arkalia:logo:*"
            keys = self.redis_client.keys(pattern)
            return {
                "enabled": True,
                "connected": True,
                "keys_count": len(keys),
                "host": self.redis_client.connection_pool.connection_kwargs.get(
                    "host", "unknown"
                ),
                "port": self.redis_client.connection_pool.connection_kwargs.get(
                    "port", "unknown"
                ),
            }
        except Exception as e:
            logger.warning(f"Erreur stats cache Redis : {e}")
            return {
                "enabled": True,
                "connected": False,
                "keys_count": 0,
                "error": str(e),
            }

    def clear_all_cache(self) -> int:
        """
        Vide tout le cache

        Returns:
            Nombre de clés supprimées
        """
        return self.invalidate_cache()
