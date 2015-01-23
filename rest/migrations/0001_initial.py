# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('notes', models.TextField()),
                ('status', django_fsm.FSMField(default=b'pending', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('notes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manager', models.ForeignKey(related_name='subordinates', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='personrequest',
            name='project',
            field=models.ForeignKey(related_name='requests', to='rest.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personrequest',
            name='requestee',
            field=models.ForeignKey(related_name='requestee_requests', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personrequest',
            name='requester',
            field=models.ForeignKey(related_name='requester_requests', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
