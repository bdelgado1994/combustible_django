from django.shortcuts import render
from django.views.generic import *
from ctrl_comb.models import *

class BrandList (ListView):
    template_name='ctrl_comb/brand.html'
    context_object_name="obj"
    model=Brand
    ordering=["description"]