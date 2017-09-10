from __future__ import absolute_import, unicode_literals

from .base import *
from . import secrets

DEBUG = False

ALLOWED_HOSTS = ['f94d7569.ngrok.io', 'localhost', '127.0.0.1']  # change this later to reflect production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = secrets.Gmail_Email_Info().EMAIL_HOST
EMAIL_HOST_PASSWORD = secrets.Gmail_Email_Info().EMAIL_HOST_PASSWORD
EMAIL_HOST_USER = secrets.Gmail_Email_Info().EMAIL_HOST_USER
EMAIL_PORT = secrets.Gmail_Email_Info().EMAIL_PORT
EMAIL_USE_TLS = secrets.Gmail_Email_Info().EMAIL_USE_TLS
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Google Recaptcha Data
RECAPTCHA_PUBLIC_KEY = secrets.RECAPTCHA_PUBLIC_KEY
RECAPTCHA_PRIVATE_KEY = secrets.RECAPTCHA_PRIVATE_KEY
NOCAPTCHA = False
RECAPTCHA_USE_SSL = False
SECURE_SSL_REDIRECT = False


# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_OFFLINE = True
COMPRESS_ENABLED = True

COMPRESS_CSS_FILTERS = [
        'compressor.filters.css_default.CssAbsoluteFilter',
            'compressor.filters.cssmin.CSSMinFilter',
            ]


try:
    from .local import *
except ImportError:
    pass
