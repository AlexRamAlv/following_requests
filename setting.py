"""
    Here are declare all the settings of the app.
        1. Database configurations.
        2. Develop config
        3. Prod config
        4. Also default config that is develop
"""
import os 
# file' path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#main class configuration
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "a hard key to crack or guess"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

# Develop configuration
class DevMode(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_DEV") or "sqlite:///" + os.path.join(BASE_DIR, "sqliteDev.sqlite")

# Production Configuration
class ProdMode(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE") or "sqlite:///" + os.path.join(BASE_DIR, "sqliteProd.sqlite")


# dictionary for selecting the confinguration desired
config = {
    "dev": DevMode,
    "prod": ProdMode,

    "default": DevMode
}