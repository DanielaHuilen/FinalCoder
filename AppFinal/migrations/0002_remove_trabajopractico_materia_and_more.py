# Generated by Django 4.1.3 on 2023-01-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajopractico',
            name='materia',
        ),
        migrations.AddField(
            model_name='trabajopractico',
            name='materia',
            field=models.CharField(default='Desconocido', max_length=50),
        ),
    ]
