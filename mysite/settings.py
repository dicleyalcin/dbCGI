"""
Django settings for dbCGI project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import os.path 
import django.conf.global_settings as DEFAULT_SETTINGS

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = PACKAGE_ROOT

#TEMPLATE_DIRS =(os.path.join(os.path.dirname(__file__),'/Users/greengageplum/mysitetemplates').replace('\\','/'),)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('/Users/greengageplum/Envs/djangoenv/lib/python2.7/site-packages/django/contrib/admin/templates/')))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%!*lx0b^-dwtnqp)+m2kf_lp#l*+p_g2o8qsr)f98l-0s#ejup'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-93417601-1'
GOOGLE_ANALYTICS_DOMAIN = 'otulab.unl.edu'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'social.apps.django_app.default',
    'mysite',
    'django_nvd3',
    'rest_framework',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'website.context_processors.google_analytics',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PACKAGE_ROOT, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                
            ]
        },
    },
]


CELERY_IMPORTS = ('google_analytics.tasks')

WSGI_APPLICATION = 'mysite.wsgi.application'

SITE_ID = 1


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cgi', 
        'USER': 'root',
        'PASSWORD': 'Sng87!65@#oJ',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#dyalcin
#Sng87!65@#oj

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")
STATIC_ROOT = os.path.join("mysite/static")

#STATIC_ROOT = '/'
#URL prefix for static files.
#STATIC_URL = '/site_media/static/'

STATIC_URL = '/mysite/static/'

#STATICFILES_DIRS = [
#    os.path.join(PACKAGE_ROOT, "static"),
#]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',   
]

#BOWER_COMPONENTS_ROOT = '/PROJECT_ROOT/components/'

MEDIA_ROOT = os.path.join('Users/greengageplum/dbCGI/mysite', 'media')
MEDIA_URL = '/media/'
BOWER_PATH = '/usr/local/bin/bower'

BOWER_INSTALLED_APPS = (
    'jquery#1.9',
    'underscore',
)
