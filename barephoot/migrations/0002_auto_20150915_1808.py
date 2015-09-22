# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barephoot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('rating', models.IntegerField()),
                ('price2', models.IntegerField()),
                ('owner', models.ForeignKey(related_name=b'barephoot2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='movdata',
            name='owner',
            field=models.ForeignKey(related_name=b'barephoot', to=settings.AUTH_USER_MODEL),
        ),
    ]
