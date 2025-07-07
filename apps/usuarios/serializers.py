from rest_framework import serializers
from .models import Usuario, TipoTecnico, Tecnico

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'email_user', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user

class TipoTecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTecnico
        fields = '__all__'

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'