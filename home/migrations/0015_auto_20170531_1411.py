# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20170531_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovation',
            name='image',
            field=models.FileField(default='static/home/images/hbnlogo.png', upload_to=''),
        ),
    ]
