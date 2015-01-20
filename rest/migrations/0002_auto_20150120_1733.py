# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='manager',
            field=models.ForeignKey(related_name='subordinates', blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
