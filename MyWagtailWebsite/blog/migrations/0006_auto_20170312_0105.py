# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-12 01:05
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170312_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
