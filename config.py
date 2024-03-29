import logging
from redis import StrictRedis


class Config():
    SECRET_KEY = '1234'

#     配置数据库信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/website"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"

    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    SESSION_REDIS = StrictRedis(host = REDIS_HOST,port=REDIS_PORT)
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = 86400

    LOG_LEVEL = logging.DEBUG



class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = logging.WARNING



class TestingConfig(Config):
    DEBUG = True


# 定义配置字典
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}