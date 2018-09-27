"""
Contains configurations for the applications
"""

class Config(object):
    """The base configurations class"""
    @staticmethod
    def init_app(app):
        """This initializes the app instance"""
        pass

class DevelopmentConfig(Config):
    """Development configurations"""
    DEBUG = True
    DATABASE_URL = ("dbname=api username=postgres password=wilson host=127.0.0.1 port=5000")

class ProductionConfig(Config):
    """Production configurations"""
    DEBUG = False

CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
