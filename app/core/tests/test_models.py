from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        username='dablblba'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            username=username,
            password=password
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'admin123',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
