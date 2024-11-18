from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Departamento, Proveedor, Lote
from .forms import ProductoForm, DepartamentoForm, ProveedorForm, LoteForm
# Create your views here.
def index(request):
    return render(request, "index.html")

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

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

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return render(request, 'correcto.html', {
        'mensaje_exito': 'Producto eliminado correctamente!',
        'url_volver': '/productos'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
        })

# DEPARTAMENTOS

def departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos.html', {'departamentos': departamentos})

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

def eliminar_departamento(request, id):
    departamento = Departamento.objects.get(id=id)
    departamento.delete()
    return render(request, 'correcto.html', {
        'mensaje_exito': 'Departamento eliminado correctamente!',
        'url_volver': '/departamentos'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
        })

# PROVEEDORES

def proveedores(request):
    proveedores = Proveedor.objects.all()
    
    return render(request, 'proveedores.html', {'proveedores': proveedores})

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

def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    return render(request, 'correcto.html', {
        'mensaje_exito': 'Proveedor eliminado correctamente!',
        'url_volver': '/proveedores'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
        })
    
    
# LOTES
def lotes(request):
    lotes = Lote.objects.all()
    return render(request, 'lotes.html', {'lotes': lotes})

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

def eliminar_lote(request, id):
    lote = Lote.objects.get(id=id)
    lote.delete()
    return render(request, 'correcto.html', {
        'mensaje_exito': 'Lote eliminado correctamente!',
        'url_volver': '/lotes'  # Redirige a la página de noticias exitosa despues de la página de creación exitosa
        })