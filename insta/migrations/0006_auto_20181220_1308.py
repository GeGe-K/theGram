# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-20 10:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_auto_20181219_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(null='false', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
