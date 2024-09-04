install:
	poetry install --no-interaction --no-root

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

build-locales:
	poetry run python manage.py makemessages -l ru

compile-locales:
	poetry run python manage.py compilemessages

convert-static:
	poetry run python manage.py collectstatic --no-input

tests-coverage:
	poetry run coverage run -m pytest

coverage-report:
	poetry run coverage report -m

format-coverage:
	poetry run coverage lcov -o lcov.info

lint:
	poetry run flake8 task_manager
