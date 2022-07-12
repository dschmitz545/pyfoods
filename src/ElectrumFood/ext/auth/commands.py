import click
from ElectrumFood.ext.auth.models import User
from ElectrumFood.ext.db import db


def list_user():
    users = User.query.all()
    click.echo(f"lista de usuários: {users}")


@click.option("--email1", "-e")
@click.option("--passwd1", "-p")
@click.option("--admin1", "-a", is_flag=True, default=False)
@click.option("--name1", "-n")
def add_user(email1, passwd1, admin1, name1):
    """Adiciona um novo usuário"""
    user = User(
        email=email1,
        passwd=passwd1,
        admin=admin1,
        nome=name1
    )
    db.session.add(user)
    db.session.commit()

    click.echo("Usuário criado no banco de dados")
