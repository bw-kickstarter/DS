"""Routing file for Kickstarter Success App"""

from flask import Flask, render_template, request, redirect, Blueprint, url_for
from flask_login import LoginManager , login_required, current_user, logout_user
from .models import Kickstarter
from . import DB
# from .predict import predict

main = Blueprint('main', __name__)

@main.route("/")
def root():
    """Renders login page"""
    return render_template("login.html")
    # render_template("home.html")
    # render_template("signup.html")

@main.route("/home", methods=["POST", "GET"])
@login_required
def home():
    """Reads inputs and redirects"""
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
    # loct = request.values["location_type"]

    if request.method == "POST":
        db_entry = Kickstarter(user_email=ue, category=cat, blurb=bl, country=cy, goal=gl, location=loc, name=name, state=st, usd_type=ut, days_alloted=da, days_before_launch=db4l) #, location_type=loct)

        DB.session.add(db_entry)
        DB.session.commit()

        # add_message = "Kickstarter project '{}' validated".format(name)

        # outcome = predict(db_entry)

        # predict_message = "'{}' Kickstarter model is more likley to {}".format(request.values["name"], "SUCCEED" if outcome else "FAIL")

        # except Exception as e:
        #     message = "Error adding '{}': {}".format(name, e)

        #     db_entry = []

        # TODO this HAS to be added:
                # if outcome:
                #     return render_template("success.html")

                # else return render_template("failure.html")
        return render_template("success.html", ks_name=name) 


@main.route("/success")
@login_required
def success():
    """Success endpoint"""
    return render_template("success.html", ks_name="name") 
                                            # name static for testing


@main.route("/failure")
@login_required
def failure():
    """Failure endpoint"""
    return render_template("failure.html", ks_name="name")
                                            # name static for testing


@main.route("/reset")
# @login_required
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
