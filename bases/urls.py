from django.urls import path
from bases.views import *
app_name="core"

urlpatterns = [
    path("",view=first_view,name="first")
]
