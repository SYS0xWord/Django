# Generated by Django 2.1.7 on 2019-02-20 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0002_facturaventa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resoluciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(db_column='Serie', max_length=45)),
                ('rangoi', models.IntegerField(db_column='RangoI')),
                ('nor', models.CharField(db_column='NoR', max_length=30)),
                ('fecha', models.DateTimeField(db_column='Fecha')),
                ('incremento', models.IntegerField(db_column='INCREMENTO')),
                ('rangof', models.IntegerField(db_column='RangoF')),
                ('activo', models.IntegerField(blank=True, db_column='Activo', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Resoluciones',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
                ('apellido', models.CharField(blank=True, db_column='Apellido', max_length=45, null=True)),
                ('usuario', models.CharField(blank=True, db_column='Usuario', max_length=45, null=True)),
                ('contraseña', models.CharField(blank=True, db_column='Contraseña', max_length=45, null=True)),
                ('privilegios', models.CharField(blank=True, db_column='Privilegios', max_length=45, null=True)),
                ('dpi', models.IntegerField(blank=True, db_column='DPI', null=True)),
                ('activo', models.IntegerField(blank=True, db_column='Activo', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Usuarios',
            },
        ),
    ]