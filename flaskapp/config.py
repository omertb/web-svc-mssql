# default config
import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ['FSECRETKEY']
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mssql+pymssql://{}@sqlexp/BikeStores".format(os.environ['MSCRED'])


class DevelopmentConfig(BaseConfig):
    SESSION_COOKIE_SECURE = False
    RECAPTCHA_USE_SSL = False
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    # session headers
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = True