# Generated by Django 3.0.6 on 2020-07-09 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0039_auto_20200709_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmodel',
            name='created_manager',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
