# Generated by Django 3.0.6 on 2020-06-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0012_onlinestatusmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinestatusmodel',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
