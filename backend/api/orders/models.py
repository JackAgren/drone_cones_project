from django.db import models
from django.contrib.postgres.fields import ArrayField

    
class OrderObject(models.Model):
    cone = models.CharField(max_length=25)
    iceCream = models.ArrayField(models.CharField(max_length=25)) #number of scoops = size of iceCream
    toppings = models.ArrayField(models.CharField(max_length=25))
    cost = models.FloatField()
    
class Orders(models.Model):
    userID = models.IntegerField()
    droneID = models.ArrayField(models.IntegerField())
    order = models.ManyToManyField(OrderObject)
    location = models.CharField(max_length=200)
    timeOrdered = models.DateTimeField()
    timeDelivered = models.DateTimeField()
    #number of cones = size of order object
