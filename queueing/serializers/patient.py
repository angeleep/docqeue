from queueing.models.patient import Patient
from rest_framework import serializers

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'email']
