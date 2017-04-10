# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0013_auto_20170409_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aws',
            old_name='id',
            new_name='user_id',
        ),
    ]
