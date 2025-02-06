"""
ASGI config for the_backend_prj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_backend_prj.settings')

application = ProtocolTypeRouter (
    {
        "http": get_asgi_application(),
        # únicamente HTTP por ahora... (Luego podremos agregar otros protocolos).
    }
)
