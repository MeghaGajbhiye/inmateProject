# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0023_auto_20170410_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aws',
            name='user_id',
            field=models.CharField(max_length=120, serialize=False, primary_key=True, blank=True),
        ),
    ]
