from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=16, unique=True)
    nombre = models.CharField(max_length=100)
    precio_costo = models.CharField(max_length=10)
    descripcion = models.TextField(blank=True)
    precio_venta = models.CharField(max_length=10)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
class Proveedor(models.Model):
    REGIONES = [
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
    
    id_proveedor = models.CharField(max_length=16, unique=True)
    nombre = models.CharField(max_length=100)
    calle = models.CharField(max_length=30)
    numero = models.CharField(max_length=6)
    ciudad = models.CharField(max_length=30)
    region = models.CharField(max_length=50, choices=REGIONES)
    contacto = models.CharField(max_length=50)
    terminos_de_pago = models.TextField(help_text='Seleccione el tipo de pago')
    
    def __str__(self):
        return f"{self.id_proveedor} - {self.nombre}"
    
    def get_terminos_de_pago_display(self):
        # Convertir el texto almacenado en lista y unirlo por comas para mostrarlo de forma correcta
        return ", ".join(eval(self.terminos_de_pago))

class Departamento(models.Model):
    id_departamento = models.CharField(max_length=16, unique=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id_departamento} - {self.nombre}"

class Lote(models.Model):
    id_lote = models.CharField(max_length=16, unique=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_vencimiento = models.DateField()
    fecha_fabricacion = models.DateField()
    cantidad_productos = models.CharField(max_length=10)
    cantidad_disponible = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.id_lote} - {self.nombre}"
