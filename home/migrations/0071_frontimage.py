# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-08 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0070_meetprof_prof_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(height_field='height_field', upload_to=home.models.upload_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('detail', models.CharField(max_length=75)),
            ],
        ),
    ]
