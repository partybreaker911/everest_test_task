import random
import logging
from string import ascii_lowercase

import requests
from celery.result import AsyncResult
from flask import render_template, redirect, url_for, request, flash, session

from . import users_blueprint
from app import csrf, db
from app.users.controller import (
    create_user,
    authenticate_user,
    get_user_by_username,
    get_user_by_email,
)


@users_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if get_user_by_username(username):
            flash("Username already exists", "error")
        elif get_user_by_email(email):
            flash("Email already exists", "error")
        else:
            create_user(username, email, password)
            flash("Registration successful. Please log in.", "success")
            return redirect(url_for("auth.login"))

    return render_template("register.html")
