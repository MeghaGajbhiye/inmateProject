# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0008_delete_aws'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Azure',
        ),
    ]
