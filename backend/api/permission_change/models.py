from django.db import models
from django.contrib.postgres.fields import ArrayField

class PermissionsRequest(models.Model):
    request = ArrayField(models.CharField(max_length=20))
    