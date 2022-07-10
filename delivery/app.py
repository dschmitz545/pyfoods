from flask import Flask
# from views import index, sobre # se importar aqui, erro circular import
app = Flask(__name__)

from views import index, sobre # se importar aqui, vai funcionar, mas não é recomendado segundo pep 8