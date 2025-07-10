from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Usuario, TipoTecnico, Tecnico
from .serializers import UsuarioSerializer, TipoTecnicoSerializer, TecnicoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TipoTecnicoViewSet(viewsets.ModelViewSet):
    queryset = TipoTecnico.objects.all()
    serializer_class = TipoTecnicoSerializer

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.none()  # Esto es necesario para el router
    serializer_class = TecnicoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tecnico.objects.filter(creado_por=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)
