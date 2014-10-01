"""
Django settings for dash_test_runner project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*z(s8sb^&p-6n#b!w=1-d2bho*+*0g_51bnx=-@a$wj6dnpd2w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_nose',

    'guardian',
    'smartmin',
    'smartmin.users',

    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'djcelery',

    #dash
    'dash.orgs',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'smartmin.users.middleware.ChangePasswordMiddleware',
    'smartmin.middleware.TimezoneMiddleware',
    'dash.orgs.middleware.SetOrgMiddleware',
)

import warnings
warnings.filterwarnings('error', r"DateTimeField received a naive datetime", RuntimeWarning, r'django\.db\.models\.fields')

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)



ROOT_URLCONF = 'dash_test_runner.urls'

WSGI_APPLICATION = 'dash_test_runner.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'


# Available languages for translation
LANGUAGES = (('en', "English"), ('fr', "French"))
DEFAULT_LANGUAGE = "en"


TIME_ZONE = 'UTC'
USER_TIME_ZONE = 'Africa/Kigali'


USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)

# create the smartmin CRUDL permissions on all objects
PERMISSIONS = {
    '*': ('create', # can create an object
          'read',   # can read an object, viewing it's details
          'update', # can update an object
          'delete', # can delete an object,
          'list'),  # can view a list of the objects
    'auth.user': ('profile','forget', 'recover', 'expired', 'failed', 'newpassword', 'mimic'),
    'orgs.org': ('choose', 'home', 'edit', 'manage_accounts', 'create_login', 'join'),
}

# assigns the permissions that each group should have, here creating an Administrator group with
# authority to create and change users
GROUP_PERMISSIONS = {
    "Administrators": (
        'users.user_profile',
        'orgs.org_home',
        'orgs.org_edit',
        'orgs.org_manage_accounts',
        'orgs.orgbackground.*',

    ),
    "Editors": (
        'users.user_profile',
        'orgs.org_home',
    ),
    "Viewers": [],
}

ANONYMOUS_USER_ID = -1
LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = "/"

#-----------------------------------------------------------------------------------
# Django-Nose config
#-----------------------------------------------------------------------------------

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

#-----------------------------------------------------------------------------------
# Async tasks with django-celery
#-----------------------------------------------------------------------------------
import djcelery
djcelery.setup_loader()

CELERY_RESULT_BACKEND = 'database'

BROKER_BACKEND = 'redis'
BROKER_HOST = 'localhost'
BROKER_PORT = 6379
BROKER_VHOST = '4'

# RapidPRO
API_ENDPOINT = 'http://localhost:8001'
SITE_HOST_PATTERN = 'http://%s.localhost:8000'
SITE_CHOOSER_TEMPLATE = 'public/org_chooser.html'

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:1',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}
if 'test' in sys.argv:
    CACHES['default'] = {'BACKEND': 'django.core.cache.backends.dummy.DummyCache',}


ORG_CONFIG_FIELDS =[ dict(name='shortcode', field=dict(help_text=_("The shortcode that users will use to contact U-report locally"), required=True)),
                     dict(name='join_text', field=dict(help_text=_("The short text used to direct visitors to join U-report"), required=False)),
                     dict(name='join_fg_color', field=dict(help_text=_("The color used to draw the text on the join bar"), required=False), superuser_only=True),
                     dict(name='join_bg_color', field=dict(help_text=_("The color used to draw the background on the join bar"), required=False), superuser_only=True),
                     dict(name='primary_color', field=dict(help_text=_("The primary color for styling for this organization"), required=False), superuser_only=True),
                     dict(name='secondary_color', field=dict(help_text=_("The secondary color for styling for this organization"), required=False), superuser_only=True),
                     dict(name='bg_color', field=dict(help_text=_("The background color for the site"), required=False), superuser_only=True),
                     dict(name='colors', field=dict(help_text=_("Up to 6 colors for styling charts, use comma between colors"), required=False), superuser_only=True),
                     dict(name='google_tracking_id', field=dict(help_text=_("The Google Analytics Tracking ID for this organization"), required=False)),
                     dict(name='youtube_channel_url', field=dict(help_text=_("The URL to the Youtube channel for this organization"), required=False)),
                     dict(name='facebook_page_url', field=dict(help_text=_("The URL to the Facebook page for this organization"), required=False)),
                     dict(name='twitter_handle', field=dict(help_text=_("The Twitter handle for this organization"), required=False)),
                     dict(name='twitter_user_widget', field=dict(help_text=_("The Twitter widget used for following new users"), required=False)),
                     dict(name='twitter_search_widget', field=dict(help_text=_("The Twitter widget used for searching"), required=False)),
                     dict(name='reporter_group', field=dict(help_text=_("The name of txbhe Contact Group that contains registered reporters")), superuser_only=True),
                     dict(name='born_label', field=dict(help_text=_("The label of the Contact Field that contains the birth date of reporters")), superuser_only=True),
                     dict(name='gender_label', field=dict(help_text=_("The label of the Contact Field that contains the gender of reporters")), superuser_only=True),
                     dict(name='occupation_label', field=dict(help_text=_("The label of the Contact Field that contains the occupation of reporters")), superuser_only=True),
                     dict(name='registration_label', field=dict(help_text=_("The label of the Contact Field that contains the registration date of reporters")), superuser_only=True),
                     dict(name='state_label', field=dict(help_text=_("The label of the Contact Field that contains the State of reporters")), superuser_only=True),
                     dict(name='district_label', field=dict(help_text=_("The label of the Contact Field that contains the District of reporters")), superuser_only=True),
                     dict(name='male_label', field=dict(help_text=_("The label assigned to U-reporters that are Male.")), superuser_only=True),
                     dict(name='female_label', field=dict(help_text=_("The label assigned to U-reporters that are Female.")), superuser_only=True)]
#                     dict(name='featured_state', field=dict(help_text=_("Choose the featured State of reporters shown on the home page")))]

#-----------------------------------------------------------------------------------
# Directory Configuration
#-----------------------------------------------------------------------------------
import os

PROJECT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))
RESOURCES_DIR = os.path.join(PROJECT_DIR, '../resources')

LOCALE_PATHS = (os.path.join(PROJECT_DIR, '../locale'),)
RESOURCES_DIR = os.path.join(PROJECT_DIR, '../resources')
FIXTURE_DIRS = (os.path.join(PROJECT_DIR, '../fixtures'),)
TESTFILES_DIR = os.path.join(PROJECT_DIR, '../testfiles')
TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, '../templates'),)
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, '../static'), os.path.join(PROJECT_DIR, '../media'), )
STATIC_ROOT = os.path.join(PROJECT_DIR, '../sitestatic')
MEDIA_ROOT = os.path.join(PROJECT_DIR, '../media')
MEDIA_URL = "/media/"