from django.urls import path,include
from user.views import *

from django.contrib.auth import views as auth_views

app_name="user"

urlpatterns = [
    path("",include("django.contrib.auth.urls")),
    path("login2/",auth_views.LoginView.as_view(template_name="users/login2.html"),name="login2")
]
