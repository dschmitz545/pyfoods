python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
export FLASK_ENV=development
export FLASK_APP=ElectrumFood/app.py
flask run
flask create-db
flask run
flask add-user --email1="a@b.com" --passwd1="1234" --admin1
flask db init
flask db migrate -m "initial migrate"
flask db upgrade
flask db current
flask db history
flask db downgrade

## Sob demanda
pip list
pip freeze
pip uninstall @nomePacote
make install
make clean
black setup.py
flake8 setup.py
pytest tests/ -v
pytest tests/ --fixtures
pytest tests/