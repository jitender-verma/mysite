# Generated by Django 3.0.6 on 2020-06-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0029_chatthread_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatthread',
            name='date_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
