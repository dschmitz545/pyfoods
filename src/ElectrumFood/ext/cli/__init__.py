import click
from jinja2 import clear_caches
from ElectrumFood.ext.db import db
from ElectrumFood.ext.db import models

def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        db.create_all()
    
    @app.cli.command()
    @click.option("--email1", "-e")
    @click.option("--passwd1", "-p")
    @click.option("--admin1", "-a", is_flag=True, default=False)
    @click.option("--name1", "-n")
    def add_user(email1, passwd1, admin1, name1):
        """Adiciona um novo usuário"""
        user = models.User(
            email=email1,
            passwd=passwd1,
            admin=admin1,
            nome=name1
        )
        db.session.add(user)
        db.session.commit()

        click.echo("Usuário criado no banco de dados")

    @app.cli.command()
    def listar_pedidos():
        click.echo("lista de pedidos")

    @app.cli.command()
    def listar_usuarios():
        users = models.User.query.all()
        click.echo(f"lista de usuários: {users}")