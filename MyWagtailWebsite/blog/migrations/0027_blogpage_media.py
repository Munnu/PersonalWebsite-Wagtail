# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 10:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmedia', '0003_copy_media_permissions_to_collections'),
        ('blog', '0026_auto_20170730_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='media',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
    ]
