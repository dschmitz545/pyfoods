import click
from jinja2 import clear_caches
from ElectrumFood.ext.db import db
from ElectrumFood.ext.site import models

def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        db.create_all()
    
    @app.cli.command()
    @click.option("--email1", "-e")
    @click.option("--passwd1", "-p")
    @click.option("--admin1", "-a", is_flag=True, default=False)
    def add_user(email1, passwd1, admin1):
        """Adiciona um novo usuário"""
        user = models.User(
            email=email1,
            passwd=passwd1,
            admin=admin1
        )
        db.session.add(user)
        db.session.commit()

        click.echo("Usuário criado no banco de dados")

    @app.cli.command()
    def listar_pedidos():
        click.echo("lista de pedidos")

    @app.cli.command()
    def listar_usuarios():
        click.echo("lista de usuários")