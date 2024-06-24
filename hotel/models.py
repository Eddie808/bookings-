from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name_of_user = models.CharField(max_length=50)
    contact_of_user = models.CharField(max_length=50)
    date_booked = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name_of_user






class Hotel(models.Model):
    name_of_hotel = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50)
    price_range = models.CharField(max_length=20)
    contact_of_hotel = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    added_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name_of_hotel


