# Generated by Django 3.0.6 on 2020-09-24 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0008_auto_20200924_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduletiming',
            name='break_time',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), null=True),
        ),
        migrations.AddField(
            model_name='scheduletiming',
            name='offline_time',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), null=True),
        ),
        migrations.AddField(
            model_name='scheduletiming',
            name='online_time',
            field=models.TimeField(blank=True, default=datetime.time(0, 0), null=True),
        ),
    ]
