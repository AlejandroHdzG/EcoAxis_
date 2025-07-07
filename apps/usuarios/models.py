import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.utils import timezone

class Usuario(AbstractBaseUser, PermissionsMixin):
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email_user = models.EmailField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email_user'
    REQUIRED_FIELDS = ['nombres', 'apellidos']

    objects = UserManager()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        db_table = 'usuario'

class TipoTecnico(models.Model):
    tipo_tecnico_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    rol_tecnico = models.CharField(max_length=50, choices=[
        ('Tecnico Superior', 'Tecnico Superior'),
        ('Tecnico Mantenimiento', 'Tecnico Mantenimiento')])

    def __str__(self):
        return self.rol_tecnico

    class Meta:
        db_table = 'tipo_tecnico'

class Tecnico(models.Model):
    tecnico_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nombre_tecnico = models.CharField(max_length=50)
    apellido_tecnico = models.CharField(max_length=50)
    correo_tecnico = models.CharField(max_length=150)
    telefono_tecnico = models.CharField(max_length=10)
    sucursal = models.ForeignKey('empresas.Sucursal', on_delete=models.CASCADE)
    empresa = models.ForeignKey('empresas.Empresa', on_delete=models.CASCADE)
    tipo_tecnico = models.ForeignKey(TipoTecnico, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_tecnico} {self.apellido_tecnico}"

    class Meta:
        db_table = 'tecnico'

