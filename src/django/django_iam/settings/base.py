"""
Django base settings for esite project.
For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

import os

env = os.environ.copy()

# > Root Paths
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# > Application Definition
# A list of strings designating all applications that are enabled in this
# Django installation.
# See https://docs.djangoproject.com/en/stable/ref/settings/#installed-apps
INSTALLED_APPS = [
    # Our own apps
    "django_iam.user",
    "django_iam.group",
    "django_iam.permission",
    "django_iam.ressource",
    "django_iam.role",

    # Django core apps
    "django.contrib.auth",
    "django.contrib.contenttypes",
]

# > Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Vienna"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# > USER Config
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-user-model
AUTH_USER_MODEL = 'user.User'

# > ORM Config
# Default primary key field type to use for models that don’t have a field
# with primary_key=True.
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
