# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-12 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('dpi', models.CharField(max_length=20)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('fecha_egreso', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('0', 'sencillas'), ('1', 'dobles')], default='0', max_length=1)),
                ('descripcion', models.CharField(max_length=150)),
                ('numero', models.IntegerField()),
                ('ocupado', models.BooleanField(default=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Fotografia de referencia')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analisisApp.habitacion'),
        ),
    ]
