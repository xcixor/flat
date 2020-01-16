"""Module contains development configurations for the app."""
from .base import *

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')