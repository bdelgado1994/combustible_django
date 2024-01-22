from django.urls import path
from bases.views import *
app_name="bases"

urlpatterns = [
    path("",view=HomeView.as_view(),name="home")
]
