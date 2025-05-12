from django.db import models

# Create your models here.
class Doctor(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    consultant_fees = models.IntegerField()