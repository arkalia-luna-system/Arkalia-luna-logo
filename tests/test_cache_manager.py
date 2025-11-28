"""
Tests pour le module CacheManager
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

from src.cache_manager import CacheManager


class TestCacheManager:
    """Tests pour CacheManager"""

    def test_cache_manager_init_disabled(self) -> None:
        """Test initialisation avec cache désactivé"""
        cache = CacheManager(enabled=False)
        assert cache.enabled is False
        assert cache.redis_client is None

    def test_cache_manager_init_no_redis_module(self) -> None:
        """Test initialisation sans module redis"""
        with patch("src.cache_manager.redis", None):
            cache = CacheManager(enabled=True)
            assert cache.enabled is False

    @patch("src.cache_manager.redis")
    def test_cache_manager_init_redis_available(self, mock_redis: MagicMock) -> None:
        """Test initialisation avec Redis disponible"""
        mock_client = MagicMock()
        mock_client.ping.return_value = True
        mock_redis.Redis.return_value = mock_client

        cache = CacheManager(enabled=True)
        assert cache.enabled is True
        assert cache.redis_client is not None

    @patch("src.cache_manager.redis")
    def test_cache_manager_init_redis_unavailable(self, mock_redis: MagicMock) -> None:
        """Test initialisation avec Redis indisponible"""
        mock_redis.Redis.side_effect = Exception("Connection refused")

        cache = CacheManager(enabled=True)
        assert cache.enabled is False
        assert cache.redis_client is None

    def test_generate_cache_key(self) -> None:
        """Test génération de clé de cache"""
        cache = CacheManager(enabled=False)
        key = cache._generate_cache_key(
            generator_type="ultimate",
            variant="serenity",
            size=200,
            emotion_variant=None,
        )
        assert key.startswith("arkalia:logo:")
        assert len(key) > 20

    def test_generate_cache_key_with_emotion(self) -> None:
        """Test génération de clé avec variante émotionnelle"""
        cache = CacheManager(enabled=False)
        key1 = cache._generate_cache_key(
            generator_type="ultimate",
            variant="serenity",
            size=200,
            emotion_variant="power",
        )
        key2 = cache._generate_cache_key(
            generator_type="ultimate",
            variant="serenity",
            size=200,
            emotion_variant="mystery",
        )
        assert key1 != key2

    @patch("src.cache_manager.redis")
    def test_get_cached_logo_path_hit(self, mock_redis: MagicMock) -> None:
        """Test récupération depuis cache (hit)"""
        mock_client = MagicMock()
        mock_client.ping.return_value = True
        mock_client.get.return_value = "/tmp/test-logo.svg"
        mock_redis.Redis.return_value = mock_client

        cache = CacheManager(enabled=True)
        with patch("pathlib.Path.exists", return_value=True):
            result = cache.get_cached_logo_path(
                generator_type="ultimate",
                variant="serenity",
                size=200,
            )
            assert result is not None
            assert isinstance(result, Path)

    @patch("src.cache_manager.redis")
    def test_get_cached_logo_path_miss(self, mock_redis: MagicMock) -> None:
        """Test récupération depuis cache (miss)"""
        mock_client = MagicMock()
        mock_client.ping.return_value = True
        mock_client.get.return_value = None
        mock_redis.Redis.return_value = mock_client

        cache = CacheManager(enabled=True)
        result = cache.get_cached_logo_path(
            generator_type="ultimate",
            variant="serenity",
            size=200,
        )
        assert result is None

    @patch("src.cache_manager.redis")
    def test_cache_logo_path(self, mock_redis: MagicMock) -> None:
        """Test mise en cache d'un logo"""
        mock_client = MagicMock()
        mock_client.ping.return_value = True
        mock_client.setex.return_value = True
        mock_redis.Redis.return_value = mock_client

        cache = CacheManager(enabled=True)
        logo_path = Path("/tmp/test-logo.svg")
        result = cache.cache_logo_path(
            logo_path=logo_path,
            generator_type="ultimate",
            variant="serenity",
            size=200,
        )
        assert result is True
        mock_client.setex.assert_called_once()

    def test_cache_logo_path_disabled(self) -> None:
        """Test mise en cache avec cache désactivé"""
        cache = CacheManager(enabled=False)
        logo_path = Path("/tmp/test-logo.svg")
        result = cache.cache_logo_path(
            logo_path=logo_path,
            generator_type="ultimate",
            variant="serenity",
            size=200,
        )
        assert result is False

    @patch("src.cache_manager.redis")
    def test_invalidate_cache(self, mock_redis: MagicMock) -> None:
        """Test invalidation du cache"""
        mock_client = MagicMock()
        mock_client.ping.return_value = True
        mock_client.keys.return_value = ["arkalia:logo:key1", "arkalia:logo:key2"]
        mock_client.get.return_value = "/tmp/test.svg"
        mock_client.delete.return_value = 2
        mock_redis.Redis.return_value = mock_client

        cache = CacheManager(enabled=True)
        with patch("pathlib.Path.exists", return_value=True):
            result = cache.invalidate_cache()
            assert result == 2

    @patch("src.cache_manager.redis")
    def test_get_cache_stats(self, mock_redis: MagicMock) -> None:
        """Test récupération des statistiques du cache"""
        mock_client = MagicMock()
        mock_client.ping.return_value = True
        mock_client.keys.return_value = ["arkalia:logo:key1", "arkalia:logo:key2"]
        mock_connection_pool = MagicMock()
        mock_connection_pool.connection_kwargs = {"host": "localhost", "port": 6379}
        mock_client.connection_pool = mock_connection_pool
        mock_redis.Redis.return_value = mock_client

        cache = CacheManager(enabled=True)
        stats = cache.get_cache_stats()
        assert stats["enabled"] is True
        assert stats["connected"] is True
        assert stats["keys_count"] == 2

    def test_get_cache_stats_disabled(self) -> None:
        """Test statistiques avec cache désactivé"""
        cache = CacheManager(enabled=False)
        stats = cache.get_cache_stats()
        assert stats["enabled"] is False
        assert stats["connected"] is False
        assert stats["keys_count"] == 0
