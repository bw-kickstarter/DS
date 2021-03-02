"""SQLAlchemy Database"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

DB = SQLAlchemy()


class User(UserMixin, DB.Model):
    """User information"""
    id = DB.Column(DB.Integer, primary_key=True)
    password = DB.Column(DB.String(50))
    email = DB.Column(DB.String, unique=True)

    def __repr__(self):
        return "< User: '{}' >".format(self.id)


class Kickstarter(DB.Model):
    """Kickstarter project information"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    owner = DB.Column(DB.)
    # TODO based on models

    def __repr__(self):
        return "< Kickstarter: '{}' >".format(self.name)

