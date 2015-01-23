# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20150120_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='manager',
            field=models.ForeignKey(related_name='subordinates', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
