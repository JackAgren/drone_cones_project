import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import DroneInfo

class droneTesting(TestCase):
    def setUp(self):
        self.userDataStaff = {"password": "password", "email": "test@test.com", "is_staff": True}
        self.userData = {"password": "password", "email": "test@test.com", "is_staff": False}
        self.droneData = {"ownerID": self.userData['email'], "size": "small", "status": "active"}
        self.client = APIClient()
        
    def test_register_drone(self):
        try:
            userResponse = self.client.post('/user/create_account', data=self.userData)
            self.assertEqual(userResponse.status_code, status.HTTP_200_OK)
            userToken = json.loads(userResponse.content)['token']
            
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {userToken}')
            droneResponse = self.client.post('/drone_operator/register_drone', data=self.droneData)
            self.assertEqual(droneResponse.status_code, status.HTTP_201_CREATED)

            drone = DroneInfo.objects.get()
            self.assertEqual(drone.ownerID.email, self.droneData['ownerID'])
            self.assertEqual(drone.size, self.droneData['size'])
            self.assertEqual(drone.status, self.droneData['status'])
        except Exception as e:
            self.fail(e)