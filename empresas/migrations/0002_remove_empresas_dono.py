# Generated by Django 3.1.7 on 2021-02-22 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresas',
            name='dono',
        ),
    ]
