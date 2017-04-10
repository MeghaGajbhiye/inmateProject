# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0006_aws_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aws',
            name='user',
        ),
    ]
