from app.auth import auth
from app.models import Administrator
from app.auth.forms import LoginForm
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        admin = Administrator.query.filter_by(username=form.username.data).first()
        if admin is not None and admin.validate_password(form.password.data):
            login_user(admin)
            next = request.args.get("next")
            if next is None or next.startswith("/"):
                next = url_for("main.show_requesters")
            return redirect(next)
        flash("Credenciales no coniciden!")

    return render_template("auth/login.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    flash("Has cerrado sesion")
    return redirect(url_for("main.show_requesters"))