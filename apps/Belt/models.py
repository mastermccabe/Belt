from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
from datetime import date
from django.utils import timezone
import datetime

class Validator(models.Manager):
    def validChecker(self, postData):
        errors = {}

        if len(postData['name']) < 3:
            errors["name"] = "Name no fewer than 3 characters"
            print errors
        if len(postData['username']) < 3:
            errors["alias"] = "Alias no fewer than 3 characters"
            print errors
        if len(postData['password']) < 8:
            errors["password"] = "Password must be no fewer than 8 characters in length"
            print errors
        if (postData['password'] != postData['conf_password']):
            errors["password"] = "passwords do not match"
            print errors
        return errors

class Users(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = Validator()

class Trips(models.Model):
    destination = models.CharField(max_length=255)
    new_trip = models.ForeignKey(Users, related_name = "new_trip")
    joined_trips = models.ManyToManyField(Users, related_name = "joined_trips")
    travel_date_to = models.DateField(null=True)
    travel_date_from = models.DateField(null=True)
    # description = models.CharField(max_length=255)

# Trips.objects.raw('INSERT INTO `Belt_trips_joined_trips`(`trips_id`,`users_id`) VALUES (0,0);')
# (INSERT INTO `Belt_trips_joined_trips`(`id`,`trips_id`,`users_id`) VALUES (1,0,0);)
    # Trips.objects.filter(new_trip_id=)
# Trips.objects.create(destination="Phoenix",travel_date_to="2018-11-11",new_trip="1")
# Trips.objects.create(destination="Tahoe",travel_date_from="2017-10-11",travel_date_to="2017-11-11",new_trip=u)
