"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

from __future__ import absolute_import, unicode_literals

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling
#from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.dev")

#application = get_wsgi_application()
#application = Cling(get_wsgi_application())
application = Cling(MediaCling(get_wsgi_application()))
