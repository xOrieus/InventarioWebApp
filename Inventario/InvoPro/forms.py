from django import forms
from .models import Producto, Departamento, Proveedor, Lote

REGIONES = [
    ("", "Seleccione una región"),
    ('ARICA_PARINACOTA', 'XV Región de Arica y Parinacota'),
    ('TARAPACA', 'I Región de Tarapacá'),
    ('ANTOFAGASTA', 'II Región de Antofagasta'),
    ('ATACAMA', 'III Región de Atacama'),
    ('COQUIMBO', 'IV Región de Coquimbo'),
    ('VALPARAISO', 'V Región de Valparaíso'),
    ('METROPOLITANA', 'XIII Región Metropolitana de Santiago'),
    ('OHIGGINS', 'VI Región del Libertador General Bernardo O´Higgins'),
    ('MAULE', 'VII Región del Maule'),
    ('NUBLE', 'XVI Región de Ñuble'),
    ('BIOBIO', 'VIII Región del Biobío'),
    ('ARAUCANIA', 'IX Región de La Araucanía'),
    ('LOS_RIOS', 'XIV Región de Los Ríos'),
    ('LOS_LAGOS', 'X Región de Los Lagos'),
    ('AYSEN', 'XI Región de Aysén'),
    ('MAGALLANES', 'XII Región de Magallanes y la Antártica Chilena'),
]

TERMINOS_PAGO =[
    ('Efectivo', 'Efectivo'),
    ('Transferencia', 'Transferencia'),
    ('Debito', 'Débito'),
    ('Credito', 'Crédito'),
]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'descripcion', 'precio_costo', 'precio_venta', 'proveedor', 'departamento']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control','maxlength': '16', 'placeholder': 'Ingrese el código del producto'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del producto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingrese la descripción del producto'}),
            'precio_costo': forms.TextInput(attrs={'class': 'form-control','maxlength': '10', 'placeholder': 'Ingrese el precio costo'}),
            'precio_venta': forms.TextInput(attrs={'class': 'form-control','maxlength': '10', 'placeholder': 'Ingrese el precio venta'}),
            'proveedor': forms.Select(attrs={'class': 'form-select'}),
            'departamento': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def clean_codigo(self):
        codigo = self.cleaned_data.get("codigo")
        if len(codigo) > 16:
            raise forms.ValidationError("El código no puede tener más de 16 dígitos.")
        if not codigo.isdigit():
            raise forms.ValidationError("El código debe contener solo dígitos.")
        return codigo
    
    def clean_precio_costo(self):
        precio_costo = self.cleaned_data.get("precio_costo")
        if len(precio_costo) > 10:
            raise forms.ValidationError("El Precio Costo no puede tener más de 10 dígitos.")
        if not precio_costo.isdigit():
            raise forms.ValidationError("El Precio Costo debe contener solo dígitos.")
        return precio_costo
    
    def clean_precio_venta(self):
        precio_venta = self.cleaned_data.get("precio_venta")
        if len(precio_venta) > 10:
            raise forms.ValidationError("El Precio Venta no puede tener más de 10 dígitos.")
        if not precio_venta.isdigit():
            raise forms.ValidationError("El Precio Venta debe contener solo dígitos.")
        return precio_venta
    
class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['id_departamento', 'nombre']
        widgets = {
            'id_departamento': forms.TextInput(attrs={'class': 'form-control','maxlength': '16', 'placeholder': 'Ingrese el ID del departamento'}), 
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del departamento'}),
        }
        
    def clean_id_departamento(self):
        id_departamento = self.cleaned_data.get("id_departamento")
        if len(id_departamento) > 16:
            raise forms.ValidationError("El ID no puede tener más de 16 dígitos.")
        if not id_departamento.isdigit():
            raise forms.ValidationError("El ID debe contener solo dígitos.")
        return id_departamento
    
