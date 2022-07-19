from pyfoods.ext.auth import models # noqa
from pyfoods.ext.auth.commands import list_user, add_user

from pyfoods.ext.db import db
from pyfoods.ext.auth.admin import UserAdmin
from pyfoods.ext.admin import admin as admin
from pyfoods.ext.auth.models import User


def init_app(app):
    """TODO: inicializar Flask simple login + JWT"""
    app.cli.command()(list_user)
    app.cli.command()(add_user)

    admin.add_view(UserAdmin(User, db.session))
