# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-11 05:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0007_auto_20181220_1509'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-posted_on']},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-posted_on']},
        ),
    ]