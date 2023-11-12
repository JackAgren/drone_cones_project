from django.db import models
from django.contrib.postgres.fields import ArrayField


class Cones(models.Model):
    cone = models.CharField(max_length=25)
    iceCream = ArrayField(models.CharField(max_length=25))
    toppings = ArrayField(models.CharField(max_length=25))
    cost = models.FloatField()


class Orders(models.Model):
    userID = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    droneID = models.ForeignKey('drone_operator.DroneInfo', on_delete=models.CASCADE)
    cones = ArrayField(models.IntegerField())
    location = models.CharField(max_length=200)
    timeOrdered = models.DateTimeField()
    timeDelivered = models.DateTimeField(null=True)
    total = models.IntegerField()
    #number of cones = size of order object
