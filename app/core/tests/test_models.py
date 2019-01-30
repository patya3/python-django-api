from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ test creating a new user with email is successful """
        email = 'test@valami.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # test the email for a new user is test_new_user_email_normalized
        email = 'test@VALAMI.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # test creating with no email raises error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        # creating a new test_create_new_superuser
        user = get_user_model().objects.create_superuser(
            'test@valami.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
