import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Orders

def setUp(self):
        self.userDataStaff = {"password": "password", "email": "staff@staff.com", "is_staff": True}
        self.client = APIClient()
        response = self.client.post('/user/create_account', data=self.userDataStaff)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.userToken = json.loads(response.content)['token']
        self.userInfo = json.loads(response.content)['user'] #id, email, password, staff, admin
        self.orderTest = {
        "userID": "staff@staff.com",
        "droneID": 1,
        "cones": [
            {
                "cone": "waffle",
                "toppings": [
                    "Sprinkles"
                ],
                "iceCream":[ "Strawberry"],
                "cost": 12.99
            },
            {
                "cone": "waffle",
                "toppings": [
                    "Sprinkles"
                ],
                "iceCream": ["Vanilla", "Chocolate"],
                "cost": 11.99
            }
        ],
        "location": "SALT LAKE"
    }

def test_add_order(self):
    try:
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
        addResponse = self.client.post('/orders/add', data=self.orderTest)
        self.assertEqual(addResponse.status_code, status.HTTP_201_CREATED)
        orderID = json.loads(addResponse.content)['orderID']

        order = Orders.objects.get(orderID=orderID)
        self.assertEqual(order.droneID, self.orderTest['droneID'])
        self.assertEqual(order.userID, self.orderTest['userID'])
        self.assertEqual(len(order.cones), len(self.orderTest['cones']))
        self.assertEqual(order.location, self.orderTest['location'])

    except Exception as e:
        self.fail(e)


