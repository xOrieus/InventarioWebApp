from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Departamento, Proveedor, Lote
from .forms import ProductoForm, DepartamentoForm, ProveedorForm, LoteForm
from .decorators import admin_required 
from django.contrib.auth import authenticate, login, logout 
from django.urls import reverse 
from django.contrib import messages 
from django.utils.timezone import now 
from datetime import timedelta

# Create your views here.
#Los admin_requiered son para que solo los usuarios con permisos/logeados puedan acceder a las páginas

@admin_required
def index(request):
    #Obtiene los lotes y filtra los que están por vencer en 7 días o menos 
    lote_por_vencer = Lote.objects.filter(fecha_vencimiento__lte=now().date() + timedelta(days=7), fecha_vencimiento__gte=now().date()) 
     
    data = { 
        'lote_por_vencer': lote_por_vencer, 
    } 
     
    return render(request, "index.html", data)

@admin_required
def productos(request):
    productos = Producto.objects.all()
    buscar = None
    
    # Obtener la busqueda ingresada
    termino = request.GET.get('termino', '')
    tipo_busqueda = request.GET.get('tipo', 'codigo')  # Por defecto busca por código
    
    if termino:
        try:
            if tipo_busqueda == 'codigo':
                buscar = Producto.objects.get(codigo=termino)
            else:  # si el tipo de busqueda es por código, lo realiza, si no, es por nombre
                # icontains para busqueda con mayusculas 
                buscar = Producto.objects.filter(nombre__icontains=termino).first()
        except Producto.DoesNotExist:
            buscar = None
    
    return render(request, 'productos.html', {
        'productos': productos,
        'buscar': buscar,
        'termino': termino,
        'tipo_busqueda': tipo_busqueda
    })

@admin_required
def ingresar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'correcto.html', {
                'mensaje_exito': '¡Producto ingresado correctamente!',
                'url_volver': '/productos'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
            })
    else:
        form = ProductoForm()
    return render(request, 'ingresar_producto.html', {'form': form})

@admin_required
def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    form = ProductoForm(instance=producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return render(request, 'correcto.html', {
            'mensaje_exito': 'Producto modificado correctamente!',
            'url_volver': '/productos'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
            })
    data={
        'form':form,
        'editar': True
    }
    return render(request,'ingresar_producto.html', data)

@admin_required
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return render(request, 'correcto.html', {
        'mensaje_exito': 'Producto eliminado correctamente!',
        'url_volver': '/productos'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
        })

# DEPARTAMENTOS

@admin_required
def departamentos(request):
    departamentos = Departamento.objects.all()
    buscar = None
    
    # Obtener la busqueda ingresada
    termino = request.GET.get('termino', '')
    tipo_busqueda = request.GET.get('tipo', 'id_departamento')  # Por defecto busca por id
    
    if termino:
        try:
            if tipo_busqueda == 'id_departamento':
                buscar = Departamento.objects.get(id_departamento=termino)
            else:  # si el tipo de busqueda es por ID, lo realiza, si no, es por nombre
                # icontains para busqueda con mayusculas 
                buscar = Departamento.objects.filter(nombre__icontains=termino).first()
        except Departamento.DoesNotExist:
            buscar = None
    
    return render(request, 'departamentos.html', {
        'departamentos': departamentos,
        'buscar': buscar,
        'termino': termino,
        'tipo_busqueda': tipo_busqueda
    })

@admin_required
def ingresar_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'correcto.html', {
                'mensaje_exito': '¡Departamento ingresado correctamente!',
                'url_volver': '/departamentos'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
            })
    else:
        form = DepartamentoForm()
    return render(request, 'ingresar_departamento.html', {'form': form})

@admin_required
def modificar_departamento(request, id):
    departamento = Departamento.objects.get(id=id)
    form = DepartamentoForm(instance=departamento)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
        return render(request, 'correcto.html', {
            'mensaje_exito': 'Departamento modificado correctamente!',
            'url_volver': '/departamentos'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
            })
    data={
        'form':form,
        'editar': True
    }
    return render(request,'ingresar_departamento.html', data)

