import wtforms as wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField

# __import__("ipdb").set_trace()


class UserForm(FlaskForm):
    email = wtf.StringField(
        "Email", [wtf.validators.DataRequired(), wtf.validators.Email()]
    )

    # __import__("ipdb").set_trace()

    password = wtf.PasswordField(
        "Senha", [wtf.validators.DataRequired()])
    foto = FileField("Foto")
    nome = wtf.StringField("Nome", [wtf.validators.DataRequired()])
