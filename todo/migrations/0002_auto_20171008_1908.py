# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('done', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='ToDoElements',
        ),
    ]
