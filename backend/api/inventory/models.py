from django.db import models

class Inventory(models.Model):
    quantity = models.IntegerField()
    costPerUnit = models.IntegerField()
    dateFilled = models.DateField()
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200, primary_key=True) #Unique identifier