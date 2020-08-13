# Generated by Django 3.0.6 on 2020-06-09 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('normal_user', '0011_managerdetails_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineStatusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_am_here', models.BooleanField(default=False)),
                ('in_meeting', models.BooleanField(default=False)),
                ('lunch_break', models.BooleanField(default=False)),
                ('tea_break', models.BooleanField(default=False)),
                ('offline', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
