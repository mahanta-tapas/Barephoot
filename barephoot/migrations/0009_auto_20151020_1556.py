# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barephoot', '0008_auto_20151007_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='placestovisit',
            name='rating',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placestovisit',
            name='review_count',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
