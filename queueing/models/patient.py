from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    priority_number=models.IntegerField(default=0)
