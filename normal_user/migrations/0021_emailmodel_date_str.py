# Generated by Django 3.0.6 on 2020-06-18 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0020_scheduletiming'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmodel',
            name='date_str',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
