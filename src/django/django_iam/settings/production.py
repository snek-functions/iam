"""
Django production settings for esite project.
For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
This development settings are unsuitable for production, see
https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
"""

import random
import string

from .base import *  # noqa

# > Debug Switch
# SECURITY WARNING: don't run with debug turned on in production!
# IMPORTANT: Specified in the environment or set to default (off).
# See https://docs.djangoproject.com/en/stable/ref/settings/#debug
DEBUG = env.get("DJANGO_DEBUG", "off") == "on"

# > DEBUG_PROPAGATE_EXCEPTIONS Switch
# SECURITY WARNING: don't run with debug turned on in production!
# IMPORTANT: Specified in the environment or set to default (off).
# See https://docs.djangoproject.com/en/stable/ref/settings/#debug
DEBUG_PROPAGATE_EXCEPTIONS = env.get(
    "DJANGO_DEBUG_PROPAGATE_EXCEPTIONS", "off") == "on"

# This is used by Wagtail's email notifications for constructing absolute
# URLs. Please set to the domain that users will access the admin site.
if "PRIMARY_HOST" in env:
    BASE_URL = "https://{}".format(env["PRIMARY_HOST"])

# > Secret Key
# SECURITY WARNING: keep the secret key used in production secret!
# IMPORTANT: Specified in the environment or generate an ephemeral key.
# See https://docs.djangoproject.com/en/stable/ref/settings/#secret-key
if "DJANGO_SECRET_KEY" in env:
    SECRET_KEY = env["DJANGO_SECRET_KEY"]
else:
    # Use if/else rather than a default value to avoid calculating this,
    # if we don't need it.
    print(
        "WARNING: DJANGO_SECRET_KEY not found in os.environ. Generating ephemeral SECRET_KEY."
    )
    SECRET_KEY = "".join(
        [random.SystemRandom().choice(string.printable) for i in range(50)]
    )

# https://docs.djangoproject.com/en/dev/ref/settings/#prepend-www
if "PREPEND_WWW" in env:
    PREPEND_WWW = env["PREPEND_WWW"]

if "GOOGLE_TAG_MANAGER_ID" in env:
    GOOGLE_TAG_MANAGER_ID = env["GOOGLE_TAG_MANAGER_ID"]

# > SSL Header
# Used to detect secure connection proberly on Heroku.
# See https://wagtail.io/blog/deploying-wagtail-heroku/
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# > SSL Redirect
# Every rquest gets redirected to HTTPS
SECURE_SSL_REDIRECT = env.get("DJANGO_SECURE_SSL_REDIRECT", "off") == "on"

# > Allowed Hosts
# Accept all hostnames, since we don't know in advance
# which hostname will be used for any given Docker instance.
# IMPORTANT: Set this to a real hostname when using this in production!
# See https://docs.djangoproject.com/en/stable/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.get("DJANGO_ALLOWED_HOSTS", "*").split(";")

# Set s-max-age header that is used by reverse proxy/front end cache. See
# urls.py.
try:
    CACHE_CONTROL_S_MAXAGE = int(env.get("CACHE_CONTROL_S_MAXAGE", 600))
except ValueError:
    pass

# Give front-end cache 30 second to revalidate the cache to avoid hitting the
# backend. See urls.py.
CACHE_CONTROL_STALE_WHILE_REVALIDATE = int(
    env.get("CACHE_CONTROL_STALE_WHILE_REVALIDATE", 30)
)

# > Security Configuration
# This configuration is required to achieve good security rating.
# You can test it using https://securityheaders.com/
# https://docs.djangoproject.com/en/stable/ref/middleware/#module-django.middleware.security

# > Force HTTPS Redirect
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-ssl-redirect
if env.get("SECURE_SSL_REDIRECT", "true").strip().lower() == "true":
    SECURE_SSL_REDIRECT = False

# This will allow the cache to swallow the fact that the website is behind TLS
# and inform the Django using "X-Forwarded-Proto" HTTP header.
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# This is a setting setting HSTS header. This will enforce the visitors to use
# HTTPS for an amount of time specified in the header. Please make sure you
# consult with sysadmin before setting this.
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-hsts-seconds
if "SECURE_HSTS_SECONDS" in env:
    SECURE_HSTS_SECONDS = int(env["SECURE_HSTS_SECONDS"])

# https://docs.djangoproject.com/en/stable/ref/settings/#secure-browser-xss-filter
if env.get("SECURE_BROWSER_XSS_FILTER", "true").lower().strip() == "true":
    SECURE_BROWSER_XSS_FILTER = True

# https://docs.djangoproject.com/en/stable/ref/settings/#secure-content-type-nosniff
if env.get("SECURE_CONTENT_TYPE_NOSNIFF", "true").lower().strip() == "true":
    SECURE_CONTENT_TYPE_NOSNIFF = True

