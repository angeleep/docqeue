from queueing.serializers.appointment import AppointmentSerializer
from queueing.models.appointment import Appointment
from rest_framework import viewsets

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
