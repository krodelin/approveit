# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('notes', models.TextField()),
                ('project', models.ForeignKey(to='rest.Project')),
                ('requestee', models.ForeignKey(related_name='requested_as_requestee', to='rest.Employee')),
                ('requester', models.ForeignKey(related_name='requested_by_requester', to='rest.Employee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
