from django.urls import path
from ctrl_comb.views import *
urlpatterns = [
    path("brand",BrandList.as_view(),name="brand_list"),
    path("brand/save",save_brand,name="save_brand"),
    path("brand/delete/<int:pk>",brand_delete,name="delete_brand"),
    path("brand/edit/<int:pk>",brand_edit,name="edit_brand"),
    #Modelo
    path("models",ModeloList.as_view(),name="model_list"),
    path("models/new",ModeloNew.as_view(),name="model_new"),
    path("models/<int:pk>",ModeloEdit.as_view(),name="model_edit"),
    path("models/delete/<int:pk>",ModeloDelete.as_view(),name="model_delete"),
]
