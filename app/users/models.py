import datetime
import enum

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, admin
from app.users.admin import UserAdmin


class UserRoleEnum(enum.Enum):
    """
    User roles.
    """

    guest = "guest"
    admin = "admin"
    manager = "manager"


class User(db.Model, UserMixin):
    """User model."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), default=True)
    password_hash = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username, email, password, *args, **kwargs):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        """Return the user's id as a string."""
        return str(self.id)

    def is_admin(self):
        """Check if the user has the admin role."""
        return self.role == UserRoleEnum.admin

    def is_manager(self):
        """Check if the user has the manager role."""
        return self.role == UserRoleEnum.manager

    def __repr__(self):
        """Represent this User as a string."""
        return self.email


admin.add_view(UserAdmin(User, db.session))
