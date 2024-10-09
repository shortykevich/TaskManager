## Tests and linter status:
![CI](https://github.com/shortykevich/python-project-52/actions/workflows/task_manager_ci.yml/badge.svg)
[![Actions Status](https://github.com/shortykevich/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/shortykevich/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/52323296be3f29fe2434/maintainability)](https://codeclimate.com/github/shortykevich/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/52323296be3f29fe2434/test_coverage)](https://codeclimate.com/github/shortykevich/python-project-52/test_coverage)


## Tech stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

## Description:
It is a task management system. Lite version of http://www.redmine.org.
It allows you to set tasks, change their statuses, mark with custom labels and assign executors.
Registration and authentication are required to work with the system.

## Installation:
```bash
git clone git@github.com:shortykevich/TaskManager.git && cd TaskManager
make install
```
#### Project heavily depends on environment variables, so it's suggested to create **.env** file
```bash
echo "SECRET_KEY=your_very_secrete_key" >> .env
# By default project use sqlite db. If you gonna use Postgres add:
echo "DATABASE_URL=postgres://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName" >> .env
# Optional:
echo "DEBUG=True" >> .env
```
#### You can create superuser with default command:
```bash
python manage.py createsuperuser
```
#### or create relevant variables in .env file
```bash
echo "DJANGO_SUPERUSER_USERNAME=YourUsername" >> .env
echo "DJANGO_SUPERUSER_PASSWORD=YourPassword" >> .env
echo "DJANGO_SUPERUSER_EMAIL=YourEmail" >> .env
```
#### then use custom command:
```bash
# Command was created for seamless deploying to avoid error if superuser already exists
python manage.py createsuperuser_if_not_exists
```
## Running:
```bash
python manage.py runserver
```
## [Demo](https://task-manager-ndp1.onrender.com/)
#### It may take a few minutes for demo project to start
