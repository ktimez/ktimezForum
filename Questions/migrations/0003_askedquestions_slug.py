# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 08:17
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0002_auto_20170824_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='askedquestions',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='title'),
        ),
    ]