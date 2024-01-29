from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Email Addres"})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "First Name"})
    )
    first_name = forms.CharField(
        widget=forms.TimeInput(attrs={"placeholder": "Your First Name"})
    )
    last_name = forms.CharField(
        widget=forms.TimeInput(attrs={"placeholder": "Your Last Name"})
    )
    password1 = forms.CharField(
        widget=forms.TimeInput(attrs={"placeholder": "Password"})
    )
    password2 = forms.CharField(
        widget=forms.TimeInput(attrs={"placeholder": "Confirm Password"})
    )

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({"class": "form-control"})

class CustomUserCreationForm2(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=(
            "email",
            "username",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username")
