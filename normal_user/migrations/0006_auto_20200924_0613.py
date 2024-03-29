# Generated by Django 3.0.6 on 2020-09-24 06:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0005_auto_20200924_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduletiming',
            name='break_time',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), null=True),
        ),
        migrations.AlterField(
            model_name='scheduletiming',
            name='offline_time',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), null=True),
        ),
        migrations.AlterField(
            model_name='scheduletiming',
            name='online_time',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), null=True),
        ),
    ]
