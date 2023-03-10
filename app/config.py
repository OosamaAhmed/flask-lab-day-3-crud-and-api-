

import os


class Config:

    SECRET_KEY = os.urandom(32) #for secret key

    @staticmethod
    def init_app():

        pass



class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"


class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"
    # postgresql database
    SQLALCHEMY_DATABASE_URI = "postgresql://itiflask:123456@localhost:5432/flask"


projectConfig = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
