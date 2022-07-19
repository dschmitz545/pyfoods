from flask_migrate import Migrate
from pyfoods.ext.db import db
from pyfoods.ext.db import models  # noqa

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
