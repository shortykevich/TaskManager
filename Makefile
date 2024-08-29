install:
	poetry install

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

build-locales:
	poetry run django-admin makemessages -l ru

compile-locales:
	poetry run django-admin compilemessages

convert-static:
	poetry run python manage.py collectstatic --no-input

tests-coverage:
	poetry run coverage run -m pytest

coverage-report:
	poetry run coverage report -m

