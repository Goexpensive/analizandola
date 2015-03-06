# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('last_modified_date', models.DateField()),
                ('buyer', models.PositiveIntegerField()),
                ('transaction_id', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=255)),
                ('status_detail', models.CharField(max_length=255)),
                ('transaction_type', models.CharField(max_length=255)),
                ('marketplace', models.CharField(max_length=255)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=3)),
                ('user_id', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
