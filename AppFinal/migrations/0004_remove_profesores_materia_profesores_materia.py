# Generated by Django 4.1.3 on 2023-01-06 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0003_remove_trabajopractico_datos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesores',
            name='materia',
        ),
        migrations.AddField(
            model_name='profesores',
            name='materia',
            field=models.CharField(default='Desconocido', max_length=50),
        ),
    ]
