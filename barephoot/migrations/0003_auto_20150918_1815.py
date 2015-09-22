# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barephoot', '0002_auto_20150915_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movdata',
            name='price2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movdata',
            name='rating',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='restdata',
            name='price2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='restdata',
            name='rating',
            field=models.FloatField(),
        ),
    ]
