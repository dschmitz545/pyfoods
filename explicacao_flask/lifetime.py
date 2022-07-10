# applicantion app out of context
# Contexto

from distutils.log import debug
from flask import Flask
app = Flask(__name__)

## 1 Configuração
    app.config["Foo"] = "bar"
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DB_URI"] = "mysql://.."
 
    ### Registrar Rotas
    @app.route("/path")
    def funcao():
        ...
    app.add_url_rule("/path", callable) #pode ser funcao, classe, qualquer coisa..

    ### Inicializar extensoes
    from flask_admin import Admin
    Admin.init_app(app)

    ### Registrar Blueprints
    app.register_blueprints(...)

    ### add hooks
    @app.before_request(...)
    @app.error_handle(...)

    ### Chamar outras factories
    views.init_app(app)

## 2 App Context

    ### App está pronto, esperando wsgi chamar ele

    ### Testar
    app.test_client
    debug
    objetos globais do Flask
        (importar request, session, g)
        - Hooks

    from flask import current_app, g
    
## 3 Request Context
    ### usar os globais do flask
    from flask import request, session, g

    request.args
    request.form