# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-01 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expenseapproval', '0005_expenses_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='Ammount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
