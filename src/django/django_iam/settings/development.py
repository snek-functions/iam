"""
Django development settings for esite project.
For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
This development settings are unsuitable for production, see
https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
"""

from .base import *  # noqa

# > Debug Switch
# SECURITY WARNING: don't run with debug turned on in production!
# See https://docs.djangoproject.com/en/stable/ref/settings/#debug
DEBUG = True

# > Application Definition
# A list of strings designating all applications that are enabled in this
# Django installation.
# See https://docs.djangoproject.com/en/stable/ref/settings/#installed-apps
INSTALLED_APPS += [
    # Django dev apps
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.conf.urls",
]

# > Secret Key
# SECURITY WARNING: keep the secret key used in production secret!
# See https://docs.djangoproject.com/en/stable/ref/settings/#secret-key
SECRET_KEY = "ct*z11t*ns876z)!f5f3h1byn7pp1ma5i!9*oo!=dmtmnrvzcn"

# > Allowed Hosts
# Accept all hostnames, since we don't know in advance.
# See https://docs.djangoproject.com/en/stable/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*",]

# > CORS Origin
# If True, the whitelist will not be used and all origins will be accepted.
# See https://pypi.org/project/django-cors-headers/
CORS_ORIGIN_ALLOW_ALL = True

# > Email Backend
# The backend to use for sending emails.
# See https://docs.djangoproject.com/en/stable/topics/email/#console-backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# > Set Base_Url
# Set the base url, needed to acces wagtail.
# See https://docs.wagtail.io/en/v0.8.10/howto/settings.html
BASE_URL = "http://localhost:8000"

# > Template Configuration
# A list containing the settings for all template engines to be used with
# Django.
# See https://docs.djangoproject.com/en/stable/ref/settings/#templates
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
            ],
        },
    },
]

# > Database Configuration
# This setting will use DATABASE_URL environment variable.
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
# https://github.com/kennethreitz/dj-database-url
SQLITE_PATH = "db.sqlite3"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, SQLITE_PATH),
    }
}

# > Middleware Definition
# In MIDDLEWARE, each middleware component is represented by a string: the full
# Python path to the middleware factory’s class or function name.
# https://docs.djangoproject.com/en/stable/ref/settings/#middleware
# https://docs.djangoproject.com/en/stable/topics/http/middleware/
MIDDLEWARE = [
    # Django middleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

# > URL Configuration
# A string representing the full Python import path to your root URL configuration.
# See https://docs.djangoproject.com/en/stable/ref/settings/#root-urlconf
ROOT_URLCONF = "django_iam.urls"

# > Staticfile Directory
# This is where Django will look for static files outside the directories of
# applications which are used by default.
# https://docs.djangoproject.com/en/stable/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]

# This is where Django will put files collected from application directories
# and custom direcotires set in "STATICFILES_DIRS" when
# using "django-admin collectstatic" command.
# https://docs.djangoproject.com/en/stable/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# This is the URL that will be used when serving static files, e.g.
# https://llamasavers.com/static/
# https://docs.djangoproject.com/en/stable/ref/settings/#static-url
STATIC_URL = "/static/"

CSRF_TRUSTED_ORIGINS = ['https://kleberbaum-schett-net-snek-0-r66qp7v4hx4rw-8000.githubpreview.dev']

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
