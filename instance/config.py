"""
Contains configurations for the applications
"""

class Config(object):
    """The base configurations class"""
    @staticmethod
    def init_app(app):
        """This initializes the app instance"""
        pass

    SECRET_KEY = "youwillneverknow"

class DevelopmentConfig(Config):
    """Development configurations"""
    DEBUG = True
    DATABASE_URL = "dbname=api host=127.0.0.1 port=5432 user=postgres password=wilson"

class ProductionConfig(Config):
    """Production configurations"""
    DEBUG = False

CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
