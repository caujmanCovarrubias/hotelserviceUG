from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Hotel, Empleado, Habitacion, AsignacionLimpieza
from .serializers import ReporteHabitacionSerializer, EmpleadoSerializer, HotelSerializer, HabitacionSerializer
from rest_framework import viewsets, generics
 
# Create your views here.
def contact(request, name):
    return HttpResponse(f"Bienvenido {name} al sistema...")

def hello(request):
    return HttpResponse("<h1>hello world<h1>")

def about(request):
    return HttpResponse("About")

def hoteles(request):
    hoteles = Hotel.objects.all()
    return render(request, "form_hoteles.html", {"hoteles": hoteles})

def empleados(request):
    empleados = list(Empleado.objects.values())
    return JsonResponse(empleados, safe=False)

@api_view(['GET'])
def hoteles_count(request):
    try:
        cantidad = Hotel.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )

@api_view(['GET'])
def reporte_habitaciones(request):
    try:
        habitaciones = Habitacion.objects.all()
        cantidad = habitaciones.count()
        return JsonResponse(
            ReporteHabitacionSerializer({
                "cantidad": cantidad,
                "habitaciones": habitaciones
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )
    
class EmpleadoCreateView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

 