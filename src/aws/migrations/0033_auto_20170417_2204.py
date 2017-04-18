# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0032_remove_aws_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aws',
            name='user_id',
            field=models.IntegerField(serialize=False, primary_key=True, blank=True),
        ),
    ]
