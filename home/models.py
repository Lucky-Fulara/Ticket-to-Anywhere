from django.db import models

class Plane(models.Model):
    plane_number = models.CharField(max_length=50)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    seats_available = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

#bus
# bus_booking/models.py
from django.db import models

class BusBooking(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bus_number = models.CharField(max_length=20)
    seat_number = models.CharField(max_length=10)
