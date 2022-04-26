#!/bin/bash

echo "Install dependencies"
pip install -r requirements.txt

echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

echo "Load mocked data to database"
python manage.py loaddata mock_data.yaml

echo "Load statics"
python manage.py collectstatic --noinput

echo "Starting server"
python manage.py runserver 0.0.0.0:8000
