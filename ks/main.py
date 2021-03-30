"""Main routing for KS App"""

from flask import Flask, render_template, request, Blueprint, redirect, url_for, jsonify
from flask_login import LoginManager , login_required, current_user, logout_user
from .models import Kickstarter
from . import DB
import pandas as pd
from .predict import ks_model

main = Blueprint('main', __name__)


@main.route("/")
def root():
    """Redirects to home if authenticated, login otherwise"""
    # if current_user.is_authenticated:
    #     return redirect("/home")
    
    return redirect("/home")
    # return redirect("/login")


@main.route("/home", methods=["POST", "GET"])
# @login_required
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
        da = request.values["days_allotted"]
        db4l = request.values["days_before_launch"]

        db_entry = Kickstarter(user_email=ue, category=cat, blurb=bl,
                               country=cy, goal=gl, location=loc, name=name, state=st, usd_type=ut, days_allotted=da, days_before_launch=db4l)

        DB.session.add(db_entry)
        DB.session.commit()

        prediction = ks_model(category=cat, country=cy, goal=gl, location=loc, state=st, usd_type=ut, days_allotted=da, days_before_launch=db4l)
        #blurb=bl, name=name, 

        if (prediction == 1):

            message1 = "We are pleased to say that based on our analysis, Kickstarter '{}' will most likely succeed!".format(name)

            return render_template("success.html", message=message1)

        elif (prediction == 0):

            message0 = "We are sorry to say that based on our analysis, Kickstarter '{}' will most likely fail.".format(name)

            return render_template("failure.html", message=message0)

    return render_template("home.html")


@main.route("/success")
# @login_required
def success():
    """Success endpoint"""
    if not current_user.is_authenticated:
        return redirect("/login")

    return render_template("success.html")


@main.route("/failure")
# @login_required
def failure():
    """Failure endpoint"""
    if not current_user.is_authenticated:
        return redirect("/login")

    return render_template("failure.html")


@main.route("/reset")
# @login_required
def reset():
    """Reset database"""
    if not current_user.is_authenticated:
        return redirect("/login")

    DB.drop_all()
    DB.create_all()
    return render_template("login.html")


@main.route('/logout')
# @login_required
def logout():
    """Logout user"""
    if not current_user.is_authenticated:
        return redirect("/login")

    logout_user()
    return render_template("login.html")


@main.route("/team")
def team():
    """Team info"""    
    return render_template("team.html")


@main.route("/ks_api", methods=["POST","GET"])
def ks_api():
    """Reads json request, returns json message"""
    if request.method=='POST':

        posted_data = request.get_json()
        input = posted_data['data'] 

        prediction = ks_model(category=input['category'],
                              country=input['country'],
                              goal=input['goal'],
                              location=input['location'],
                              state=input['state'],
                              usd_type=input['usd_type'],
                              days_allotted=input['days_allotted'], days_before_launch=input['days_before_launch'])

        if prediction == 1:
            message = "Kickstarter campaign will succeed"

        elif prediction == 0:
            message = "Kickstarter campaign will fail"

        pass

    return jsonify(message)

# API call example:

# dat = { 'category':"some category",
#         'country':"Wakanda",
#         'goal':"42",
#         'location':"somewhere",
#         'state':"CA",
#         'usd_type':"domestic",
#         'days_allotted':"0",
#         'days_before_launch':"1" }

# req=request.post("https://bw-kickstarter-success.herokuapp.com/hapi",data=dat)