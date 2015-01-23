# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_auto_20150120_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personrequest',
            name='status',
            field=django_fsm.FSMField(default='pending', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personrequest',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
    ]
