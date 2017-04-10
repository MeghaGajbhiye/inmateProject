# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0009_delete_azure'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Google',
        ),
        migrations.DeleteModel(
            name='IBM',
        ),
        migrations.DeleteModel(
            name='Rackspace',
        ),
    ]
