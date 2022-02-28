from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from form.models import Form

# Create your tests here.
class TestSetup(APITestCase):
    # this function name should be camel case by convention
    # in APITestCase
    def setUp(self):
        self.register_url = reverse('users:user-list')
        self.login_url = reverse('login')
        self.user_details_url = reverse('details:index')

        self.auth_test_data = {
            'username': 'daniel',
            'password': 'test-pass'
        }

        self.post_test_data = {
            'title': 'Post Test Title',
            'first_name': 'Daniel',
            'surname': 'Taylor',
            'dob': '12/02/1990',
            'company_name': 'Trades International',
            'address': '104, My Street, London',
            'telephone': '+254729097858',
            'bid': 'high',
            'google_id': '1234567890',
        }

        return super().setUp()

    # this function name should be camel case by convention
    # in APITestCase
    def tearDown(self):
        return super().tearDown()