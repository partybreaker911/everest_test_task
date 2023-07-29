import random
import logging
from string import ascii_lowercase

import requests
from celery.result import AsyncResult
from flask import render_template, redirect, url_for, request, flash, session

from . import users_blueprint
from app import db
from app.users.controller import (
    create_user,
    authenticate_user,
    get_user_by_username,
    get_user_by_email,
)
from app.users.forms import RegistrationForm


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
            return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)
