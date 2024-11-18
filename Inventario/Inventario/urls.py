"""
URL configuration for Inventario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from InvoPro.views import index, productos, ingresar_producto, modificar_producto, eliminar_producto, departamentos, ingresar_departamento, modificar_departamento, eliminar_departamento, proveedores, ingresar_proveedor, modificar_proveedor, eliminar_proveedor, lotes, ingresar_lote, modificar_lote, eliminar_lote

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("productos/", productos),
    path("ingresar_producto/", ingresar_producto),
    path('modificar_producto/<int:id>', modificar_producto),
    path('eliminar_producto/<int:id>', eliminar_producto),
    path("departamentos/", departamentos),
    path("ingresar_departamento/", ingresar_departamento),
    path('modificar_departamento/<int:id>', modificar_departamento),
    path('eliminar_departamento/<int:id>', eliminar_departamento),
    path("proveedores/", proveedores),
    path("ingresar_proveedor/", ingresar_proveedor),
    path('modificar_proveedor/<int:id>', modificar_proveedor),
    path('eliminar_proveedor/<int:id>', eliminar_proveedor),
    path("lotes/", lotes),
    path("ingresar_lote/", ingresar_lote),
    path('modificar_lote/<int:id>', modificar_lote),
    path('eliminar_lote/<int:id>', eliminar_lote),
    
]
