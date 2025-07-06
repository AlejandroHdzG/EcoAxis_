from rest_framework import serializers
from EcoAxis.models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        fields = '__all__'

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'

class ProductosEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model: ProductosEmpresas
        fields = '__all__'

class SucursalProductosEmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model: SucursalProductosEmpresas
        fields = '__all__'

class TipoTecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTecnico
        fields = '__all__'

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'

class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'

class SubscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscripcion
        fields = '__all__'

class ReciboCfeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReciboCfe
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'