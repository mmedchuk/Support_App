from django.urls import path

from users.api import UserCreateAPI

urlpatterns = [
    path("", UserCreateAPI.as_view()),
]
