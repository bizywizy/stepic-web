# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 05:47
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='question',
            managers=[
                ('QuestionManager', django.db.models.manager.Manager()),
            ],
        ),
    ]