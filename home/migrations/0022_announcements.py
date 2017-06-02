# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20170531_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('url', models.URLField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]