# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-01 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expenseapproval', '0004_expenses_employee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
