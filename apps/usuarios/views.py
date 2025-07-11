from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Usuario, TipoTecnico, Tecnico
from .serializers import UsuarioSerializer, TipoTecnicoSerializer, TecnicoSerializer, RegistroUsuarioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TipoTecnicoViewSet(viewsets.ModelViewSet):
    queryset = TipoTecnico.objects.all()
    serializer_class = TipoTecnicoSerializer

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.none()
    serializer_class = TecnicoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Evita error cuando no hay usuario autenticado (Swagger, etc.)
        if getattr(self, 'swagger_fake_view', False) or not self.request.user.is_authenticated:
            return Tecnico.objects.none()
        return Tecnico.objects.filter(creado_por=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)

class RegistroUsuarioView(APIView):
    permission_classes = []  # Permitir acceso público

    def post(self, request):
        serializer = RegistroUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)
