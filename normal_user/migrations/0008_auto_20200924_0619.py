# Generated by Django 3.0.6 on 2020-09-24 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0007_auto_20200924_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduletiming',
            name='break_time',
        ),
        migrations.RemoveField(
            model_name='scheduletiming',
            name='offline_time',
        ),
        migrations.RemoveField(
            model_name='scheduletiming',
            name='online_time',
        ),
    ]
