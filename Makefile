install:
	poetry install

migrate:
	poetry run python manage.py migrate

build-locales:
	poetry run django-admin makemessages -l ru

compile-locales:
	poetry run django-admin compilemessages

convert-static:
	poetry run python manage.py collectstatic --no-input

