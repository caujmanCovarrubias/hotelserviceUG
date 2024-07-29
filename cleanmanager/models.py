from django.db import models
from . import validators
from django.utils import timezone

# Create your models here.

# Hoteles
class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    num_habitaciones =  models.IntegerField(validators=[validators.validar_habitaciones])

    def __str__(self):
        return self.nombre

# Empleados
class Empleado(models.Model):
    dni = models.CharField(max_length=20,validators=[validators.validar_numero], default='')
    nombre = models.CharField(max_length=100,validators=[validators.validar_nombre])
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=10,validators=[validators.validar_telefono])
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre

class TipoHabitacion(models.TextChoices):
    SIMPLE = 'simple', 'habitacion francesa'
    DOBLE = 'doble', 'habitacion doble'
    TRIPLE = 'triple', 'habitacion triple'
    CUADRUPLE = 'cuadruple', 'habitacion familiar'

class EstadoHabitacion(models.TextChoices):
    LIBRE = 'libre', 'habitacion libre'
    OCUPADA = 'ocupada', 'habitacion ocupada'

# Habitaciones
class Habitacion(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='habitaciones')
    numero_habitacion = models.CharField(max_length=10, unique=True)
    tipo_habitacion = models.CharField(
        max_length=20,
        choices=TipoHabitacion.choices,
        default=TipoHabitacion.SIMPLE
        )
    estado_habitacion = models.CharField(
        max_length=20,
        choices=EstadoHabitacion.choices,
        default=EstadoHabitacion.LIBRE
    )
    piso = models.IntegerField()
    tiempo_limpieza = models.IntegerField()

    def __str__(self):
        return f"{self.numero_habitacion} - {self.tipo_habitacion}"

class EstadoLimpieza(models.TextChoices):
    PENDIENTE = 'pendiente', 'limpieza pendiente'
    PROCESO = 'enproceso', 'limpieza en proceso'
    COMPLETADA = 'completada', 'limpieza completada'
    CANCELADA = 'cancelada', 'limpieza cancelada'

# Modelo para las Asignaciones de Limpieza
class AsignacionLimpieza(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='asignaciones')
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='asignaciones')
    estado = models.CharField(
        max_length=20,
        choices=EstadoLimpieza.choices,
        default=EstadoLimpieza.PENDIENTE
    )
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_modificado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.empleado.nombre} - {self.habitacion.numero_habitacion} - {self.fecha_asignacion}"