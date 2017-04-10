# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0002_awshome'),
    ]

    operations = [
        migrations.AddField(
            model_name='awshome',
            name='aws_zone',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
