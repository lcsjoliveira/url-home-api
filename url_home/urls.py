from django.urls import path

from .views import create_url, redirect_url, get_url_details


urlpatterns = [
    path("v1/urls", create_url),
    path("v1/urls/<str:url_id>", get_url_details),
    path("<str:url_id>", redirect_url),
]
