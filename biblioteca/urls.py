from django.urls import path
from . import views

urlpatterns = [
    
    path('/empleados/desactivar/<int:id>', views.desactivar_Registro_Empleado, name='desactivar_Registro_Empleado'),
    path('empleados_listado/', views.listado_empleados, name="listado_empleados"),
]