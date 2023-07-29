from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for

from flask_login import current_user


class UserAdmin(ModelView):
    column_list = ["id", "username", "email", "created_at"]


class AuthenticatedModelView(ModelView):
    """ModelView with authentication required."""

    def is_accessible(self):
        return current_user.is_authenticated and (
            current_user.is_admin() or current_user.is_manager()
        )  # Предполагается, что у пользователя есть атрибут is_admin, который указывает на то, что он администратор

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("users.login"))
