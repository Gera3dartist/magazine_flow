# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporter',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reporter',
            name='password',
            field=models.CharField(verbose_name='password', max_length=128, default=datetime.datetime(2017, 1, 14, 13, 41, 36, 808791, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
