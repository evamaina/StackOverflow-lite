import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    

class DevelopmentConfig(Config):
    """ Development Configurations."""
    DEBUG = True

class TestingConfig(Config):
    """Testing Configurations ."""
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    """ Staging Configurations"""
    DEBUG = True

class ProductionConfig(Config):
    """ Production Configurations."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}



