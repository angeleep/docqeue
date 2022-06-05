from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    shift = models.CharField(max_length=50)
    info = models.CharField(max_length=50)
