# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0034_auto_20170419_1848'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AWS',
            new_name='AWSModel',
        ),
    ]
