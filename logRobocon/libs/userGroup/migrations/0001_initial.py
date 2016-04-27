# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('accountName', models.CharField(max_length=20)),
                ('emailAddr', models.EmailField(max_length=50)),
                ('userPasswd', models.CharField(max_length=20)),
            ],
        ),
    ]
