# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='head',
            field=models.BooleanField(default=False),
        ),
    ]
