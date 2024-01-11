# Generated by Django 2.2 on 2024-01-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Servicio')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='services/', verbose_name='Imagen')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
