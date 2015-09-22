# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barephoot', '0005_auto_20150920_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movdata',
            name='movie_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movdata',
            name='theatre',
            field=models.CharField(max_length=50),
        ),
    ]
