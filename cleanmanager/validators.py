from django.core.exceptions import ValidationError
import re


# Validador para nombres
def validar_nombre(value):
    if not re.match("^[a-zA-Z]*$", value):
        raise ValidationError("El nombre solo debe contener caracteres")

# Validador para numeros
def validar_numero(value):
    if not re.match(r'^\d+$', value):
        raise ValidationError("El campo solo debe contener números")

# Validador para nombres
def validar_nombre(value):
    if not re.match("^[a-zA-Z]*$", value):
        raise ValidationError("El nombre solo debe contener caracteres")

# Validador para el numero de habitaciones    
def validar_habitaciones(value):
    if value > 500:
        raise ValidationError("El número de habitaciones no puede ser mayor a 500")

# Validador para el teléfono
def validar_telefono(value):
    if not re.match(r'^\d{10}$', value):
        raise ValidationError("El número de teléfono debe tener exactamente 10 dígitos.")
