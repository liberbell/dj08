from django.urls import path
from .views import (RegistUserView, HomeView, UserLoginView, UserLogoutView)

app_name = "accounts"

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
]