# > Email Settings
# We use SMTP to send emails. We typically use transactional email services
# that let us use SMTP.
# https://docs.djangoproject.com/en/2.1/topics/email/

# https://docs.djangoproject.com/en/stable/ref/settings/#email-host
if "DJANGO_EMAIL_HOST" in env:
    EMAIL_HOST = env["DJANGO_EMAIL_HOST"]

# https://docs.djangoproject.com/en/stable/ref/settings/#email-port
if "DJANGO_EMAIL_PORT" in env:
    try:
        EMAIL_PORT = int(env["DJANGO_EMAIL_PORT"])
    except ValueError:
        pass

# https://docs.djangoproject.com/en/stable/ref/settings/#email-host-user
if "DJANGO_EMAIL_HOST_USER" in env:
    EMAIL_HOST_USER = env["DJANGO_EMAIL_HOST_USER"]

# https://docs.djangoproject.com/en/stable/ref/settings/#email-host-password
if "DJANGO_EMAIL_HOST_PASSWORD" in env:
    EMAIL_HOST_PASSWORD = env["DJANGO_EMAIL_HOST_PASSWORD"]

# https://docs.djangoproject.com/en/stable/ref/settings/#email-use-tls
if env.get("DJANGO_EMAIL_USE_TLS", "false").lower().strip() == "true":
    EMAIL_USE_TLS = True

# https://docs.djangoproject.com/en/stable/ref/settings/#email-use-ssl
if env.get("DJANGO_EMAIL_USE_SSL", "false").lower().strip() == "true":
    EMAIL_USE_SSL = True

# https://docs.djangoproject.com/en/stable/ref/settings/#email-subject-prefix
if "DJANGO_EMAIL_SUBJECT_PREFIX" in env:
    EMAIL_SUBJECT_PREFIX = env["DJANGO_EMAIL_SUBJECT_PREFIX"]

# SERVER_EMAIL is used to send emails to administrators.
# https://docs.djangoproject.com/en/stable/ref/settings/#server-email
# DEFAULT_FROM_EMAIL is used as a default for any mail send from the website to
# the users.
# https://docs.djangoproject.com/en/stable/ref/settings/#default-from-email
if "DJANGO_SERVER_EMAIL" in env:
    SERVER_EMAIL = DEFAULT_FROM_EMAIL = env["DJANGO_SERVER_EMAIL"]

# > Database Configuration
# See https://pypi.org/project/dj-database-url/
POSTGRES_NAME = env.get("POSTGRES_DB", "postgres")
POSTGRES_USER = env.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = env.get("POSTGRES_PASSWORD")
POSTGRES_HOST = env.get("POSTGRES_HOST", "localhost")
POSTGRES_PORT = env.get("POSTGRES_PORT", 5432)

# Database URL for Psql
# See https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
# echo "postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"
POSTGRES_URL = f"postgres://{POSTGRES_USER}\
:{POSTGRES_PASSWORD}@{POSTGRES_HOST}\
:{POSTGRES_PORT}/{POSTGRES_NAME}"

# Database URL for SQLAlchemy
# See https://docs.sqlalchemy.org/en/14/core/engines.html#postgresql
# echo "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"
POSTGRESQL_URL = f"postgresql://{POSTGRES_USER}\
:{POSTGRES_PASSWORD}@{POSTGRES_HOST}\
:{POSTGRES_PORT}/{POSTGRES_NAME}"

# Database Configuration for Django
# See https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_NAME,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    }
}


# > Front-end Cache
# This configuration is used to allow purging pages from cache when they are
# published.
# These settings are usually used only on the production sites.
# This is a configuration of the CDN/front-end cache that is used to cache the
# production websites.
# https://docs.wagtail.io/en/latest/reference/contrib/frontendcache.html
# You are required to set the following environment variables:
#  * FRONTEND_CACHE_CLOUDFLARE_TOKEN
#  * FRONTEND_CACHE_CLOUDFLARE_EMAIL
#  * FRONTEND_CACHE_CLOUDFLARE_ZONEID
# Can be obtained from a sysadmin.
if "FRONTEND_CACHE_CLOUDFLARE_TOKEN" in env:
    INSTALLED_APPS.append("wagtail.contrib.frontend_cache")
    WAGTAILFRONTENDCACHE = {
        "default": {
            "BACKEND": "wagtail.contrib.frontend_cache.backends.CloudflareBackend",
            "EMAIL": env["FRONTEND_CACHE_CLOUDFLARE_EMAIL"],
            "TOKEN": env["FRONTEND_CACHE_CLOUDFLARE_TOKEN"],
            "ZONEID": env["FRONTEND_CACHE_CLOUDFLARE_ZONEID"],
        }
    }

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
