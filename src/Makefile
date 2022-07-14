clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf .pytest_cache
	pip install -e .[dev] --upgrade --no-cache

install:
	pip install --upgrade pip
	pip install -e .['dev']

init_db:
	FLASK_APP=ElectrumFood/app.py flask create-db
	FLASK_APP=ElectrumFood/app.py flask db upgrade

test:
	FLASK_ENV=test pytest tests/ -v --cov=ElectrumFood

format:
	isort **/*.py
	black -l 79 **/*.py

run_dev:
	FLASK_APP=ElectrumFood/app.py FLASK_ENV=development flask run

run:
	FLASK_APP=ElectrumFood/app.py FLASK_ENV=production flask run
