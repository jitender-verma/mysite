# Generated by Django 3.0.6 on 2020-09-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0002_userdetails_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='profile_pic',
            field=models.FileField(blank=True, default='/static/img/admin-demo.png', null=True, upload_to=''),
        ),
    ]
