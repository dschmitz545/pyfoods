python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
export FLASK_ENV=development
export FLASK_APP=ElectrumFood/app.py
flask run