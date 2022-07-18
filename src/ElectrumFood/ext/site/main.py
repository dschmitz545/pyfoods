from flask import redirect, render_template, request
from flask import Blueprint
from ElectrumFood.ext.auth.form import UserForm
from ElectrumFood.ext.auth.controller import create_user, save_user_foto


bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/about")
def about():
    return(render_template("about.html"))


@bp.route("/restaurants")
def restautants():
    return(render_template("restaurants.html"))


@bp.route("/cadastro", methods=["GET", "POST"])
def signup():
    form = UserForm()
    if form.validate_on_submit():
        create_user(
            email=form.email.data,
            password=form.password.data,
            nome=form.nome.data
        )
        foto = request.files.get('foto')
        if foto:
            save_user_foto(
                foto.filename,
                foto
            )
        return redirect("/")

    # if request.method == "POST":
    #     __import__("ipdb").set_trace()

    return render_template("userform.html", form=form)


@bp.route("/admin")
def admin():
    ...
