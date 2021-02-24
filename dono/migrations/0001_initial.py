# Generated by Django 3.1.7 on 2021-02-22 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0002_remove_empresas_dono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=100)),
                ('empresa', models.ManyToManyField(to='empresas.Empresas')),
            ],
            options={
                'db_table': 'dono',
                'managed': True,
            },
        ),
    ]
