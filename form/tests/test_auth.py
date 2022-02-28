from .test_setup import TestSetup
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import pdb

class TestAuth(TestSetup):

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)
        self.assertNotEqual(res.status_code, 201)
        self.assertNotEqual(res.status_code, 200)
    
    def test_user_can_register_correctly(self):
        res = self.client.post(self.register_url, self.auth_test_data, format="json")
        # pdb.set_trace()
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data['username'], self.auth_test_data['username'])

    def test_user_cannot_register_existing_username(self):
        self.client.post(self.register_url, self.auth_test_data, format="json")
        res = self.client.post(
            self.register_url, self.auth_test_data, format="json")
        self.assertEqual(res.status_code, 400)
    
    def test_user_cannot_login_with_no_data(self):
        res = self.client.post(self.login_url)
        self.assertEqual(res.status_code, 400)
        self.assertNotEqual(res.status_code, 200)

    def test_user_cannot_login_with_unregistered_username(self):
        res = self.client.post(self.login_url, self.auth_test_data, format="json")
        self.assertEqual(res.status_code, 400)

    def test_user_can_login_correctly_with_registered_username(self):
        self.client.post(self.register_url, self.auth_test_data, format="json")
        res = self.client.post(self.login_url, self.auth_test_data, format="json")
        self.assertEqual(res.status_code, 200)

    def test_user_cannot_login_with_wrong_password(self):
        self.client.post(self.register_url, self.auth_test_data, format="json")
        self.auth_test_data['password'] = "unregisteredpassword"
        res = self.client.post(self.login_url, self.auth_test_data, format="json")
        self.assertEqual(res.status_code, 400)
    
    def test_token_auth(self):
        user = User.objects.create_user(self.auth_test_data)
        token = Token.objects.create(user=user)
        # print(token)
