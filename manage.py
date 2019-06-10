from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_session import Session
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis

app = Flask(__name__)

class Config():
    DEBUG = True

#     配置数据库信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/website"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    SESSION_REDIS = StrictRedis(host = REDIS_HOST,port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400


app.config.from_object(Config)

db = SQLAlchemy(app)
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
CSRFProtect(app)
Session(app)

manager = Manager(app)

Migrate(app,db)
manager.add_command('db',MigrateCommand)


@app.route("/")
def index():
    return "ok"

if __name__ == "__main__":
    manager.run()
