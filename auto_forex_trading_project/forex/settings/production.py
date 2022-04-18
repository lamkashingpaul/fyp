from .base import *
from os import environ
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = f'Set the {setting} env variable'
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_setting('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS += ['lamkashingpaul.com']

WSGI_APPLICATION = 'forex.wsgi.application'

# correct the static url by adding the SCRIPT_NAME
STATIC_URL = 'forex/' + STATIC_URL