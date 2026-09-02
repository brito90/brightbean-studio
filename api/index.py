"""
Vercel Python Handler for BrightBean Studio

This module provides the WSGI/ASGI handler required by Vercel's
@vercel/python runtime for Django applications.
"""

import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

# Import Django and get WSGI application
from django.core.wsgi import get_wsgi_application

# This is the handler Vercel expects
app = get_wsgi_application()
