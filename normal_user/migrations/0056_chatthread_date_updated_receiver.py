# Generated by Django 3.0.6 on 2020-07-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0055_chatmessage_created_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatthread',
            name='date_updated_receiver',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
