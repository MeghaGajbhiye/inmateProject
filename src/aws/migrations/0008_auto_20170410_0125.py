# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0007_remove_aws_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aws',
            name='id',
            field=models.ForeignKey(primary_key=True, default=b'', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
