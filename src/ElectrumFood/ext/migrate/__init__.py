from flask_migrate import Migrate
from ElectrumFood.ext.db import db
from ElectrumFood.ext.db import models #noqa

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)