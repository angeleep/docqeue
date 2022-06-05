from queueing.models.doctor import Doctor
from rest_framework import serializers

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['name', 'shift', 'description']
