from django.db import models

class Users(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=250)
    permissions = models.ArrayField(models.CharField(max_length=20))# admin, manager, drone owner, user