from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating an new user with an email is successful"""
        email = 'test@teja.com'
        password = 'naga'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        '''Test the email for a new user in normailzed'''
        email = 'test@Teja.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        '''Test creating user with  no email rasies error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    
    def test_create_new_superuser(self):
        '''test creating an superuser'''
        user = get_user_model().objects.create_superuser(
            'test@teja.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)