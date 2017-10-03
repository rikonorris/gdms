'''
Main system congif-file.
PLEASE, be careful when make some changes with it.
For your local purposes redifine or add new directives into settings_local.py and don't forget
add the same changes into settings_local_sample.py.
'''

from .settings_local import *  # local config file

# Global system definitions:
ROOT_URLCONF = 'system.urls'
WSGI_APPLICATION = 'system.wsgi.application'

# Application definition:
INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'easy_thumbnails',
    'filer',
    'mptt',



    'guardian',
    'viewflow',
    'system',
    'todo',
    'django_activeurl',
    'stronghold',
    'haystack',
    'pure_pagination',
    'employees',
    'debug_toolbar',
    'documents',
    'report_builder',
    'filemanager'
]

HAYSTACK_CONNECTIONS = {
  'default': {
    'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
    'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
  },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

MIDDLEWARE = [
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'stronghold.middleware.LoginRequiredMiddleware',
    'django.middleware.common.CommonMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
            ],
        },
    },
]

TIME_ZONE = 'Europe/Kiev'
LANGUAGE_CODE = 'uk_UA'
DEFAULT_CHARSET = 'utf8'
USE_I18N = True
DATETIME_FORMAT = 'M. d, Y H:i'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'modules/viewflow/locale'),
)

# Custom user-model
AUTH_USER_MODEL = "employees.User"

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



REPORT_BUILDER_GLOBAL_EXPORT = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'allauth.account.auth_backends.AuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
)

# Static folder definitions:
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

ASSETS_ROOT = os.path.join(BASE_DIR, 'assets')
ASSETS_URL = '/assets/'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, os.path.join(MEDIA_ROOT, 'django_cache')),
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Pagination settings
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 1,
    'MARGIN_PAGES_DISPLAYED': 2,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}


STRONGHOLD_DEFAULTS = True
STRONGHOLD_PUBLIC_URLS = (
    r'^/accounts/login/$',
    r'^/accounts/password_reset/$',
    r'^/accounts/password_reset/done/$',
    r'^/accounts/reset/done/$',
    r'^/accounts/signup/',

)
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': "auto",
        'extraAllowedContent': 'iframe[*]',
    },
}

CKEDITOR_UPLOAD_PATH = "ckeditor/uploads/"

LOGIN_REDIRECT_URL = '/'


#To-Do Module Settings

TODO_STAFF_ONLY = True

# If you use the "public" ticket filing option, to whom should these tickets be assigned?
# Must be a valid username in your system. If unset, unassigned tickets go to "Anyone."
#TODO_DEFAULT_ASSIGNEE = 'johndoe'

# If you use the "public" ticket filing option, to which list should these tickets be saved?
# Defaults to first list found, which is probably not what you want!
TODO_DEFAULT_LIST_ID = 1

# If you use the "public" ticket filing option, to which *named URL* should the user be
# redirected after submitting? (since they can' see the rest of the ticket system).
# Defaults to "/"
#TODO_PUBLIC_SUBMIT_REDIRECT = 'dashboard'


#REPORT BUILDER SETTINGS

REPORT_BUILDER_INCLUDE = ['documents.InstructionProcess'] # Allow only the model user to be accessed
REPORT_BUILDER_FRONTEND = True
