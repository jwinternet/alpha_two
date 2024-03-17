#!/usr/bin/python3.12

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alpha_two.settings')

application = get_asgi_application()
