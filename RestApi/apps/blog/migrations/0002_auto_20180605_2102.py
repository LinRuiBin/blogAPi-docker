# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-05 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artilcle',
            name='label',
        ),
        migrations.AddField(
            model_name='artilcle',
            name='label',
            field=models.ManyToManyField(related_name='articles', to='blog.Label', verbose_name='文章标签'),
        ),
    ]
