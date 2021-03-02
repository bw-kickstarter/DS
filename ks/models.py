"""SQLAlchemy Database"""

from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin

DB = SQLAlchemy()


# class User(UserMixin, DB.Model):
#     """User information"""
#     id = DB.Column(DB.Integer, primary_key=True)
#     password = DB.Column(DB.String(50))
#     email = DB.Column(DB.String, unique=True)

#     def __repr__(self):
#         return "< User: '{}' >".format(self.email)


class Kickstarter(DB.Model):
    """Kickstarter project information"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    user_email = DB.Column(DB.String(100))

    category = DB.Column(DB.String(50))
    blurb = DB.Column(DB.String(1000))
    country = DB.Column(DB.String(3))
    goal = DB.Column(DB.BigInteger)
    location = DB.Column(DB.String(100))
    name = DB.Column(DB.String(100))
    state = DB.Column(DB.String)
    usd_type = DB.Column(DB.String)
    days_alloted = DB.Column(DB.Integer)
    days_before_launch = DB.Column(DB.Integer)
    location_type = DB.Column(DB.String(20))

    def __repr__(self):
        return "< Kickstarter: '{}' >".format(self.name)
