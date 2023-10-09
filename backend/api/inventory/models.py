from django.db import models

# Create your models here.
class Inventory(models.Model):
    droneId = models.CharField(max_length=20) 

    def __str__(self):
        return self.droneId
