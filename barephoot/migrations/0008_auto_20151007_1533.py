# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barephoot', '0007_events_placestovisit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placestovisit',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
