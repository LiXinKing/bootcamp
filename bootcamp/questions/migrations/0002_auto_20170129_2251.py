# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 14:51
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='Description'),
        ),
    ]
