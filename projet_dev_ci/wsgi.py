"""
WSGI config for projet_dev_ci project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

path = "/var/www/html/epsi/current"
if path not in sys.path:
	sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet_dev_ci.settings')

application = get_wsgi_application()
