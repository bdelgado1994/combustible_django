from django.shortcuts import render,HttpResponse
from django.views.generic import *

class AboutView(TemplateView):
    template_name="pages/about.html"
