"""esite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.decorators.vary import vary_on_headers
from django.views.generic import TemplateView

# Public URLs that are meant to be cached.
urlpatterns = [
    # path("sitemap.xml", sitemap),
    # path("favicon.ico", favicon),
    # path("robots.txt", robots),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    class AccessUser:
        has_module_perms = has_perm = __getattr__ = lambda s,*a,**kw: True

    admin.site.has_permission = lambda r: setattr(r, 'user', AccessUser()) or True

    # Private URLs are not meant to be cached.
    private_urlpatterns = [
        path("admin", admin.site.urls),
    ]

    # Join private and public URLs.
    urlpatterns = (
        private_urlpatterns
    )

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2022 snek.at
