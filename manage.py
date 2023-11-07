#!/usr/bin/env python
import django
from decouple import config
from django.conf import settings
from django.core.management import execute_from_command_line
from django.conf import global_settings


def init_django():
    if settings.configured:
        return

    db_name = config('DB_NAME')
    db_user = config('DB_USER')
    db_password = config('DB_PASSWORD')
    db_host = config('DB_HOST')
    db_port = config('DB_PORT')

    settings.configure(
        global_settings,
        INSTALLED_APPS=[
            'db',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': db_name,
                'USER': db_user,
                'PASSWORD': db_password,
                'HOST': db_host,
                'PORT': db_port,
            }
        }
    )
    django.setup()


if __name__ == "__main__":
    init_django()
    execute_from_command_line()
