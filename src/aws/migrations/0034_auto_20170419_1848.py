# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0033_auto_20170417_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aws',
            name='user_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
