# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azure', '0005_auto_20170409_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='azure',
            old_name='api_key',
            new_name='client_id',
        ),
        migrations.RenameField(
            model_name='azure',
            old_name='enrollment_number',
            new_name='secret_key',
        ),
        migrations.AddField(
            model_name='azure',
            name='subscription_id',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='azure',
            name='tenant_id',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
