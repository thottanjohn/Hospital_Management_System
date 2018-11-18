# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-18 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_auto_20181113_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurses',
            name='department_num',
            field=models.ForeignKey(db_column='department_num', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='hospital.Department'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='nurses',
            unique_together=set([('department_num', 'nurse_id')]),
        ),
    ]
