# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('project', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='projects',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myportfolio.Editor'),
        ),
    ]
