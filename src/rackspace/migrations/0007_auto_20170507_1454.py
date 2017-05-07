# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rackspace', '0006_auto_20170430_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rackspace',
            old_name='tenant_id',
            new_name='api_key',
        ),
        migrations.AddField(
            model_name='rackspace',
            name='username',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
