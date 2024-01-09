import functools
from operator import add

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

__all__ = ["urlpatterns"]

# Project-level URLs

project_urls = [
    path("", include("reactor.core.urls")),
]


# Includes from the project's contrib apps

contrib_app_urls = []


# Admin site

admin_urls = [
    path("admin/", admin.site.urls),
]


# Internationalization

i18n_urls = [
    path("i18n/", include("django.conf.urls.i18n")),
]


# Static files and media

static_urls = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

media_urls = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Debugging URLs

debug_urls = []


# Export URLs

url_groups = [
    project_urls,
    contrib_app_urls,
    admin_urls,
    i18n_urls,
    static_urls,
    media_urls,
    debug_urls,
]


# Combined 'urlpatterns'

urlpatterns = functools.reduce(add, url_groups)
