# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='Nome')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug', blank=True)),
                ('parents', models.CharField(max_length=250, verbose_name='Pais')),
                ('description', models.TextField(verbose_name='Descri\xe7\xe3o', blank=True)),
                ('img', models.CharField(max_length=250, verbose_name='img', blank=True)),
            ],
            options={
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=250, verbose_name='Tipo')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug', blank=True)),
                ('description', models.TextField(verbose_name='Descri\xe7\xe3o', blank=True)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='Nome')),
                ('original_name', models.CharField(max_length=250, verbose_name='Nome', blank=True)),
                ('slug', models.SlugField(unique=True, verbose_name='Slug', blank=True)),
                ('synopsis', models.TextField(verbose_name='Sinopse', blank=True)),
                ('img', models.CharField(max_length=250, verbose_name='img')),
                ('actors', models.ManyToManyField(to='core.Actors', verbose_name='Atores', blank=True)),
                ('genres', models.ManyToManyField(to='core.Genres', verbose_name='Genero', blank=True)),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
            },
            bases=(models.Model,),
        ),
    ]
