# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 09:28
from __future__ import unicode_literals

import blog.code_markdown_blocks
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_blogpage_code_block'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='code_block',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='code_md_block',
            field=wagtail.wagtailcore.fields.StreamField([('code_block', wagtail.wagtailcore.blocks.StructBlock([(b'language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'python', b'Python'), (b'bash', b'Bash/Shell'), (b'html', b'HTML'), (b'css', b'CSS'), (b'scss', b'SCSS')])), (b'code', wagtail.wagtailcore.blocks.TextBlock())])), ('md_block', blog.code_markdown_blocks.MarkDownBlock())], default=''),
            preserve_default=False,
        ),
    ]
