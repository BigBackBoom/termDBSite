# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('termDBFront', '0004_auto_20170129_0752'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=512)),
            ],
        ),
        migrations.AlterField(
            model_name='term',
            name='term_path',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='termDBFront.TermData'),
        ),
    ]
