from django.contrib import admin
from django.urls import path
from InvoPro.views import logout_view, login_view, index, productos, ingresar_producto, modificar_producto, eliminar_producto, departamentos, ingresar_departamento, modificar_departamento, eliminar_departamento, proveedores, ingresar_proveedor, modificar_proveedor, eliminar_proveedor, lotes, ingresar_lote, modificar_lote, eliminar_lote
from django.contrib.auth.decorators import login_required
from InvoPro.decorators import admin_required

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_required(index), name="index"),
    path("productos/", admin_required(productos), name="productos"),
    path("productos/ingresar_producto/", admin_required(ingresar_producto), name="ingresar_producto"),
    path('productos/modificar_producto/<int:id>', admin_required(modificar_producto), name="modificar_producto"),
    path('eliminar_producto/<int:id>', admin_required(eliminar_producto), name="eliminar_producto"),
    path("departamentos/", admin_required(departamentos), name="departamentos"),
    path("departamentos/ingresar_departamento/", admin_required(ingresar_departamento), name="ingresar_departamento"),
    path('departamentos/modificar_departamento/<int:id>', admin_required(modificar_departamento), name="modificar_departamento"),
    path('eliminar_departamento/<int:id>', admin_required(eliminar_departamento), name="eliminar_departamento"),
    path("proveedores/", admin_required(proveedores), name="proveedores"),
    path("proveedores/ingresar_proveedor/", admin_required(ingresar_proveedor), name="ingresar_proveedor"),
    path('proveedores/modificar_proveedor/<int:id>', admin_required(modificar_proveedor), name="modificar_proveedor"),
    path('eliminar_proveedor/<int:id>', admin_required(eliminar_proveedor), name="eliminar_proveedor"),
    path("lotes/", admin_required(lotes), name="lotes"),
    path("lotes/ingresar_lote/", admin_required(ingresar_lote), name="ingresar_lote"),
    path('lotes/modificar_lote/<int:id>', admin_required(modificar_lote), name="modificar_lote"),
    path('eliminar_lote/<int:id>', admin_required(eliminar_lote), name="eliminar_lote"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
]
