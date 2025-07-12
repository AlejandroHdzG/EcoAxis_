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

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'email_user', 'password']
        # Optionally, you can make the password write-only
        # This prevents the password from being returned in responses
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = Usuario(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

