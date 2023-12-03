import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Inventory 
# Create your tests here.
class inventoryTesting(TestCase):
    def setUp(self):
        self.userDataStaff = {"password": "password", "email": "staff@staff.com", "is_staff": True}
        self.client = APIClient()
        response = self.client.post('/user/create_account', data=self.userDataStaff)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.userToken = json.loads(response.content)['token']
        self.userInfo = json.loads(response.content)['user'] #id, email, password, staff, admin
        self.icecreamTest = {"description": "Flavor", "salesPrice": 12.00, "costPerUnit": 4.00, "quantity": 0, "category": "icecream"}

    def test_add_and_delete_inventory(self):
        try:
            #Add Item
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            addResponse = self.client.post('/inventory/add', data=self.icecreamTest)
            self.assertEqual(addResponse.status_code, status.HTTP_201_CREATED)
            itemDescription = json.loads(addResponse.content)['description']

            #Test 
            item = Inventory.objects.get(description=itemDescription)
            self.assertEqual(item.salesPrice, self.icecreamTest['salesPrice'])
            self.assertEqual(item.costPerUnit, self.icecreamTest['costPerUnit'])
            self.assertEqual(item.quantity, self.icecreamTest['quantity'])
            self.assertEqual(item.category, self.icecreamTest['category'])
            
            #Delete Item
            deleteResponse = self.client.post('/inventory/remove', data={"description": self.icecreamTest['description']})
            self.assertEqual(deleteResponse.data['success'], f"{itemDescription} deleted.")
        except Exception as e:
            self.fail(e)

    def test_update_inventory(self):
        try:
            self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.userToken}')
            addResponse = self.client.post('/inventory/add', data=self.icecreamTest)
            self.assertEqual(addResponse.status_code, status.HTTP_201_CREATED)
            itemDescription = json.loads(addResponse.content)['description']

            updateResponse = self.client.post('/inventory/update_item', data={'description': self.icecreamTest['description'], "quantity": 100})
            item = Inventory.objects.get(description=itemDescription)
            self.assertEqual(updateResponse.data['success'], f"{itemDescription} updated.")
            self.assertEqual(item.quantity, 100)

        except Exception as e:
            self.fail(e)