class ProveedorForm(forms.ModelForm):
    terminos_de_pago = forms.MultipleChoiceField(choices=TERMINOS_PAGO,widget=forms.CheckboxSelectMultiple, required=False , label="Términos de Pago")
    region = forms.ChoiceField(choices=REGIONES,widget=forms.Select(attrs={'class': 'form-control'}),label='Selecciona la región')
    class Meta:
        model = Proveedor
        fields = ['id_proveedor', 'nombre', 'calle', 'numero', 'ciudad', 'region', 'contacto', 'terminos_de_pago']
        widgets = {
            'id_proveedor': forms.TextInput(attrs={'class': 'form-control','maxlength': '16', 'placeholder': 'Ingrese el ID del proveedor'}), 
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del proveedor'}),
            'calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de la calle'}),
            'numero': forms.TextInput(attrs={'class': 'form-control','maxlength': '6', 'placeholder': 'Ingrese el número de domicilio'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Ingrese la ciudad'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control','minlength': '8','maxlength': '8', 'placeholder': 'Ingrese el contacto sin espacios'}),
        
        }
        
    def clean_id_proveedor(self):
        id_proveedor = self.cleaned_data.get("id_proveedor")
        if len(id_proveedor) > 16:
            raise forms.ValidationError("El ID no puede tener más de 16 dígitos.")
        if not id_proveedor.isdigit():
            raise forms.ValidationError("El ID debe contener solo dígitos.")
        return id_proveedor
    
    def clean_contacto(self):
        contacto = self.cleaned_data.get("contacto")
        if len(contacto) != 8:
            raise forms.ValidationError("El contacto debe tener exactamente 8 dígitos.")
        if not contacto.isdigit():
            raise forms.ValidationError("El contacto debe contener solo dígitos.")
        return contacto
    
    def clean_numero(self):
        numero = self.cleaned_data.get("numero")
        if len(numero) > 6:
            raise forms.ValidationError("El número de calle no puede tener más de 6 dígitos.")
        if not numero.isdigit():
            raise forms.ValidationError("El número de calle debe contener solo dígitos.")
        return numero
    
    def clean_terminos_pago(self):
        terminos_de_pago = self.cleaned_data.get('terminos_de_pago', [])
        return ', '.join(terminos_de_pago) if terminos_de_pago else ''
    
class LoteForm(forms.ModelForm):
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        to_field_name='nombre'  # Muestra solo el nombre del producto
    )
    class Meta:
        model = Lote
        fields = ['id_lote', 'producto', 'nombre', 'descripcion', 'fecha_vencimiento', 'fecha_fabricacion', 'cantidad_productos', 'cantidad_disponible']  
        widgets = {
            'id_lote': forms.TextInput(attrs={'class': 'form-control','maxlength': '16', 'placeholder': 'Ingrese el ID del lote'}), 
            
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del lote'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingrese la descripción del lote'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'fecha_fabricacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'cantidad_productos': forms.TextInput(attrs={'class': 'form-control' ,'maxlength': '10', 'placeholder': 'Ingrese la cantidad de productos'}),
            'cantidad_disponible': forms.TextInput(attrs={'class': 'form-control','maxlength': '10', 'placeholder': 'Ingrese la cantidad disponible'}),
        
        }
    
    def clean_id_lote(self):
        id_lote = self.cleaned_data.get("id_lote")
        if len(id_lote) > 16:
            raise forms.ValidationError("El ID no puede tener más de 16 dígitos.")
        if not id_lote.isdigit():
            raise forms.ValidationError("El ID debe contener solo dígitos.")
        return id_lote
    
    def clean_cantidad_productos(self):
        cantidad_productos = self.cleaned_data.get("cantidad_productos")
        if len(cantidad_productos) > 10:
            raise forms.ValidationError("La cantidad no puede tener más de 10 dígitos.")
        if not cantidad_productos.isdigit():
            raise forms.ValidationError("La cantidad debe contener solo dígitos.")
        return cantidad_productos
    
    def clean_cantidad_disponible(self):
        cantidad_disponible = self.cleaned_data.get("cantidad_disponible")
        if len(cantidad_disponible) > 10:
            raise forms.ValidationError("La cantidad no puede tener más de 10 dígitos.")
        if not cantidad_disponible.isdigit():
            raise forms.ValidationError("La cantidad debe contener solo dígitos.")
        return cantidad_disponible