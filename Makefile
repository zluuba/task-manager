dev:
	poetry run python3 manage.py runserver

start:
	python3 manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

install:
	poetry install

lint:
	flake8 task_manager

test:
	poetry run python3 manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py
