# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0003_reportertoken_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporter',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
