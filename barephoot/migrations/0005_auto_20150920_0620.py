# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barephoot', '0004_movdata_showing'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheatreDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theatre', models.CharField(unique=True, max_length=200)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('rating', models.FloatField()),
                ('price2', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='movdata',
            old_name='showing',
            new_name='movie_name',
        ),
        migrations.RenameField(
            model_name='movdata',
            old_name='name',
            new_name='theatre',
        ),
        migrations.RemoveField(
            model_name='movdata',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='movdata',
            name='long',
        ),
        migrations.RemoveField(
            model_name='movdata',
            name='price2',
        ),
        migrations.RemoveField(
            model_name='movdata',
            name='rating',
        ),
        migrations.AddField(
            model_name='movdata',
            name='timing',
            field=models.CharField(default='0 00', max_length=10),
            preserve_default=False,
        ),
    ]
