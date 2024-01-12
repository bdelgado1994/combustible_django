from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *

# def first_view(request):
#     template_name="base/home.html"
#     return render(request,template_name)
class HomeView(TemplateView):
    template_name="base/home.html"