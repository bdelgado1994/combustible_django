from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views.generic import *
from django.urls import reverse_lazy


class RegistrationUserView(CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy("user:login")
    template_name="users/register.html"
