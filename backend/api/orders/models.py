from django.db import models
from django.contrib.postgres.fields import ArrayField


class Cones(models.Model):
    cone = models.CharField(max_length=25)
    iceCream = models.CharField(max_length=25) #number of scoops = size of iceCream
    toppings = ArrayField(models.CharField(max_length=25))
    cost = models.FloatField()


class Orders(models.Model):
    userID = models.IntegerField()
    droneID = ArrayField(models.IntegerField())
    cones = ArrayField(models.IntegerField())
    location = models.CharField(max_length=200)
    timeOrdered = models.DateTimeField()
    timeDelivered = models.DateTimeField(null=True)
    #number of cones = size of order object
