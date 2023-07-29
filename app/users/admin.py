from flask_admin.contrib.sqla import ModelView

from app import db, admin
from app.users.models import User


class UserAdmin(ModelView):
    column_list = ["id", "username", "email", "created_at"]


admin.add_view(UserAdmin(User, db.session))
