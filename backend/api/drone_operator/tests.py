import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import DroneInfo

class droneTesting(TestCase):
    def setUp(self):
        self.userDataStaff = {"password": "password", "email": "staff@staff.com", "is_staff": True}
        self.droneDataL = {"ownerID": self.userDataStaff['email'], "size": "large", "status": "active"}
        self.droneDataM = {"ownerID": self.userDataStaff['email'], "size": "medium", "status": "active"}
        self.droneDataS = {"ownerID": self.userDataStaff['email'], "size": "small", "status": "active"}
        self.client = APIClient()

        response = self.client.post('/user/create_account', data=self.userDataStaff)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.userToken = json.loads(response.content)['token']
        self.userInfo = json.loads(response.content)['user'] #id, email, password, staff, admin
        
    def test_register_and_delete_drone(self):
        try:
            # Register Drone
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            registerResponse = self.client.post('/drone_operator/register_drone', data=self.droneDataS)
            self.assertEqual(registerResponse.status_code, status.HTTP_201_CREATED)
            droneID = json.loads(registerResponse.content)['id']

            drone = DroneInfo.objects.get(id=droneID)
            self.assertEqual(drone.ownerID.email, self.droneDataS['ownerID'])
            self.assertEqual(drone.size, self.droneDataS['size'])
            self.assertEqual(drone.status, self.droneDataS['status'])

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
            registerResponse = self.client.post('/drone_operator/register_drone', data=self.droneDataS)
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
            self.assertEqual(self.droneDataS['status'],  json.loads(statusResponse.content)['status'])

            # Update Status
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            newStatusResponse = self.client.post('/drone_operator/update_status', data={"droneID": droneID, "status": "inactive"})
            self.assertEqual(statusResponse.status_code, status.HTTP_200_OK)
            self.assertEqual("inactive",  json.loads(newStatusResponse.content)['status'])
            drone = DroneInfo.objects.get(id=droneID)
            self.assertEqual(drone.status, "inactive")

        except Exception as e:
            self.fail(e)

    def test_drone_assignment(self):
        try:
            # Register Drones
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            registerResponse = self.client.post('/drone_operator/register_drone', data=self.droneDataS)
            self.assertEqual(registerResponse.status_code, status.HTTP_201_CREATED)

            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            registerResponse = self.client.post('/drone_operator/register_drone', data=self.droneDataM)
            self.assertEqual(registerResponse.status_code, status.HTTP_201_CREATED)

            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            registerResponse = self.client.post('/drone_operator/register_drone', data=self.droneDataL)
            self.assertEqual(registerResponse.status_code, status.HTTP_201_CREATED)

            # Get Drones
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            droneResponse = self.client.get('/drone_operator/get_all_owned_drones', QUERY_STRING=f"ownerID={self.userDataStaff['email']}")
            self.assertEqual(droneResponse.status_code, status.HTTP_200_OK)
            droneIDSm = json.loads(droneResponse.content)[0]['id']
            droneIDMd = json.loads(droneResponse.content)[1]['id']
            droneIDLg = json.loads(droneResponse.content)[2]['id']

            # Test Assignments
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            assignResponse = self.client.get('/drone_operator/get_delivering_drones', QUERY_STRING=f"cone_count={1}")
            self.assertEqual(droneIDSm , json.loads(assignResponse.content)[0]['id'])

            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            assignResponse = self.client.get('/drone_operator/get_delivering_drones', QUERY_STRING=f"cone_count={4}")
            self.assertEqual(droneIDMd , json.loads(assignResponse.content)[0]['id'])

            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            assignResponse = self.client.get('/drone_operator/get_delivering_drones', QUERY_STRING=f"cone_count={8}")
            self.assertEqual(droneIDLg , json.loads(assignResponse.content)[0]['id'])

            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            assignResponse = self.client.get('/drone_operator/get_delivering_drones', QUERY_STRING=f"cone_count={100}")
            self.assertEqual('Not enough drones.' , json.loads(assignResponse.content)['error'])
        except Exception as e:
            self.fail()