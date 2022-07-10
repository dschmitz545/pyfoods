# code-show-python
# treinamento sobre python e flash

# wsgi = servidor já embutido no python
# gunicorn = servidor de aplicação para python

# python3 -m venv .venv
# source .venv/bin/activate
# pip install gunicorn
# pip install --upgrade pip
# gunicorn wsgi:application
# pip install -r requirements.txt
# export FLASK_ENV=development
# unset FLASK_ENV
# não é uma boa pratia, fazer pip freeze ou pip list para preencher o requirements.txt
# factorys, funções ou classes que podem ser invocadas no futuro, melhor jeito de trabalhar com flask
# conveções: chamar de create_app a factory principal, chamar de init_app a factory de cada uma das extenções separadamente
# nunca usar import app em outros arquivos, no máximo o import create_app, a não ser em casos especificos de teste.