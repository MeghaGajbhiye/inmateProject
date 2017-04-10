# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0016_auto_20170409_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aws',
            old_name='user_id',
            new_name='user',
        ),
    ]
