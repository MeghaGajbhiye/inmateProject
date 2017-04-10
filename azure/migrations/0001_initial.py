# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Azure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enrollment_number', models.CharField(max_length=120, null=True, blank=True)),
                ('api_key', models.CharField(max_length=120, null=True, blank=True)),
            ],
        ),
    ]
