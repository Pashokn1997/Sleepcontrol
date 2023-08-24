
from rest_framework import generics
from apps.sleepcontrolapp.models import SleepPoint
from apps.sleepcontrolapp.serializers import SleepPointGetAddSerializer


class SleepPointListCreate(generics.ListCreateAPIView):
    queryset = SleepPoint.objects.all()
    serializer_class = SleepPointGetAddSerializer


class SleepPointDelete(generics.DestroyAPIView):
    queryset = SleepPoint.objects.all()
