# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0006_auto_20170320_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ibm',
            old_name='access_key',
            new_name='api_key',
        ),
    ]
