from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['tinny.pythonanywhere.com']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'tinny$default',
       'USER' : 'tinny', 
       'PASSWORD' : 'philip1234',
       
       'HOST' : '127.0.0.1',
   },
}