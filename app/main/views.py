from app.main import main
from flask import render_template
from app.models import Requester

@main.route("/")
def show_requesters():
    requesters = Requester.query.all()
    return render_template("requesters/index.html", requesters = requesters)