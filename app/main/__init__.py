"""
    Creating the main blueprint
    it servers the views and errors when needed
"""

from flask import Blueprint

# creating the instance of a blueprint which name is main
main = Blueprint("main", __name__)

# this are the views and error views the blueprint will be controlling
from app.main import views, errors