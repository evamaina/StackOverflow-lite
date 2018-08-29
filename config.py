
import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    
class DevelopmentConfig(Config):
    """setting environment variables for the database."""
    SECRET_KEY ="thisismeevet"
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing."""
    TESTING = True
    DEBUG = True
    SECRET_KEY ="thisismeevet"

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}

