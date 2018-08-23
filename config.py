
import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    
class DevelopmentConfig(Config):
    """setting environment variables for the database."""
    SECRET_KEY ="thisismeevet"
    os.environ['DATABASE'] = 'stackoverflow'
    os.environ['USER'] = 'stack'
    os.environ['PASSWORD'] = 'stack123'
    os.environ['HOST'] = 'localhost'
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing."""
    # os.environ['DATABASE'] = 'test-stackoverflow'
    # os.environ['USER'] = 'stack'
    # os.environ['PASSWORD'] = 'stack123'
    # os.environ['HOST'] = 'localhost'
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}

