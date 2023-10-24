from django.db import models

class Inventory(models.Model):
    quantity = models.IntegerField()
    costPerUnit = models.IntegerField()
    dateFilled = models.DateField()
    description = models.CharField(max_length=200, primary_key=True) #Unique identifier