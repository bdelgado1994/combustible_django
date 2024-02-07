from django.urls import path
from ctrl_comb.views import *
urlpatterns = [
    path("brand",BrandList.as_view(),name="brand_list")
]
