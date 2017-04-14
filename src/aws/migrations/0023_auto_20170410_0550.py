# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0022_auto_20170409_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aws',
            name='user_id',
            field=models.OneToOneField(primary_key=True, default=b'', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
