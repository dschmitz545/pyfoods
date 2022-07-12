from ElectrumFood.ext.auth import models # noqa
from ElectrumFood.ext.auth.commands import list_user, add_user

from ElectrumFood.ext.db import db
from ElectrumFood.ext.auth.admin import UserAdmin
from ElectrumFood.ext.admin import admin as admin
from ElectrumFood.ext.auth.models import User


def init_app(app):
    """TODO: inicializar Flask simple login + JWT"""
    app.cli.command()(list_user)
    app.cli.command()(add_user)

    admin.add_view(UserAdmin(User, db.session))
