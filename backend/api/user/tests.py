from django.shortcuts import get_object_or_404
from django.test import TestCase
from .models import CustomUser
from .serializers import UsersSerializer


class userTesting(TestCase):
  def setUp(self):
    self.userData = {"password": "password", "email": "test@test.com"}
    serializer = UsersSerializer(data=self.userData)
    if serializer.is_valid():
      serializer.save()
      user = CustomUser.objects.get(email=self.userData['email'])
      user.set_password(self.userData['password'])
      user.save()

  def test_user_exists(self):
    try:
      user = CustomUser.objects.get(email=self.userData['email'])
      self.assertEqual(user.email, self.userData['email'])
      self.assertEqual(user.is_staff, False)
      self.assertEqual(user.is_superuser, False)
      self.assertNotEqual(user.password, self.userData['password'])#shows hashing
    except Exception as e:
      self.fail()

  def test_delete_user(self):
    try:
      self.assertEqual(CustomUser.objects.all().count(), 1)
      user = CustomUser.objects.get(email=self.userData['email'])
      user.delete()
      self.assertEqual(CustomUser.objects.all().count(), 0)
    except Exception as e:
      self.fail()