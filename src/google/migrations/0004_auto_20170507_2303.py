# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0003_auto_20170430_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='google',
            name='client_secret',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='google',
            name='refresh_token',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
