# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moderator', '0002_auto_20170114_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='moderatortoken',
            name='user',
            field=models.ForeignKey(related_name='reporter', to='moderator.Moderator'),
            preserve_default=True,
        ),
    ]
