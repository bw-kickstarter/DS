# from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from .models import DB #, User


def create_app():
    """Create Flask Application"""
    app = Flask(__name__)

    # app.config['SECRET_KEY'] = "needsecretkey"
                              # getenv("SECRET_KEY")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3" 
                                           # getenv("DATABASE_URI")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)

    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

APP = create_app()
