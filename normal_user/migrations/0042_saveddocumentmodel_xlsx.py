# Generated by Django 3.0.6 on 2020-07-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0041_chatthread_archive_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='saveddocumentmodel',
            name='xlsx',
            field=models.BooleanField(default=False),
        ),
    ]
