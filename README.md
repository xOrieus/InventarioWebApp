Para instalar los requerimientos

```
pip install -r requirements.txt
```

Iniciar base de datos antes de seguir

Para crear un usuario

```
py manage.py createsuperuser
```

colocar datos

```
admin
admin
admin@admin.cl
admin
```

requisitos:
```
pip install django
pip install mysqlclient
pip install django-auto-logout
```

la base de datos está en la raíz, llamado "inventario.sql"
debe estar ingresada la base de datos y ejecutar
```
py manage.py makemigrations
py manage.py migrate
```
si tienes un problema con las migrations
ve al directorio
InventarioWebApp\Inventario\InvoPro\migrations
y borra los archivos que empiezen con 000x con extensión .py y dentro
de la carpeta __ pycache __ también no borrar los que dicen __ init__.py
después intentar migrar de nuevo
