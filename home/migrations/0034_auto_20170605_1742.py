# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-05 12:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_innovation_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='innovation',
            old_name='Location',
            new_name='location',
        ),
    ]
