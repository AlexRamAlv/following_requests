"""
    In this file it's been declered the function to create an instance of the Flask class
    using the configuration avialable in the setting python file.
    the function recived a string as a configuration name passing to the dict imported
    the function also return a Flask instance.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from setting import config
from flask_login import LoginManager

# Initializing variables to use later in the create app function
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()

login_manager.login_view = "main.show_requesters"

# create function
def create_app(config_name : str) -> Flask:
    app =Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app