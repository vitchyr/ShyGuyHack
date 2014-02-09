"""
WSGI config for shyguy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shyguy.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# To get static files to work on Heroku. See https://devcenter.heroku.com/articles/django-assets
from dj_static import Cling

application = Cling(get_wsgi_application())`
