"""Authentication system"""

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import LM, DB

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["POST","GET"])
def login():
    if current_user.is_authenticated:
        return render_template("home.html")

    email = request.values["email"]
    password = request.values["password"]
    # remember = True if request.values["remember"] else False

    if request.method == "POST":
        credential = User.query.filter_by(email = email).first()

        if credential and (credential.password == password):
            login_user(credential)
            return render_template("home.html")

        flash("Incorrect email or password! Try again or register.")
        return render_template("login.html")
    
    return render_template("login.html")


@auth.route("/register", methods=["POST","GET"])
def register():
    email = request.values["email"]
    password = request.values["password"]

    if request.method == "POST":
        credential = User.query.filter_by(email = email).first()

        if credential is None:
            new_credential = User(email=email, password=password)

            DB.session.add(new_credential)
            DB.session.commit()

            login_user(new_credential)

            return render_template("home.html")
        
        flash("Email already in use! Try again or login.")

    return render_template("register.html")


@LM.user_loader
def load_user(user_id):
    """Checks if user authorized"""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@LM.unauthorized_handler
def unauthorized():
    """Redirects unauthorized users"""
    flash("You must be logged in to view that page.")
    return render_template("login.html")
