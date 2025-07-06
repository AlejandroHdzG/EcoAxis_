from rest_framework import serializers
from EcoAxis.models import *

# Clase base reutilizable
class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class UsuarioSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Usuario

class EmpresaSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Empresa

class CatalogoSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Catalogo

class SucursalSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Sucursal

class ProductosEmpresaSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = ProductosEmpresas

class SucursalProductosEmpresasSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = SucursalProductosEmpresas

class TipoTecnicoSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = TipoTecnico

class TecnicoSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Tecnico

class ReporteSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Reporte

class MantenimientoSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Mantenimiento

class SubscripcionSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Subscripcion

class ReciboCfeSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = ReciboCfe

class TicketSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Ticket
