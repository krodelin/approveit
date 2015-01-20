# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0006_auto_20150120_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='requestee',
            field=models.ForeignKey(related_name='requestee_requests', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='requester',
            field=models.ForeignKey(related_name='requester_requests', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
