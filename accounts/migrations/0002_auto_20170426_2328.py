# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-27 04:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='swings',
            old_name='end_rot_x',
            new_name='end_rot',
        ),
        migrations.RenameField(
            model_name='swings',
            old_name='end_rot_y',
            new_name='start_rot',
        ),
        migrations.RemoveField(
            model_name='swings',
            name='end_rot_z',
        ),
        migrations.RemoveField(
            model_name='swings',
            name='start_rot_x',
        ),
        migrations.RemoveField(
            model_name='swings',
            name='start_rot_y',
        ),
        migrations.RemoveField(
            model_name='swings',
            name='start_rot_z',
        ),
    ]
