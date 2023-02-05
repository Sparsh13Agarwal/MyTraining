# Day 12

# flask_sqlalchemy
#flask-migrate
# flask ORM

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)
app.app_context().push()
Migrate(app,db)

class Pet(db.Model):
    __tablename__='pets'
    id = db.Column(db.Integer,primary_key=True)
    # breed = db.Column(db.Text)
    name = db.Column(db.Text)
    toys = db.relationship('Toy',backref='Pet',lazy='dynamic')
    owner= db.relationship('Owner',backref='Pet',uselist =False)

    def __init__(self,name) -> None:
        self.name = name

    def __repr__(self) -> str:
        if self.owner:
            return f"Pet's name is{self.name} and owner is {self.owner.name}."
        else:
            return f"Pet's name is {self.name} and no owner is assigned yet."
    def report_toy(self):
        print("there are many toys")
        for toy in self.toys:
            print(toy.item_name)

class Owner(db.Model):
    __tablename__='owners'
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    pet_id = db.Column(db.Integer,db.ForeignKey('pets.id'))
    def __init__(self,name,pet_id):
        self.name = name
        self.pet_id=pet_id
    
class Toy(db.Model):
    __tablename__='toys'
    id = db.Column(db.Integer,primary_key=True)
    item_name=db.Column(db.Text)
    pet_id=db.Column(db.Integer,db.ForeignKey('pets.id'))

    def __init__(self,item_name,pet_id):
        self.item_name=item_name
        self.pet_id=pet_id










