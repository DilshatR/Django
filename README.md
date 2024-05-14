# Django
DjangoDocker

- docker compose run --rm web sh -c "django-admin startproject service ."
- docker compose run --rm web sh -c "python manage.py migrate"
- docker compose run --rm web sh -c "python manage.py createsuperuser"
