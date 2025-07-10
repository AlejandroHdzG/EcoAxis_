from rest_framework import serializers
from .models import Empresa, Sucursal, ProductosEmpresas, SucursalProductosEmpresas

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'

class ProductosEmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosEmpresas
        fields = '__all__'

class SucursalProductosEmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = SucursalProductosEmpresas
        fields = '__all__'