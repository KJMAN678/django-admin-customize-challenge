#!/bin/sh
python manage.py migrate
python manage.py createsuperuser --noinput || true
python manage.py make_dummy_data
python manage.py runserver 0.0.0.0:8000
