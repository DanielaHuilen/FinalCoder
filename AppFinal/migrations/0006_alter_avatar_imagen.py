# Generated by Django 4.1.3 on 2023-01-09 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0005_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(upload_to='media/avatares'),
        ),
    ]
