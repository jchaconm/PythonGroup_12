# Generated by Django 2.0.7 on 2019-09-21 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lector',
            name='address',
            field=models.CharField(max_length=50, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='lector',
            name='bdate',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='lector',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='lector',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='lector',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]
