# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0003_auto_20170221_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default=datetime.datetime(2017, 3, 1, 4, 44, 47, 320000, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
