# Generated by Django 3.0.6 on 2020-07-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0054_userdetails_last_countdown_timer_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='created_receiver',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
