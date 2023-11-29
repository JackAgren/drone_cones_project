import json
from django.test import TestCase
from .models import CustomUser
from rest_framework import status
from rest_framework.test import APIClient

class userTesting(TestCase):
    def setUp(self):
        self.userData = {"password": "password", "email": "test@test.com", "is_staff": True}
        self.droneData = {"ownerId": self.userData['email'], "size": "small", "status": "Active"}
        self.client = APIClient()
        
    def test_register_drone(self):
        try:
            userResponse = self.client.post('/user/create_account', data=self.userData)
            self.assertEqual(userResponse.status_code, status.HTTP_200_OK)
            userToken = json.loads(userResponse.content)['token']
            
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {userToken}')
            droneResponse = self.client.post('/drone_operator/register_drone', data=self.droneData)
            self.assertEqual(droneResponse.status_code, status.HTTP_200_OK)
        except Exception as e:
            self.fail(e)