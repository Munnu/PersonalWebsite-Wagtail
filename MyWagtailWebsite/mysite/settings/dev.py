from __future__ import absolute_import, unicode_literals

from .base import *
from . import secrets

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
use_local_email_script = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY

ALLOWED_HOSTS = ['f94d7569.ngrok.io', 'localhost', '127.0.0.1']

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

if use_local_email_script == True:
    # for testing purposes, use shell script for localhost smtp
    DEFAULT_FROM_EMAIL = 'testing@example.com'
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False
else:
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

try:
    from .local import *
except ImportError:
    pass
