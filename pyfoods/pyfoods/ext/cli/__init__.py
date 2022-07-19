import click
from pyfoods.ext.db import db


def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        db.create_all()

    @app.cli.command()
    def listar_pedidos():
        # TODO: usar tabulate e listar pedidos
        click.echo("lista de pedidos")
