# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-21 07:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('contact_number', models.CharField(blank=True, max_length=10, null=True)),
                ('grade', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'doctors',
            },
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hospital.Doctors')),
            ],
            options={
                'db_table': 'emergency',
            },
        ),
        migrations.CreateModel(
            name='Nurses',
            fields=[
                ('nurse_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nurses',
            },
        ),
        migrations.AddField(
            model_name='emergency',
            name='nurse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hospital.Nurses'),
        ),
    ]
