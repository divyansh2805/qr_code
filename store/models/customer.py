from django.db import models
from store.models.location import Location

class Users(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
    patient_id = models.CharField(max_length=100, unique=True, null=True)
    patient_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True, default=None, blank=True)
    gender = models.CharField(max_length=15, null=True)
    phone = models.CharField(max_length=10, null=True, default=None, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    weight = models.IntegerField(null=True, default=None)
    date_field = models.DateField(default=None)

    xray = models.BooleanField(default=False)
    ecg = models.BooleanField(default=False)
    pft = models.BooleanField(default=False)
    audiometry = models.BooleanField(default=False)
    optometry = models.BooleanField(default=False)
    vitals = models.BooleanField(default=False)
    sample_collection = models.BooleanField(default=False)

    def __str__(self):
        return str(self.patient_name)