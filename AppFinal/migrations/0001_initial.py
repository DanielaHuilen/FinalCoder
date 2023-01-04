# Generated by Django 4.1.3 on 2023-01-03 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('antiguedad', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('materia', models.ManyToManyField(to='AppFinal.materia')),
            ],
        ),
        migrations.CreateModel(
            name='TrabajoPractico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('archivo', models.FileField(upload_to='')),
                ('datos', models.DateTimeField(auto_now_add=True)),
                ('materia', models.ManyToManyField(to='AppFinal.materia')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppFinal.profesores')),
            ],
        ),
    ]
