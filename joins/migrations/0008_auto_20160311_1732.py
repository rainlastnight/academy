# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0007_auto_20160311_1730'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='join',
            unique_together=set([('email', 'ref_id')]),
        ),
    ]
