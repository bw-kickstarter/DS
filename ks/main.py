"""Routing file for Kickstarter Success App"""

# from os import getenv
from flask import Flask, render_template, request, Blueprint, redirect, url_for
from flask_login import LoginManager, login_required, current_user
from .models import Kickstarter, DB
from .predict import predict

main = Blueprint('main', __name__)

@main.route("/")
def root():
    """Directs you to signin"""
    return redirect(url_for('auth.login')) 
    # render_template("signup.html", title="Register")

@main.route("/home", methods = ["POST"])
@login_required
def predict_outcome():
    """Reads inputs from forms and returns prediction.html or error"""
    ue = request.values["user_email"]
    cat = request.values["category"]
    bl = request.values["blurb"]
    cy = request.values["country"]
    gl = request.values["goal"]
    loc = request.values["location"]
    name = request.values["name"]
    st = request.values["state"]
    ut = request.values["usd_type"]
    da = request.values["days_allocated"]
    db4l = request.values["days_before_launch"]
    loct = request.values["location_type"]

    try:
        db_entry = DB.Kickstarter(user_name=ue, category=cat, blurb=bl, country=cy, goal=gl, location=loc, name=name, state=st, usd_type=ut, days_allocated=da, days_before_launch=db4l, colation_type=loct)

        DB.session.add(db_entry)
        DB.session.commit()

        add_message = "Kickstarter project '{}' validated".format(name)

        outcome = predict(db_entry)

        predict_message = "'{}' Kickstarter model is more likley to {}".format(request.values["name"], "SUCCEED" if outcome else "FAIL")

    except Exception as e:
        message = "Error adding '{}': {}".format(name, e)

    return render_template("prediction.html", title="Prediction",
        message1=add_message, message2=predict_message)


@main.route("/reset")
@login_required
def reset():
    """Reset database"""
    DB.drop_all()
    DB.create_all()
    return render_template("home.html")