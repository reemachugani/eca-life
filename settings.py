# Django settings for ecalife project.

import os.path
from django.conf.urls.defaults import patterns


DIRNAME = os.path.abspath(os.path.dirname(__file__))

SITE_URL = 'http://localhost:8000'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('eCALife', 'ntu.ecalife@hotmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'data.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


TIME_ZONE = 'Asia/Singapore'

LANGUAGE_CODE = 'en'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')

MEDIA_ROOT = os.path.join(DIRNAME, 'static/')

MEDIA_URL = '/static/'

STATIC_ROOT = ''


STATIC_URL = ''


ADMIN_MEDIA_PREFIX = '/static/admin/'


STATICFILES_DIRS = (
    STATIC_ROOT,
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


SECRET_KEY = 'sb&asm+-sm#*#$p9+n8=hi@wyi#z3_!va6_hk$ie7zk6@hhf63'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.Loader',
)

AVATAR_ALLOWED_FILE_EXTS = ('.jpg', '.png')
AVATAR_MAX_SIZE = 1024 * 1024
AVATAR_MAX_AVATARS_PER_USER = 20
AVATAR_STORAGE_DIR = MEDIA_ROOT + 'images'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ecalife.urls'

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'club',
    'profiles',
    'registration',
    'announcement',
    'event',
    'utils',
    'forum',
	'messages',
    'avatar',
    'search',
    'django_filters',
    )


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

TEMPLATE_CONTEXT_PROCESSOR = (
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.csrf',
    'messages.context_processors.inbox',
    'club.custom_context_processors.my_club_list',

    )

CSRF_FAILURE_VIEW = 'ecalife.custom.csrf.views.csrf_rejected'

SITE_HOST = '127.0.0.1:8000'
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.live.com"
EMAIL_HOST_USER = 'ntu.ecalife@hotmail.com'
EMAIL_HOST_PASSWORD = '"admin"'
DEFAULT_FROM_EMAIL = "NTU e-CA life <ntu.ecalife@hotmail.com>"
EMAIL_PORT = 587


# To setup the debugging server
# Use command: python -m smtpd -n -c DebuggingServer localhost:1025

LOGIN_REDIRECT_URL = '/homepage/'
LOGIN_URL = '/accounts/login/'

ACCOUNT_ACTIVATION_DAYS = 2

AUTH_PROFILE_MODULE = 'profiles.StudentProfile'

# uses cookiesessions app which is a session backend which uses Django's secure cookie encoding and
# decoding functionality to store the whole session in the cookie, instead of
# talking to some database or cache instance.

#SESSION_ENGINE = 'cookiesessions.engine'

#CACHE_BACKEND = 'newcache://127.0.0.1:11211/?binary=true'
