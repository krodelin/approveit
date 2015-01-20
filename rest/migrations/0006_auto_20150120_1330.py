# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_auto_20150120_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='project',
            field=models.ForeignKey(related_name='requests', to='rest.Project'),
            preserve_default=True,
        ),
    ]
