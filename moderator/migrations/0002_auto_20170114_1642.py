# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('moderator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moderator',
            name='last_login',
        ),
        migrations.AddField(
            model_name='moderator',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='moderator',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterModelTable(
            name='moderator',
            table='moderators_moderator',
        ),
        migrations.AlterModelTable(
            name='moderatortoken',
            table='moderators_token',
        ),
    ]
