# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_auto_20150306_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='refresh_token',
            field=models.CharField(null=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='token',
            field=models.CharField(null=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_external_reference',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
