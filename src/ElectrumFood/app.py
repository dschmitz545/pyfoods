from flask import Flask
from ElectrumFood.ext import config
from ElectrumFood.ext import site
from ElectrumFood.ext import toolbar
from ElectrumFood.ext import db
from ElectrumFood.ext import cli
from ElectrumFood.ext import migrate


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
