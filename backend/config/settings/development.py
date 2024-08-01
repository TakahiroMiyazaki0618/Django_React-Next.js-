from .base import *
import os

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': os.getenv('MYSQL_DB'),
    'USER': os.getenv('MYSQL_USER'),
    'PASSWORD': os.getenv('MYSQL_PASSWORD'),
    'HOST': os.getenv('MYSQL_HOST'),
    'PORT': os.getenv('MYSQL_PORT'),
    'ATOMIC_REQUESTS': True,
  }
}
