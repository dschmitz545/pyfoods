import os
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from pyfoods.ext.auth.models import User
from pyfoods.ext.db import db
from flask import current_app as app

ALGO = "pbkdf2:sha256"


def create_user(nome: str, email: str, password: str,
                admin: bool = False) -> User:
    user = User(
        email=email,
        passwd=generate_password_hash(password, ALGO),
        admin=admin,
        nome=nome,
    )

    # TODO: Tratar user exist exceptions
    db.session.commit()
    return user


def save_user_foto(filename, filestorage):
    """Saves user foto in 
    ./uploads/foo/folder.ext
    """
    filename = os.path.join(
        app.config["UPLOAD_FOLDER"],secure_filename(filename))
    filestorage.save(filename)
