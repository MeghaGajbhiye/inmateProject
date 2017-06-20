# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ORACLEModel',
            fields=[
                ('user_id', models.IntegerField(serialize=False, primary_key=True)),
                ('oracle_name', models.CharField(max_length=120, null=True, blank=True)),
                ('oracle_password', models.CharField(max_length=120, null=True, blank=True)),
                ('oracle_domain_name', models.CharField(max_length=120, null=True, blank=True)),
            ],
        ),
    ]
