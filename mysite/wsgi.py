"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
import os
import sys

#  Add your Django project directory to the sys.path
path = '/home/Mklein51/mklein51.pythonanywhere.com/djangogirls01'
if path not in sys.path:
    sys.path.append(path)

#  Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

#  Get the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
