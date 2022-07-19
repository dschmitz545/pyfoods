from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from pyfoods.ext.auth.models import User
from pyfoods.ext.db import db
from flask import flash


def format_user(self, request, user, *args):
    return user.email.split("@")[0]


class UserAdmin(ModelView):
    """Interface admin de user"""
    # column_formatters = {"email": format_user}
    column_list = ["email", "admin", "nome"] # Exibindo apenas algumas colunas

    column_searchable_list = ["email", "nome"]
    column_filters = ["email", "admin"]

    can_create = True  # limitando ações no admin
    can_edit = False    # limitando ações no admin
    can_delete = True  # limitando ações no admin


    @action(
        'toggle_admin',
        'Togle admin status',
        'Are you sure?'
    )
    def toogle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f"{len(users)} usuários alterados com sucesso", "success")
