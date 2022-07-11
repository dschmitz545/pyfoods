python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
export FLASK_ENV=development
export FLASK_APP=ElectrumFood/app.py
flask run

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