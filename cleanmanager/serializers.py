from rest_framework import serializers
from .models import Habitacion, Hotel, Empleado, AsignacionLimpieza

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

class ReporteHabitacionSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    habitaciones = HabitacionSerializer(many=True)
