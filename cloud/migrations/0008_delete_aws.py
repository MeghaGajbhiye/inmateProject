# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0007_auto_20170405_1438'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AWS',
        ),
    ]
