# Generated by Django 3.0.6 on 2020-06-26 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0030_chatthread_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
