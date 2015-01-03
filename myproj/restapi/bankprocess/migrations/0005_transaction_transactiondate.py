# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bankprocess', '0004_auto_20150103_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='TransactionDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 3, 13, 6, 56, 360955, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
