requisitos:

pip install django
pip install mysqlclient

la base de datos está en la raíz, llamado "inventario.sql"
debe estar ingresada la base de datos y ejecutar
1. py manage.py makemigrations
2. py manage.py migrate

si tienes un problema con las migrations
ve al directorio
InventarioWebApp\Inventario\InvoPro\migrations
y borra los archivos que empiezen con 000x con extensión .py y dentro
de la carpeta __pycache__ también no borrar los que dicen __init__.py
después intentar migrar de nuevo
