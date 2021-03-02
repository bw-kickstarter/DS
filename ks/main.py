"""Routing file for Kickstarter Success"""

# from os import getenv
from flask import Flask, render_template, request, Blueprint
from flask_login import LoginManager, login_required, current_user

main = Blueprint('main', __name__)

@main.route("/")
def root():
    return render_template("index.html", title="Home")

@main.route("/ks/", methods = ["POST"])
@main.route("/ks/<name>", methods = ["GET"])
@login_required
def user(name=None, message=""):
    name = name or request.values["ks_name"]

    try:
        if request.method == "POST":
            add_project(name)
            message = "Kickstarter project '{}' successfully added!".format(name)

        # TODO "ks_veredict = ???" 

    except Exception as e:
        message = "Error adding '{}': {}".format(name, e)

    return render_template("ks_project.html", title="Kickstarter Project Predictions") #TODO ", results=??? )"
