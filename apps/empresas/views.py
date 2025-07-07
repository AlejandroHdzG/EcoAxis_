from django.shortcuts import render
from rest_framework import viewsets
from .models import Empresa, Sucursal, ProductosEmpresas, SucursalProductosEmpresas
from .serializers import EmpresaSerializer, SucursalSerializer, ProductosEmpresasSerializer, SucursalProductosEmpresasSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class ProductosEmpresasViewSet(viewsets.ModelViewSet):
    queryset = ProductosEmpresas.objects.all()
    serializer_class = ProductosEmpresasSerializer

class SucursalProductosEmpresasViewSet(viewsets.ModelViewSet):
    queryset = SucursalProductosEmpresas.objects.all()
    serializer_class = SucursalProductosEmpresasSerializer
