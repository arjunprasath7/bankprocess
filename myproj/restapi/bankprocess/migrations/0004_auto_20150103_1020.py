# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankprocess', '0003_auto_20150103_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='userId',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]
