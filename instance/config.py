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

class ProductionConfig(Config):
    """Production configurations"""
    DEBUG = False

CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
