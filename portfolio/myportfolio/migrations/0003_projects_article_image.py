# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_auto_20180503_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='projects/'),
        ),
    ]
