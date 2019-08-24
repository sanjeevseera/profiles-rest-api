# Profiles Rest API
Profiles Rest API source code.

## start django project
django-admin.py startproject profile_project .

## create django application
python manage.py startapp profiles_api

## Enable app in Django settings file
profile_project > settings.py >
INSTALLED_APPS [
  'rest-framework',
  'rest_framework.authtoken',
  'profiles_api',]

## run server
python manage.py runserver
