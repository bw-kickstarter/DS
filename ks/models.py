"""SQLAlchemy Database"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from . import DB


class User(UserMixin, DB.Model):
    """User information"""
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    email = DB.Column(DB.String, unique=True)
    password = DB.Column(DB.String)

    def __repr__(self):
        return "< User: '{}' >".format(self.email)


class Kickstarter(DB.Model):
    """Table for Kickstarter projects"""
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    user_email = DB.Column(DB.String)
    category = DB.Column(DB.String)
    blurb = DB.Column(DB.String)
    country = DB.Column(DB.String)
    goal = DB.Column(DB.BigInteger)
    location = DB.Column(DB.String)
    name = DB.Column(DB.String)
    state = DB.Column(DB.String)
    usd_type = DB.Column(DB.String)
    days_allotted = DB.Column(DB.Integer)
    days_before_launch = DB.Column(DB.Integer)

    def __repr__(self):
        return "< Kickstarter: '{}' >".format(self.name)
