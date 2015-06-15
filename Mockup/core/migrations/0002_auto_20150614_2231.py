# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='img',
            field=models.CharField(max_length=250, verbose_name='img', blank=True),
        ),
    ]
