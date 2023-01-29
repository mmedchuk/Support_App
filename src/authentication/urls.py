import rest_framework_simplejwt.views as views
from django.urls import path

urlpatterns = [
    path("token/", views.TokenObtainPairView.as_view()),
    path("token/refresh/", views.TokenRefreshView.as_view()),
]
