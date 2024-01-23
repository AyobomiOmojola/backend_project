from django.urls import path, re_path
from . import views

app_name = "jwt_auth"


urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
]