@admin_required
def eliminar_departamento(request, id):
    departamento = Departamento.objects.get(id=id)
    departamento.delete()
    return render(request, 'correcto.html', {
        'mensaje_exito': 'Departamento eliminado correctamente!',
        'url_volver': '/departamentos'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
        })

# PROVEEDORES

@admin_required
def proveedores(request):
    proveedores = Proveedor.objects.all()
    buscar = None
    
    # Obtener la busqueda ingresada
    termino = request.GET.get('termino', '')
    tipo_busqueda = request.GET.get('tipo', 'id_proveedor')  # Por defecto busca por id
    
    if termino:
        try:
            if tipo_busqueda == 'id_proveedor':
                buscar = Proveedor.objects.get(id_proveedor=termino)
            else:  # si el tipo de busqueda es por ID, lo realiza, si no, es por nombre
                # icontains para busqueda con mayusculas 
                buscar = Proveedor.objects.filter(nombre__icontains=termino).first()
        except Proveedor.DoesNotExist:
            buscar = None
    
    return render(request, 'proveedores.html', {
        'proveedores': proveedores,
        'buscar': buscar,
        'termino': termino,
        'tipo_busqueda': tipo_busqueda
    })

@admin_required
def ingresar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor = form.save(commit=False)
            proveedor.terminos_de_pago = form.cleaned_data['terminos_de_pago']
            proveedor.save()
            return render(request, 'correcto.html', {
                'mensaje_exito': '¡Proveedor ingresado correctamente!',
                'url_volver': '/proveedores'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
            })
    else:
        form = ProveedorForm()
    return render(request, 'ingresar_proveedor.html', {'form': form})

@admin_required
def modificar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    form = ProveedorForm(instance=proveedor)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return render(request, 'correcto.html', {
                'mensaje_exito': 'Proveedor modificado correctamente!',
                'url_volver': '/proveedores'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
                })
    data={
        'form':form,
        'editar': True
    }
    return render(request,'ingresar_proveedor.html', data)

@admin_required
def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    return render(request, 'correcto.html', {
        'mensaje_exito': 'Proveedor eliminado correctamente!',
        'url_volver': '/proveedores'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
        })
    
    
# LOTES
@admin_required
def lotes(request):
    lotes = Lote.objects.all()
    return render(request, 'lotes.html', {'lotes': lotes})

@admin_required
def ingresar_lote(request):
    if request.method == 'POST':
        form = LoteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'correcto.html', {
                'mensaje_exito': '¡Lote ingresado correctamente!',
                'url_volver': '/lotes'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
            })
    else:
        form = LoteForm()
    return render(request, 'ingresar_lote.html', {'form': form})

@admin_required
def modificar_lote(request, id):
    lote = Lote.objects.get(id=id)
    form = LoteForm(instance=lote)
    if request.method == 'POST':
        form = LoteForm(request.POST, instance=lote)
        if form.is_valid():
            form.save()
        return render(request, 'correcto.html', {
            'mensaje_exito': 'Lote modificado correctamente!',
            'url_volver': '/lotes'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
            })
    data={
        'form':form,
        'editar': True
    }
    return render(request,'ingresar_lote.html', data)

@admin_required
def eliminar_lote(request, id):
    lote = Lote.objects.get(id=id)
    lote.delete()
    return render(request, 'correcto.html', {
        'mensaje_exito': 'Lote eliminado correctamente!',
        'url_volver': '/lotes'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
        })

#LOGIN

def login_view(request): 
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password) 
        if user is not None and (user.is_staff or user.is_superuser): 
            login(request, user) 
            return redirect(reverse('index'))  
        else: 
            return render(request, 'login.html', {'error': 'Credenciales inválidas o usuario no autorizado'}) 
    return render(request, 'login.html') 
 
def logout_view(request): 
    logout(request) 
    messages.success(request, 'Has cerrado sesión exitosamente.') 
    return redirect('login') 