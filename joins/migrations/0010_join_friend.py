# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0009_auto_20160312_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referral', to='joins.Join'),
        ),
    ]
