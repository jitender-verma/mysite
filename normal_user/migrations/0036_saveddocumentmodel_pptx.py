# Generated by Django 3.0.6 on 2020-06-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0035_managerdetails_timezone'),
    ]

    operations = [
        migrations.AddField(
            model_name='saveddocumentmodel',
            name='pptx',
            field=models.BooleanField(default=False),
        ),
    ]
