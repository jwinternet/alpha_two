#!/usr/bin/python3.12

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alpha_two.settings")

application = get_wsgi_application()
