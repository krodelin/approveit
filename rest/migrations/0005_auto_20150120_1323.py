# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='requestee',
            field=models.ForeignKey(related_name='requested_as_requestee', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='requester',
            field=models.ForeignKey(related_name='requested_by_requester', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
