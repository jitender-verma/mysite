# Generated by Django 3.0.6 on 2020-09-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0003_userdetails_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='managerdetails',
            name='profile_pic',
            field=models.FileField(blank=True, default='/static/img/admin-demo.png', null=True, upload_to=''),
        ),
    ]
