# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-07 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_suggestion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Suggestion',
        ),
    ]