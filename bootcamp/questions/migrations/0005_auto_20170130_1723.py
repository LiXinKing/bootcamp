# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 09:23
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20170130_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='description',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='ansDescription'),
        ),
    ]
