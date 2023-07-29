from celery.result import AsyncResult
from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_user

from app import db
from . import users_blueprint
from app.users.models import User
from app.users.forms import RegistrationForm, LoginForm


@users_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        if User.query.filter_by(username=username).first():
            flash("Username already exists", "error")
        elif User.query.filter_by(email=email).first():
            flash("Email already exists", "error")
        else:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            flash("Registration successful. Please log in.", "success")
            return redirect(url_for("users.login"))

    return render_template("users/register.html", form=form)


@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    """View for user login."""
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user is not None and user.check_password(password):
            login_user(user)
            return redirect(url_for("products.list_of_products"))
        else:
            flash("Неправильные учетные данные. Пожалуйста, повторите попытку.")

    return render_template("users/login.html", form=form)


@users_blueprint.route("/logout")
def logout():
    session.clear()

    return redirect(url_for("products.list_of_products"))
