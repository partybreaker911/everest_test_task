from app import db
from app.users.models import User


def create_user(username, email, password):
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()


def authenticate_user(username, password):
    user = get_user_by_username(username)
    if user and user.check_password(password):
        return user
    return None


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()
