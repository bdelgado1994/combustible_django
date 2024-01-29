from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve
from user.forms import CustomUserCreationForm
from user.views import RegistrationUserView
class CustomUserTest(TestCase):
    def test_create_user(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username="debconsultores",
            email="correo@correo.com",
            password="123"
        )
        # Assertions
        self.assertEqual(user.username, "debconsultores")
        self.assertEqual(user.email, "correo@correo.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        superuser_model = get_user_model()
        superuser = superuser_model.objects.create_superuser(
            username="debconsultores",
            email="correo@correo.com",
            password="123"
        )
        # Assertions
        self.assertEqual(superuser.username, "debconsultores")
        self.assertEqual(superuser.email, "correo@correo.com")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

class UserRegisterTest(TestCase):
    def setUp(self):
        url=reverse("user:register")
        self.response=self.client.get(url)
    
    def test_plantilla_registro(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,"users/register.html")
        self.assertContains(self.response,"Registrar")
        self.assertNotContains(self.response,"Bienvenido")
    
    def test_registro_form(self):
        form=self.response.context.get("form")
        self.assertIsInstance(form,CustomUserCreationForm)
        self.assertContains(self.response,"csrfmiddlewaretoken")
        
    def test_registro_vista(self):
        view=resolve("/users/register/")
        self.assertEqual(view.func.__name__,RegistrationUserView.as_view().__name__)
    