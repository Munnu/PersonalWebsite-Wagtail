from __future__ import absolute_import, unicode_literals

from .base import *
from . import secrets

DEBUG = False

ALLOWED_HOSTS = ['165.227.63.130', 'moniqueblake.me', '.moniqueblake.me']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#EMAIL_HOST = secrets.Gmail_Email_Info().EMAIL_HOST
#EMAIL_HOST_PASSWORD = secrets.Gmail_Email_Info().EMAIL_HOST_PASSWORD
#EMAIL_HOST_USER = secrets.Gmail_Email_Info().EMAIL_HOST_USER
#EMAIL_PORT = secrets.Gmail_Email_Info().EMAIL_PORT
#EMAIL_USE_TLS = secrets.Gmail_Email_Info().EMAIL_USE_TLS
## DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_HOST = secrets.Email_Info().EMAIL_HOST
EMAIL_HOST_PASSWORD = secrets.Email_Info().EMAIL_HOST_PASSWORD
EMAIL_HOST_USER = secrets.Email_Info().EMAIL_HOST_USER
EMAIL_PORT = secrets.Email_Info().EMAIL_PORT
EMAIL_USE_TLS = secrets.Email_Info().EMAIL_USE_TLS
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Google Recaptcha Data
RECAPTCHA_PUBLIC_KEY = secrets.RECAPTCHA_PUBLIC_KEY
RECAPTCHA_PRIVATE_KEY = secrets.RECAPTCHA_PRIVATE_KEY
NOCAPTCHA = True
RECAPTCHA_USE_SSL = False
SECURE_SSL_REDIRECT = False


# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_OFFLINE = False
COMPRESS_ENABLED = False

COMPRESS_CSS_FILTERS = [
        'compressor.filters.css_default.CssAbsoluteFilter',
            'compressor.filters.cssmin.CSSMinFilter',
            ]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


try:
    from .local import *
except ImportError:
    pass
