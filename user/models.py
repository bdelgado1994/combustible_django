from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
from user.manager import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(_("Nombre de Usuario"), max_length=150)
    first_name = models.CharField(_("Nombre"))
    last_name = models.CharField(_("Apellido"))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "firstname"]

    def __str__(self) -> str:
        return str(self.email)
