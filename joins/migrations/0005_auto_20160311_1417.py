# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0004_auto_20160309_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='email',
            field=models.EmailField(max_length=254, unique=False),
        ),
    ]
