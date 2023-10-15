from django.db import models

class DroneInfo(models.Model):
    ownerID = models.ForeignKey()
    status = models.CharField(max_length=25)
    size = models.CharField(max_length=25)