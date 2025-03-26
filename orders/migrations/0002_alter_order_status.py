# Generated by Django 5.1.6 on 2025-03-26 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pendiente'), ('in_preparation', 'En preparación'), ('ready', 'Listo para entregar'), ('cancelled', 'Cancelado')], default='pending', max_length=20),
        ),
    ]
