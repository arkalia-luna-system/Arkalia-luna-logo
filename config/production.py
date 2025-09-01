"""
Configuration Production pour Arkalia-LUNA Logo Generator
Optimisations pour environnement de production
"""

import os
from pathlib import Path
from typing import Union, Type

# Configuration de base
class ProductionConfig:
    """Configuration optimisée pour la production"""
    
    # Performance
    CACHE_SIZE = 1000  # Cache plus grand en production
    CACHE_TTL = 3600   # 1 heure de cache
    MAX_WORKERS = 8    # Nombre de workers parallèles
    
    # Optimisations SVG
    SVG_COMPRESSION = True
    SVG_MINIFICATION = True
    SVG_OPTIMIZATION_LEVEL = 3  # 0-3, 3 = max
    
    # Cache Redis (optionnel)
    REDIS_ENABLED = os.getenv('REDIS_ENABLED', 'false').lower() == 'true'
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
    REDIS_DB = int(os.getenv('REDIS_DB', 0))
    
    # Monitoring
    ENABLE_METRICS = True
    METRICS_INTERVAL = 60  # secondes
    LOG_LEVEL = 'INFO'
    
    # Sécurité
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS = ['.svg', '.png', '.jpg', '.jpeg']
    RATE_LIMIT = 100  # requêtes par minute par IP
    
    # Paths
    EXPORT_DIR = Path('exports/production')
    CACHE_DIR = Path('cache/production')
    LOG_DIR = Path('logs/production')
    
    @classmethod
    def get_cache_config(cls):
        """Configuration du cache"""
        return {
            'size': cls.CACHE_SIZE,
            'ttl': cls.CACHE_TTL,
            'redis_enabled': cls.REDIS_ENABLED,
            'redis_host': cls.REDIS_HOST,
            'redis_port': cls.REDIS_PORT,
            'redis_db': cls.REDIS_DB
        }
    
    @classmethod
    def get_svg_config(cls):
        """Configuration SVG"""
        return {
            'compression': cls.SVG_COMPRESSION,
            'minification': cls.SVG_MINIFICATION,
            'optimization_level': cls.SVG_OPTIMIZATION_LEVEL
        }
    
    @classmethod
    def get_monitoring_config(cls):
        """Configuration monitoring"""
        return {
            'enabled': cls.ENABLE_METRICS,
            'interval': cls.METRICS_INTERVAL,
            'log_level': cls.LOG_LEVEL
        }

# Configuration spécifique par environnement
class DevelopmentConfig(ProductionConfig):
    """Configuration développement"""
    CACHE_SIZE = 100
    CACHE_TTL = 300
    MAX_WORKERS = 2
    LOG_LEVEL = 'DEBUG'
    ENABLE_METRICS = False

class StagingConfig(ProductionConfig):
    """Configuration staging"""
    CACHE_SIZE = 500
    CACHE_TTL = 1800
    MAX_WORKERS = 4
    LOG_LEVEL = 'INFO'

# Factory de configuration
def get_config(environment: Union[str, None] = None) -> Type[ProductionConfig]:
    """Retourne la configuration selon l'environnement"""
    if not environment:
        environment = os.getenv('ENVIRONMENT', 'production')
    
    configs = {
        'development': DevelopmentConfig,
        'staging': StagingConfig,
        'production': ProductionConfig
    }
    
    return configs.get(environment, ProductionConfig)

# Configuration par défaut
config = get_config()
