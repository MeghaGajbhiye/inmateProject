# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azure', '0007_auto_20170430_1601'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='azure',
            table='azure_azure',
        ),
    ]
