# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tax_Name', models.CharField(max_length=50)),
                ('Tax_Rate', models.CharField(max_length=4)),
            ],
        ),
    ]
