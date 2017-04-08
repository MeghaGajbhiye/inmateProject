# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aws', '0005_auto_20170407_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='aws',
            name='user',
            field=models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL),
        ),
    ]
