from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('contact/<str:name>/', views.contact, name='contact'),
    path('hoteles/', views.hoteles, name='hoteles'),
    path('hoteles/cantidad/', views.hoteles_count),

    path('empleados/', views.empleados),
    path('empleados2/', views.EmpleadoCreateView.as_view(), name='empleados2'),
    path('habitaciones/reporte/', views.reporte_habitaciones, name='reporte_habitaciones'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.hello),
    path('about/', views.about)
]