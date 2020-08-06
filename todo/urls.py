from django.urls import path
from .views import home_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home_view, name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="todo/login.html"
        ),
        name="users-login",
    ),
]
