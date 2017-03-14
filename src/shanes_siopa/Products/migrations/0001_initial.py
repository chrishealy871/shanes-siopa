# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('tag', models.CharField(blank=True, max_length=30, null=True)),
                ('rating', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
