# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150614_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='original_name',
            field=models.CharField(max_length=250, verbose_name='Nome Original', blank=True),
        ),
    ]
