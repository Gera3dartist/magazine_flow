# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0004_reporter_is_active'),
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(related_name='articles', to='reporter.Reporter'),
            preserve_default=True,
        ),
    ]
