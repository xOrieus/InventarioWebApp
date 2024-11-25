# Generated by Django 5.0.7 on 2024-11-25 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("InvoPro", "0002_alter_producto_precio_costo_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="producto",
            name="precio_costo",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="producto",
            name="precio_venta",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]