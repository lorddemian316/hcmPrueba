from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JornadaSerializer
from .models import Jornada

class JornadaViewSet(viewsets.ModelViewSet):
    queryset=Jornada.objects.all().order_by('-id')
    serializer_class=JornadaSerializer