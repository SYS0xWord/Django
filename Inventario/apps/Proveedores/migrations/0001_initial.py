# Generated by Django 2.1.7 on 2019-03-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrev', models.CharField(blank=True, db_column='NombreV', max_length=45, null=True)),
                ('representante', models.CharField(blank=True, db_column='Representante', max_length=45, null=True)),
                ('nit', models.CharField(blank=True, db_column='Nit', max_length=45, null=True)),
                ('direccion', models.CharField(blank=True, db_column='Direccion', max_length=200, null=True)),
                ('numero', models.IntegerField(blank=True, db_column='Numero', null=True)),
                ('correo', models.CharField(blank=True, db_column='Correo', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Proveedor',
                'managed': False,
            },
        ),
    ]
