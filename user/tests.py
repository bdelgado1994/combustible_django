from django.test import TestCase
from django.contrib.auth import get_user_model

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