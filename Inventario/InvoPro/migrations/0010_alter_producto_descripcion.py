# Generated by Django 5.0.7 on 2024-11-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("InvoPro", "0009_alter_producto_descripcion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="producto",
            name="descripcion",
            field=models.TextField(blank=True),
        ),
    ]