import uuid
from django.db import models


class Usuario(models.Model):
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email_user = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Empresa(models.Model):
    empresa_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nombre_empresa = models.CharField(max_length=150, unique=True)
    colonia_empresa = models.CharField(max_length=100)
    calle_empresa = models.CharField(max_length=100)
    codigo_postal_empresa = models.CharField(max_length=10)
    num_externo_empresa = models.CharField(max_length=5)
    num_interno_empresa = models.CharField(max_length=5, blank=True, null=True)
    rfc = models.CharField(max_length=13, unique=True)
    estado_empresa = models.CharField(max_length=25,
                                     choices=[('Mexicali', 'Mexicali'),
                                              ('Tijuana', 'Tijuana'),
                                              ('Ensenada', 'Ensenada'),
                                              ('Tecate', 'Tecate'),
                                              ('Playas de rosarito', 'Playas de rosarito')],
                                     default='Tijuana')
    telefono_empresa = models.CharField(max_length=10, unique=True)
    giro_empresa = models.CharField(max_length=100)
    tamano_empresa = models.CharField(max_length=25,
                                     choices=[('Grande', 'Grande'),
                                              ('Mediana', 'Mediana')],
                                     default='Mediana')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_empresa


class Catalogo(models.Model):
    producto_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nombre_producto = models.CharField(max_length=255, unique=True)
    marca_producto = models.CharField(max_length=50, unique=True)
    modelo_producto = models.CharField(max_length=50, unique=True)
    consumo_kw = models.DecimalField(decimal_places=5, max_digits=6)

    def __str__(self):
        return self.nombre_producto


class Sucursal(models.Model):
    sucursal_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nombre_sucursal = models.CharField(max_length=100, unique=True)
    colonia_sucursal = models.CharField(max_length=100)
    calle_sucursal = models.CharField(max_length=100)
    codigo_postal_sucursal = models.CharField(max_length=10)
    num_externo_sucursal = models.CharField(max_length=5)
    num_interno_sucursal = models.CharField(max_length=5, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_sucursal


class ProductosEmpresas(models.Model):
    prod_empresa_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    alias_producto = models.CharField(max_length=100)
    horas_uso_diario = models.FloatField()
    dias_uso_mensual = models.FloatField()
    ubicacion = models.CharField(max_length=100)
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='productos_empresariales')

    def __str__(self):
        return self.alias_producto


class SucursalProductosEmpresas(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    producto_empresa = models.ForeignKey(ProductosEmpresas, on_delete=models.CASCADE)


class TipoTecnico(models.Model):
    tipo_tecnico_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    rol_tecnico = models.CharField(max_length=50, choices=[
        ('Tecnico Superior', 'Tecnico Superior'),
        ('Tecnico Mantenimiento', 'Tecnico Mantenimiento')])

    def __str__(self):
        return self.rol_tecnico


class Tecnico(models.Model):
    tecnico_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nombre_tecnico = models.CharField(max_length=50)
    apellido_tecnico = models.CharField(max_length=50)
    correo_tecnico = models.CharField(max_length=150)
    telefono_tecnico = models.CharField(max_length=10)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo_tecnico = models.ForeignKey(TipoTecnico, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_tecnico} {self.apellido_tecnico}"


class Reporte(models.Model):
    reporte_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    reporte_consumo = models.FloatField()
    fecha_inicio_reporte = models.DateField()
    fecha_final_reporte = models.DateField()
    fecha_generacion_reporte = models.DateField(auto_now_add=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.empresa.nombre_empresa} - {self.reporte_consumo} kWh ({self.fecha_inicio_reporte} → {self.fecha_final_reporte})"


class Mantenimiento(models.Model):
    mantenimiento_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    fecha_mantenimiento = models.DateField()
    tipo_mantenimiento = models.CharField(max_length=100)
    estado_equipo = models.CharField(max_length=50, choices=[
        ('Excelente', 'Excelente'), ('Muy buena', 'Muy buena'),
        ('Regular', 'Regular'), ('Mala', 'Mala'), ('Muy mala', 'Muy mala')])
    proximo_mantenimiento = models.DateField()
    producto_empresa = models.ForeignKey(ProductosEmpresas, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto_empresa.alias_producto} - {self.tipo_mantenimiento}"


class Subscripcion(models.Model):
    subscripcion_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    fecha_pago = models.DateField()
    siguiente_pago = models.DateField()
    estatus_sub = models.BooleanField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.empresa.nombre_empresa} - {self.fecha_pago} → {self.siguiente_pago}"


class ReciboCfe(models.Model):
    recibo_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    periodo_factura_inicio = models.DateField()
    periodo_factura_final = models.DateField()
    indicador_consumo = models.CharField(max_length=100, choices=[
        ('Muy Bajo', 'Muy Bajo'), ('Bajo', 'Bajo'), ('Medio', 'Medio'),
        ('Alto', 'Alto'), ('Muy alto', 'Muy alto')])
    lectura_anterior = models.FloatField()
    lectura_actual = models.FloatField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sucursal.nombre_sucursal} ({self.lectura_anterior} → {self.lectura_actual})"


class Ticket(models.Model):
    ticket_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nombre_ticket = models.CharField(max_length=100)
    descripcion_ticket = models.CharField(max_length=256, null=True, blank=True)
    estado_ticket = models.BooleanField()
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_ticket} - Estado: {'Abierto' if self.estado_ticket else 'Cerrado'}"
