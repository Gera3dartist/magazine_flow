# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'db_table': 'reporters_reporter',
            },
        ),
        migrations.CreateModel(
            name='ReporterToken',
            fields=[
                ('key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'reporters_token',
            },
        ),
    ]
