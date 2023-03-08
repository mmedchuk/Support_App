from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from config.settings.openapi import schema_view

v1: list = [
    path("admin/", admin.site.urls),
    path("exchange-rates/", include("exchange_rates.urls")),
    path("", include("core.urls")),
    path("users/", include("users.urls")),
    path("auth/", include("authentication.urls")),
]

openapi_urls: list = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns: list = [
    path("v1/", include(v1)),
    path("", include(openapi_urls)),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
