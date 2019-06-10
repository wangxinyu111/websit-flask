from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Config():
    DEBUG = True

#     配置数据库信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/website"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route("/")
def index():
    return "ok"

if __name__ == "__main__":
    app.run()
