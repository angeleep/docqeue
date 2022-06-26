from queueing.models.appointment import Appointment
from rest_framework import serializers

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'email' , 'details', 'added_on', 'schedule']
