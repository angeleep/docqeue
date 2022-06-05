from queueing.serializers.patient import PatientSerializer
from queueing.models.patient import Patient
from rest_framework import viewsets

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
