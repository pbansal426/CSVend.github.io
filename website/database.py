from main import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_number = db.Column(db.String(6), unique=True)
    password = db.Column(db.String(150))
    points = db.Column(db.Integer)

class Food(db.Model):
    name=db.Column(db.Integer, unique=True)
    points = db.Column(db.Integer)