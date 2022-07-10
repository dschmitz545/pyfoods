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