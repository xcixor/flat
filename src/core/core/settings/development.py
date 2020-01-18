"""Module contains development configurations for the app."""
from .base import *

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')
MEDIA_URL= "/media/"