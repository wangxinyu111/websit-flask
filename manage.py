from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_session import Session
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from config import *



manager = Manager(app)

Migrate(app,db)
manager.add_command('db',MigrateCommand)


@app.route("/")
def index():
    return "ok"

if __name__ == "__main__":
    manager.run()
