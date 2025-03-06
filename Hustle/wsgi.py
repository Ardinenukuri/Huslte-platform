import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hustle.settings')

application = get_wsgi_application()

# Configure WhiteNoise for media files regardless of environment
application = WhiteNoise(application)
application.add_files('media/', prefix='media/')