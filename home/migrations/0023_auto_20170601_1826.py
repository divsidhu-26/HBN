# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_announcements'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Announcements',
            new_name='Announcement',
        ),
    ]
