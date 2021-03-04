"""Main routing for KS App"""

from flask import Flask, render_template, request, Blueprint
from flask_login import LoginManager , login_required, current_user, logout_user
from .models import Kickstarter
from . import DB
import pandas as pd
from .predict import ks_model

main = Blueprint('main', __name__)

@main.route("/")
def root():
    """Renders login page"""
    return render_template("login.html")


@main.route("/home", methods=["POST", "GET"])
@login_required
def home():
    """Reads inputs, calls mmodel, returns prediction page"""
    if request.method == "POST":
        ue = request.values["user_email"]
        cat = request.values["category"]
        bl = request.values["blurb"]
        cy = request.values["country"]
        gl = request.values["goal"]
        loc = request.values["location"]
        name = request.values["name"]
        st = request.values["state"]
        ut = request.values["usd_type"]
        da = request.values["days_alloted"]
        db4l = request.values["days_before_launch"]

        db_entry = Kickstarter(user_email=ue, category=cat, blurb=bl,
                               country=cy, goal=gl, location=loc, name=name, state=st, usd_type=ut, days_alloted=da, days_before_launch=db4l)

        DB.session.add(db_entry)
        DB.session.commit()

        prediction = ks_model(blurb=bl, category=cat, country=cy, goal=gl, location=loc, name=name, state=st, usd_type=ut, days_allotted=da, days_before_launch=db4l)

        if prediction:
            return render_template("success.html", ks_name=name)

        return render_template("failure.html", ks_name=name)

    return render_template("home.html")


@main.route("/success")
@login_required
def success():
    """Success endpoint"""
    return render_template("success.html")


@main.route("/failure")
@login_required
def failure():
    """Failure endpoint"""
    return render_template("failure.html")


@main.route("/reset")
@login_required
def reset():
    """Reset database"""
    DB.drop_all()
    DB.create_all()
    return render_template("login.html")


@main.route('/logout')
@login_required
def logout():
    """Logout user"""
    logout_user()
    return render_template("login.html")
