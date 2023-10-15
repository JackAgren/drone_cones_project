from django.db import models

class Inventory(models.Model):
    quantity = models.IntegerField()
    costPerUnit = models.IntegerField()
    dateFilled = models.DateField()
    descriptoin = models.CharField(max_length=200)