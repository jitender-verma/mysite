# Generated by Django 3.0.6 on 2020-05-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0004_auto_20200528_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cities', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
