# Generated by Django 4.1.7 on 2023-04-08 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_alter_mensajes_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='Cliente',
        ),
    ]