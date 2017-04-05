# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0005_aws'),
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
        migrations.CreateModel(
            name='Google',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_id', models.CharField(max_length=120, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='IBM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_key', models.CharField(max_length=120, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rackspace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tenant_id', models.CharField(max_length=120, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='aws',
            name='account_id',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
