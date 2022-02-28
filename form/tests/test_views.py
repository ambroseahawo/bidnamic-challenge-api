from django.forms import ValidationError
from .test_setup import TestSetup
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import pdb

class TestViews(TestSetup):

    def obtain_token(self):
        user = User.objects.create_user(self.auth_test_data)
        token = Token.objects.create(user=user)
        return token

    def test_unauthenticated_user_cannot_get_details(self):
        res = self.client.get(self.user_details_url)
        self.assertEqual(res.status_code, 401)
        self.assertNotEqual(res.status_code, 200)
    
    def test_authenticated_user_can_get_details(self):
        token = self.obtain_token()
        res = self.client.get(self.user_details_url, HTTP_AUTHORIZATION="token {0}".format(token))
        self.assertEqual(res.status_code, 200)
        self.assertNotEqual(res.status_code, 401)
    
    def test_unauthenticated_user_cannot_post_details(self):
        res = self.client.post(self.user_details_url, self.post_test_data)
        self.assertEqual(res.status_code, 401)
        self.assertNotEqual(res.status_code, 200)

    def test_authenticated_user_can_post_details(self):
        token = self.obtain_token()
        res = self.client.post(self.user_details_url, self.post_test_data, 
                                    HTTP_AUTHORIZATION="token {0}".format(token))
        self.assertEqual(res.status_code, 201)
        self.assertNotEqual(res.status_code, 401)

    def test_user_cannot_submit_invalid_bidding_settings(self):
        token = self.obtain_token()
        self.post_test_data['bid'] = 'randomstring'
        res = self.client.post(self.user_details_url, self.post_test_data,
                               HTTP_AUTHORIZATION="token {0}".format(token))
        self.assertEqual(res.status_code, 400)
        self.assertNotEqual(res.status_code, 201)
    
    def test_user_below_18years_cannot_post_details(self):
        token = self.obtain_token()
        self.post_test_data['dob'] = '12/02/2020'
        res = self.client.post(self.user_details_url, self.post_test_data,
                               HTTP_AUTHORIZATION="token {0}".format(token))
        self.assertEqual(res.status_code, 400)
        self.assertNotEqual(res.status_code, 201)
