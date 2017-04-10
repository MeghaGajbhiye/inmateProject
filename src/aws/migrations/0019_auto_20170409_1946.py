# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0018_auto_20170409_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aws',
            old_name='user',
            new_name='user_id',
        ),
    ]
