from django.contrib import admin
from .models import Hotel, Empleado, Habitacion, AsignacionLimpieza

# Register your models here.

class HotelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'num_habitaciones')

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'email', 'telefono')
    search_fields = ('nombre',)
    ordering = ('nombre', 'fecha_contratacion',)

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero_habitacion', 'tipo_habitacion', 'piso', 'tiempo_limpieza')
    list_filter = ('piso', )
    search_fields = ('numero_habitacion','tipo_habitacion',)
    ordering = ('numero_habitacion', 'piso', 'tipo_habitacion',)

class AsignacionLimpiezaAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'habitacion', 'estado', 'fecha_creado', 'fecha_modificado',)
    list_filter = ('estado', 'fecha_creado', 'fecha_modificado',)
    search_fields = ('empleado__nombre', 'habitacion__numero_habitacion')
    ordering = ('fecha_modificado',)

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(AsignacionLimpieza, AsignacionLimpiezaAdmin)