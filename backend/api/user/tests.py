import json
from django.test import TestCase
from .models import CustomUser
from rest_framework import status
from rest_framework.test import APIClient

class userTesting(TestCase):
  def setUp(self):
    self.userData = {"password": "password", "email": "test@test.com"}
    self.client = APIClient()

  def test_user_creation_and_deletion(self):
    ## Create User ##
    try:
       # Access the create_account function
      createResponse = self.client.post('/user/create_account', data=self.userData)
      self.assertEqual(createResponse.status_code, status.HTTP_200_OK)
      userToken = json.loads(createResponse.content)['token']

      user = CustomUser.objects.get(email=self.userData['email'])
      self.assertEqual(user.email, self.userData['email'])
      self.assertEqual(user.is_staff, False)
      self.assertEqual(user.is_superuser, False)
      self.assertNotEqual(user.password, self.userData['password'])#shows hashing
    except Exception as e:
      self.fail("Failed to create User")

    ## Delete User ##
    try:
      self.assertEqual(CustomUser.objects.all().count(), 1)

      self.client.credentials(HTTP_AUTHORIZATION=f'Token {userToken}')
      deleteResponse = self.client.delete('/user/delete_account', data=self.userData)
      self.assertEqual(deleteResponse.status_code, status.HTTP_200_OK)

      self.assertEqual(CustomUser.objects.all().count(), 0)
    except Exception as e:
      self.fail("Failed to delete User")