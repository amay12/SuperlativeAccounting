# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-13 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0003_item_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='tax',
            name='username',
            field=models.CharField(default='amaykadre', max_length=50),
            preserve_default=False,
        ),
    ]
