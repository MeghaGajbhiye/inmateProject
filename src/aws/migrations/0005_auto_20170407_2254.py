# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0004_delete_awshome'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aws',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='aws',
            table='aws',
        ),
    ]
