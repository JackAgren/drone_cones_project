from django.db import models

class PermissionsRequest(models.Model):
    request = models.ArrayField(models.CharField(max_length=20))
    