# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0004_signup_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='AWS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aws_access_key', models.CharField(max_length=120, null=True, blank=True)),
                ('aws_secret_key', models.CharField(max_length=120, null=True, blank=True)),
            ],
        ),
    ]
