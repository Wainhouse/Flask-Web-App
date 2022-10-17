from . import db 
from flask_login import UserMixin
from sqlalchemy import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.foreignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.column(db.String(150), unique=True)
    password = db.column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship('Note')