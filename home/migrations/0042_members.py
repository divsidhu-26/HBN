# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-06 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
