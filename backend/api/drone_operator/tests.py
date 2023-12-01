import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import DroneInfo

class droneTesting(TestCase):
    def setUp(self):
        self.userDataStaff = {"password": "password", "email": "staff@staff.com", "is_staff": True}
        self.userData = {"password": "password", "email": "user@user.com", "is_staff": False}
        self.droneData = {"ownerID": self.userDataStaff['email'], "size": "small", "status": "active"}
        self.client = APIClient()

        response = self.client.post('/user/create_account', data=self.userDataStaff)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.userToken = json.loads(response.content)['token']
        self.userInfo = json.loads(response.content)['user'] #id, email, password, staff, admin
        
    def test_register_and_delete_drone(self):
        try:
            # Register Drone
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            registerResponse = self.client.post('/drone_operator/register_drone', data=self.droneData)
            self.assertEqual(registerResponse.status_code, status.HTTP_201_CREATED)
            droneID = json.loads(registerResponse.content)['id']

            drone = DroneInfo.objects.get(id=droneID)
            self.assertEqual(drone.ownerID.email, self.droneData['ownerID'])
            self.assertEqual(drone.size, self.droneData['size'])
            self.assertEqual(drone.status, self.droneData['status'])

            # Delete Drone
            currentCount = DroneInfo.objects.all().count()
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            droneResponse = self.client.delete('/drone_operator/decomission_drone', data={"id": droneID})
            self.assertEqual(droneResponse.status_code, status.HTTP_200_OK)
            self.assertEqual(DroneInfo.objects.all().count(), currentCount-1)
        except Exception as e:
            self.fail(e)

    def test_get_and_update_status(self):
        try:
            # Register Drone
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            registerResponse = self.client.post('/drone_operator/register_drone', data=self.droneData)
            self.assertEqual(registerResponse.status_code, status.HTTP_201_CREATED)

            # Get Drone
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            droneResponse = self.client.get('/drone_operator/get_all_owned_drones', QUERY_STRING=f"ownerID={self.userDataStaff['email']}")
            self.assertEqual(droneResponse.status_code, status.HTTP_200_OK)
            droneID = json.loads(droneResponse.content)[0]['id']

            # Get Status
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            statusResponse = self.client.get('/drone_operator/get_status', QUERY_STRING=f"droneID={droneID}")
            self.assertEqual(statusResponse.status_code, status.HTTP_200_OK)
            self.assertEqual(self.droneData['status'],  json.loads(statusResponse.content)['status'])

            # Update Status
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            newStatusResponse = self.client.post('/drone_operator/update_status', data={"droneID": droneID, "status": "inactive"})
            self.assertEqual(statusResponse.status_code, status.HTTP_200_OK)
            self.assertEqual("inactive",  json.loads(newStatusResponse.content)['status'])
            drone = DroneInfo.objects.get(id=droneID)
            self.assertEqual(drone.status, "inactive")

        except Exception as e:
            self.fail(e)