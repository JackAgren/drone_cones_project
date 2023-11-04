from django.db import models

class Inventory(models.Model):
    quantity = models.IntegerField()
    costPerUnit = models.FloatField()
    dateFilled = models.DateField()
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200, primary_key=True) #Unique identifier
    salesPrice = models.FloatField(default=0)
