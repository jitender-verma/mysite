# Generated by Django 3.0.6 on 2020-05-27 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0002_managerdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='managerdetails',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
