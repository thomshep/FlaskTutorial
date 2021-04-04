#importo la variable db que esta en este modulo, esta definido en __init__.py
from . import db
#me ayuda al trabajar con usuarios
from flask_login import UserMixin
from sqlalchemy.sql import func

#defino los campos que tendra la base de datos
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#defino los campos que tendra la base de datos
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    #es como una lista con todas las notas que tenga el usuario