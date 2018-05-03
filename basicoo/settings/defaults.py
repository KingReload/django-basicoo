import os

import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))

location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

# Setup the database from env

env = environ.Env()
env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '@hj9v)+nz&*rw49mk#zopa4saqotku+&dv#$-&kt225y7fqi#7'

PROJECT_NAME = env.list('APP_NAME')[0]

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True  # True for dev version

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'colorfield',

    '%s.apps.core' % env.list('APP_NAME')[0],
    '%s.apps' % env.list('APP_NAME')[0],
    '%s' % env.list('APP_NAME')[0],
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'querycount.middleware.QueryCountMiddleware',
]

ROOT_URLCONF = '%s.urls' % env.list('APP_NAME')[0]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            location('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'builtins': [
                '%s.templatetags.userdata_tags' % env.list('APP_NAME')[0],
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '%s.wsgi.application' % env.list('APP_NAME')[0]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': env.db(
        default='postgresql://localhost/%s' % (
            env.list('APP_NAME')[0])),
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    '%s.backends.EmailBackend' % env.list('APP_NAME')[0],
    'django.contrib.auth.backends.ModelBackend',
)

# Django querycoount

QUERYCOUNT = {
    'THRESHOLDS': {
        'MEDIUM': 50,
        'HIGH': 200,
        'MIN_TIME_TO_LOG': 0,
        'MIN_QUERY_COUNT_TO_LOG': 0
    },
    'IGNORE_REQUEST_PATTERNS': [],
    'IGNORE_SQL_PATTERNS': [],
    'DISPLAY_DUPLICATES': None,
    'RESPONSE_HEADER': 'X-DjangoQueryCount-Count'
}

STYLING_FILE = os.path.join(BASE_DIR, 'templates/stylingform.txt')
LOG_FILE = os.path.join(BASE_DIR, 'templates/partials/logs.html')

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'public/staticfiles'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')
MEDIA_URL = '/media/'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'core:home'

# Mail part of the website

EMAIL_SUBJECT_PREFIX = env.str('EMAIL_SUBJECT_PREFIX', default=[])
DEFAULT_FROM_EMAIL = env.str('DEFAULT_FROM_EMAIL', default=[])
SERVER_EMAIL = env.str('SERVER_EMAIL', default=[])

EMAIL_HOST = env.str('EMAIL_HOST', default=[])
EMAIL_PORT = env.str('EMAIL_PORT', default=[])
EMAIL_HOST_USER = env.str('SERVER_EMAIL', default=[])
EMAIL_HOST_PASSWORD = env.str('HOST_PASSWORD', default=[])
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
