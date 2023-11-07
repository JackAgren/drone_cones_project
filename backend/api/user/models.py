from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from .managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        db_collation="ucs_basic",
        unique=True, 
        error_messages={"unique": "An account with that email already exists"}
    )
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email


"""
Need to define groups and group permissions.
"""
