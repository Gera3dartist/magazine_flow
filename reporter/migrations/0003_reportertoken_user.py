# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0002_auto_20170114_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportertoken',
            name='user',
            field=models.ForeignKey(related_name='reporter', to='reporter.Reporter'),
            preserve_default=True,
        ),
    ]
