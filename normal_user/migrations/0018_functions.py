# Generated by Django 3.0.6 on 2020-06-16 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0017_emailmodel_email_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Functions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
