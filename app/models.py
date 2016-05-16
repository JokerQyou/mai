# -*- coding: utf-8 -*-
from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User {} (id:{})>'.format(self.username, self.id)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role {} (id:{})>'.format(self.name, self.id)
