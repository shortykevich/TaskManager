#!/usr/bin/env bash
# Exit on error
set -o errexit

make install

# Convert static asset files
make convert-static

make compile-locales

# Apply any outstanding database migrations
make migrate

# Adding superuser if you have relevant env variables
# Comment it if you don't need it
python manage.py createsuperuser_if_not_exists
