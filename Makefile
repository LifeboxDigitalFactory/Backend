.PHONY: help install migrate seed runserver test

help:
	@echo "install    Install dependencies"
	@echo "migrate    Apply migrations"
	@echo "seed       Seed demo users"
	@echo "runserver  Start Django server"
	@echo "test       Run tests"

install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

seed:
	python seeder.py

runserver:
	python manage.py runserver

test:
	python manage.py test
