"""
    Declaring the functions which are gonna managin the errors that might be happend
    Those handler will be call in any part of the application
    this is why app_errorhandler is called, in order to not declared the same code in other blueprint
"""

from app.main import main
from flask import render_template

#When an error server occurs
@main.app_errorhandler(500)
def error_server(error):
    return render_template("err/500.html"), 500

#When a page can be found
@main.app_errorhandler(404)
def not_found(error):
    return render_template("err/404.html"), 404