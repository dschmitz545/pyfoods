import click
from ElectrumFood.ext.auth.models import User
from ElectrumFood.ext.auth.controller import create_user

# TODO: mover para controller
def list_user():
    users = User.query.all()
    click.echo(f"lista de usuários: {users}")


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
@click.option("--nome", "-n")
#def add_user(email_usu, passwd_usu, admin_usu, name_usu):
def add_user(email, passwd, admin, nome):
    """Adiciona um novo usuário"""
    # TODO: Tratar user exist exceptions
    create_user(
        email=email,
        password=passwd,
        admin=admin,
        nome=nome
        )

    click.echo("Usuário criado no banco de dados")
