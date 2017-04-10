# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0003_awshome_aws_zone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AWSHome',
        ),
    ]
