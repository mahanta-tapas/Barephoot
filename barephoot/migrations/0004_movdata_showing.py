# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barephoot', '0003_auto_20150918_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='movdata',
            name='showing',
            field=models.CharField(default='nothing', max_length=200),
            preserve_default=False,
        ),
    ]
