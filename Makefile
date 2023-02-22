APP_LIST ?= main api 
.PHONY: collectstatic run test ci install install-dev migrations staticfiles

help:
	@echo "Available commands"
	@echo " - ci               : lints, migrations, tests, coverage"
	@echo " - install          : installs production requirements"
	@echo " - isort            : sorts all imports of the project"
	@echo " - lint             : lints the codebase"
	@echo " - runserver        : runs the development server"
	@echo " - shellplus        : runs the development shell"

collectstatic:
	python manage.py collectstatic --noinput

clean:
	rm -rf __pycache__ .pytest_cache

check:
	python manage.py check

check-deploy:
	python manage.py check --deploy

install:
	pip install -r requirements.txt

shellplus:
	python manage.py shell_plus

shell:
	python manage.py shell

showmigrations:
	python manage.py showmigrations

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

migrations-check:
	python manage.py makemigrations --check --dry-run

runserver:
	python manage.py runserver

build: install makemigrations migrate runserver

isort:
	isort . --check-only --profile black

format:
	black . --check 

lint: format
	flake8 .

test: migrations-check
	python -Wa manage.py test

ci: lint
	coverage run --source='.' manage.py test
	coverage html

superuser:
	python manage.py createsuperuser