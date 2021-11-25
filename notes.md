## How to install Django
`pip install django`

## Start new Django project
`django-admin startproject project_name` (creates new directory. Put space at end to place in current directory)

## Run server
`python3 manage.py runserver`

## File structure

- manage.py - not meant to be altered with
- db.sqlite3 - database file
- main_folder
  - init.py - add in special features when django launches for the first time
  - asgi.py/wsgi.py - for deployment
  - settings.py
    - DEBUG = TRUE, offers additional info when errors found. Set to false when deploy
    - INSTALLED_APPS, different pieces of code we can introduce in the app
  - urls.py - Starting point for any django project
  
## Add a new app
`python3 manage.py startapp appname`
- Add app to main folder settings.py INSTALLED_APPS 

## URLS
- add app urls in urls.py file. Reference functions in views.py file in the app folder

## Templates
- Create templates/appname folder in app.
- Place html templates there
- reference template in views.py using render function

