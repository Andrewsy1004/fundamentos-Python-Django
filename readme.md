
## Entornos Virtuales
1. python -m venv venv 
2. .\venv\Scripts\activate 
3. pip install django                                                    
4. pip freeze > requirements.txt

## Django
1. django-admin startproject config . 
2. python manage.py startapp ("nombre de la app")
3. python manage.py runserver

## ORM (Objeto Relacional Mapper) Django
1. python manage.py makemigrations "nombre de la app"    ( migraciones de la app )
2. python manage.py migrate

## Django Admin
1. python manage.py createsuperuser