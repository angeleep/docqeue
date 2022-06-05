from queueing.serializers.doctor import DoctorSerializer
from queueing.models.doctor import Doctor
from rest_framework import viewsets

# ViewSets define the view behavior.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
