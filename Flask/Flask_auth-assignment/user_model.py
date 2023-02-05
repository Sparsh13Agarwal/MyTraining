import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# for jwt we could use expire -> ["JWT_ACCESS_TOKEN_EXPIRE"] = False
# 
db = SQLAlchemy(app)
app.app_context().push()
Migrate(app,db)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password
