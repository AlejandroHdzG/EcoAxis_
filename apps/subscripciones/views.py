from django.shortcuts import render
from rest_framework import viewsets
from .models import Subscripcion
from .serializers import SubscripcionSerializer

# Create your views here.

class SubscripcionViewSet(viewsets.ModelViewSet):
    queryset = Subscripcion.objects.all()
    serializer_class = SubscripcionSerializer
