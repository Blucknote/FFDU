from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Text
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    files = db.relationship('File', backref='uploader', lazy='dynamic')


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(64), unique=True)
    path = db.Column(db.String(256), unique=True)
    size = db.Column(db.Integer)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="files")
