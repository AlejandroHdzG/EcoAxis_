from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    Usuario, Empresa, Catalogo, Sucursal, ProductosEmpresas, SucursalProductosEmpresas,
    TipoTecnico, Tecnico, Reporte, Mantenimiento, Subscripcion, ReciboCfe, Ticket
)
from .serializers import (
    UsuarioSerializer, EmpresaSerializer, CatalogoSerializer, SucursalSerializer, ProductosEmpresasSerializer,
    SucursalProductosEmpresasSerializer, TipoTecnicoSerializer, TecnicoSerializer, ReporteSerializer,
    MantenimientoSerializer, SubscripcionSerializer, ReciboCfeSerializer, TicketSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo.objects.all()
    serializer_class = CatalogoSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class ProductosEmpresasViewSet(viewsets.ModelViewSet):
    queryset = ProductosEmpresas.objects.all()
    serializer_class = ProductosEmpresasSerializer

class SucursalProductosEmpresasViewSet(viewsets.ModelViewSet):
    queryset = SucursalProductosEmpresas.objects.all()
    serializer_class = SucursalProductosEmpresasSerializer

class TipoTecnicoViewSet(viewsets.ModelViewSet):
    queryset = TipoTecnico.objects.all()
    serializer_class = TipoTecnicoSerializer

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer

class SubscripcionViewSet(viewsets.ModelViewSet):
    queryset = Subscripcion.objects.all()
    serializer_class = SubscripcionSerializer

class ReciboCfeViewSet(viewsets.ModelViewSet):
    queryset = ReciboCfe.objects.all()
    serializer_class = ReciboCfeSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
