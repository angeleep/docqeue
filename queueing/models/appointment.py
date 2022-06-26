from django.db import models

class Appointment(models.Model):
    patient_name = models.CharField(max_length=50)
    email = models.EmailField()
    details = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True) 
    schedule = models.DateTimeField()
