from .base import *
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'CONN_MAX_AGE': 60,
        'NAME': '${database}',
        'USER': '${database_username}',
        'PASSWORD': '${database_password}',
        'HOST': '${database_host}',
        'PORT': '5432',
    }
}
