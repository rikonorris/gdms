# Individual settings. Configure it on project start up.
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_ID = 1
SITE_URL = ''
SECRET_KEY = 'qus+h6pl%n76&_1m=_&(p7l81fsdf#lasdfasdfaw35434qfaw080ig='  # chenge the secret key for your local system.

# Debug mode options
DEBUG = True

# SECURITY WARNING: don't run with debug turned on in production!
if (DEBUG):
    ALLOWED_HOSTS = ['127.0.0.1', '192.168.86.1']
    INTERNAL_IPS = ['192.168.86.1', '127.0.0.1']
else:
    ALLOWED_HOSTS = ['*']
    INTERNAL_IPS = ['*']

# MariaDB definations:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ised',  # Database name
        'USER': 'root',  # User name
        'PASSWORD': 'root',  # User password
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}

# Static folder definations:
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR)
STATICFILES_DIRS = [os.path.join(STATIC_ROOT, 'static'), ]

# DON'T redifine fixtures path, please. it is important for fixtures upload.
FIXTURE_DIRS = [os.path.join(BASE_DIR, 'development/dumps')]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': STATIC_ROOT + STATIC_URL + 'django_cache',
    }
}

# Please, change the admin name and email for your own. This is used for error-log sending
ADMINS = (
    ('Test Test', 'test@gmail.com'),
)
MANAGERS = ADMINS

# Please, choose propriate email backend for your own goals. For develop and testing use console email backend only.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # CONSOLE MODE - for development purposes.
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  #SMTP - for production server.

# SMTP settings
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'test@test.org'
EMAIL_HOST_PASSWORD = 'fxse_df06'
DEFAULT_FROM_EMAIL = 'Test instant <test@test.org>'
DEFAULT_TO_EMAIL = 'test@test.org'
TIMEOUT = 1