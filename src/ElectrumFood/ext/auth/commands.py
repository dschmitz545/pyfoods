import click
from ElectrumFood.ext.auth.models import User
from ElectrumFood.ext.db import db


def list_user():
    users = User.query.all()
    click.echo(f"lista de usuários: {users}")


@click.option("--email_usu", "-e")
@click.option("--passwd_usu", "-p")
@click.option("--admin_usu", "-a", is_flag=True, default=False)
@click.option("--name_usu", "-n")
def add_user(email_usu, passwd_usu, admin_usu, name_usu):
    """Adiciona um novo usuário"""
    user = User(
        email=email_usu,
        passwd=passwd_usu,
        admin=admin_usu,
        nome=name_usu
    )
    db.session.add(user)
    db.session.commit()

    click.echo("Usuário criado no banco de dados")
