from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

DB = SQLAlchemy()
LM = LoginManager()


def create_app():
    """Create Flask Application"""
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "needsecretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    LM.login_view = 'auth.login'

    DB.init_app(app)
    LM.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


APP = create_app()
