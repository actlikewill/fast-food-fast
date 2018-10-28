"""
Contains configurations for the applications
"""
import os

class Config(object):
    """The base configurations class"""
    @staticmethod
    def init_app(app):
        """This initializes the app instance"""
        pass

    SECRET_KEY = "youwillneverknowandiwontshow"

class DevelopmentConfig(Config):
    """Development configurations"""
    DATABASE_URL = "dbname=dev_fastfoodfast host=127.0.0.1 port=5432 user=postgres password=wilson"
    DEBUG = False

class ProductionConfig(Config):
    """Production configurations"""
    # DATABASE_URL = os.environ['DATABASE_URL']
    DEBUG = False

class TestingConfig(Config):
    DATABASE_URL = "dbname=test_fastfoodfast host=127.0.0.1 port=5432 user=postgres password=wilson"

CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    'testing': TestingConfig
}
