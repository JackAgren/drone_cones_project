import json
from django.test import TestCase
from .models import CustomUser
from rest_framework import status
from rest_framework.test import APIClient


class userTesting(TestCase):
  def setUp(self):
    self.userData = {"password": "password", "email": "test@test.com"}
    self.userDataStaff = {"password": "password", "email": "staff@test.com", "is_staff": True}
    self.userDataAdmin = {"password": "password", "email": "admin@test.com", "is_superuser": True}
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

  def test_guest_functions(self):
    # Create Guest
    try:
      createResponse = self.client.post('/user/create_guest')
      self.assertEqual(createResponse.status_code, status.HTTP_200_OK)
      guestToken = json.loads(createResponse.content)['token']

      user = CustomUser.objects.get(email='guest@guest.com')
      self.assertEqual(user.email, 'guest@guest.com')
      self.assertEqual(user.is_staff, False)
      self.assertEqual(user.is_superuser, False)
    except Exception as e:
      self.fail("Guest Creation Failed")

    # Delete Guest
    try:
      currentCount = CustomUser.objects.all().count()
      self.client.credentials(HTTP_AUTHORIZATION=f'Token {guestToken}')
      deleteResponse = self.client.delete('/user/delete_guest')
      self.assertEqual(deleteResponse.status_code, status.HTTP_200_OK)
      self.assertEqual(CustomUser.objects.all().count(), currentCount-1)
    except Exception as e:
      self.fail("Guest Deletion Failed")

  def test_permission_checking(self):
    try:
      staffResponse = self.client.post('/user/create_account', data=self.userDataStaff)
      self.assertEqual(staffResponse.status_code, status.HTTP_200_OK)
      staffToken = json.loads(staffResponse.content)['token']
    
      adminResponse = self.client.post('/user/create_account', data=self.userDataAdmin)
      self.assertEqual(adminResponse.status_code, status.HTTP_200_OK)
      adminToken = json.loads(adminResponse.content)['token']

      self.client.credentials(HTTP_AUTHORIZATION=f'Token {staffToken}')
      staffPermissions = self.client.get('/user/get_permissions', QUERY_STRING=f"email={self.userDataStaff['email']}")
      self.assertEqual(json.loads(staffPermissions.content)['is_staff'], True)
      self.assertEqual(json.loads(staffPermissions.content)['is_superuser'], False)

      self.client.credentials(HTTP_AUTHORIZATION=f'Token {adminToken}')
      adminPermissions = self.client.get('/user/get_permissions', QUERY_STRING=f"email={self.userDataAdmin['email']}")
      self.assertEqual(json.loads(adminPermissions.content)['is_staff'], False)
      self.assertEqual(json.loads(adminPermissions.content)['is_superuser'], True)
    except Exception as e:
      self.fail("Failed to check permissions")

  def test_duplicate_users(self):
    try:
      createResponse1 = self.client.post('/user/create_account', data=self.userData)
      self.assertEqual(createResponse1.status_code, status.HTTP_200_OK)
      userToken = json.loads(createResponse1.content)['token']

      createResponse2 = self.client.post('/user/create_account', data=self.userData)
      self.assertEqual(createResponse2.status_code, status.HTTP_400_BAD_REQUEST)
      
      # Delete User
      currentCount = CustomUser.objects.all().count()
      self.client.credentials(HTTP_AUTHORIZATION=f'Token {userToken}')
      deleteResponse = self.client.delete('/user/delete_account', data=self.userData)
      self.assertEqual(deleteResponse.status_code, status.HTTP_200_OK)
      self.assertEqual(CustomUser.objects.all().count(), currentCount-1)
    except Exception as e:
      self.fail("Failed to deny two similar user creations")

