"""
Django settings for ddprobe_mall project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
DB_SETTING_PATH = '/root/project/Django_project/ddprobe_mall/utils/databaseSettings.json'
DB_NAME, DB_USER, DB_SECRET ='', '', ''

with open(DB_SETTING_PATH) as json_file:
    dbSetting = json.load(json_file)['databaseSetting']
    DB_NAME = dbSetting['databaseName']
    DB_USER = dbSetting['User']
    DB_SECRET = dbSetting['Secret']
    

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.meiduo.site', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users',
    # include the corsheaders to allow the frontend to access backend using cors
    'corsheaders',
]

# https://github.com/adamchainz/django-cors-headers#setup
# CorsMiddleware should be placed as high as possible,
# especially before any middleware that can generate responses such as
# Django's CommonMiddleware or Whitenoise's WhiteNoiseMiddleware. 
# If it is not before, it will not be able to add the CORS headers to these responses.
MIDDLEWARE = [
    # Set the middleware of our CORS
    'corsheaders.middleware.CorsMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ddprobe_mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ddprobe_mall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST' : 'localhost',
        'PORT' : 3306,
        'USER' : DB_USER,
        'PASSWORD' : DB_SECRET,
        'NAME': DB_NAME,
    }
}

# Cache
# Use Django-redis to include redis into the project
# https://github.com/jazzband/django-redis
CACHES = {
    # Reserve
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # Used to save the session data
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Use django-redis as backend for session storage
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging set up
# Extracted from https://docs.djangoproject.com/en/4.0/topics/logging/ final complex setup


###########LOGGING##############
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {     # The format of our logs
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        # 'special': {
        #     '()': 'project.logging.SpecialFilter',
        #     'foo': 'bar',
        # },
        'require_debug_true': {     # only output the log under debug mode for Django
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {        # Write the logs into the console
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {       # Write the logs into specific file
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/mall.log'),
            'maxBytes': 100 * 1024 * 1024,      # set the max size to 300 MB
            'backupCount': 10,      # at most contains 10 files
            'formatter': 'verbose'
        }
        # 'mail_admins': {        # mail the error to the admin's email
        #     'level': 'ERROR',
        #     'class': 'django.utils.log.AdminEmailHandler',
        #     'filters': ['special']
        # }
    },
    'loggers': {
        'django': {     # logger name
            'handlers': ['console', 'file'],    # are allowed to send log to console and file
            'propagate': True,
            'level': 'INFO'
        }
        # 'django.request': {
        #     'handlers': ['mail_admins'],
        #     'level': 'ERROR',
        #     'propagate': False,
        # },
        # 'myproject.custom': {
        #     'handlers': ['console', 'mail_admins'],
        #     'level': 'INFO',
        #     'filters': ['special']
        # }
    }
}



########################################
# Django allows you to override the default user model by providing a value for 
# the AUTH_USER_MODEL setting that references a custom model:
# This dotted pair describes the label of the Django app (which must be in your INSTALLED_APPS),
# and the name of the Django model that you wish to use as your user model.
AUTH_USER_MODEL = 'users.User'


#####CORS#######################

# CORS  ?????????
# This is used to allow the frontend to access the backend
# https://github.com/adamchainz/django-cors-headers#configuration
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8080',
    'http://localhost:8080',
    'http://www.meiduo.site:8080',
    'http://www.meiduo.site:8000'
)
CORS_ALLOW_CREDENTIALS = True  # ????????????cookie