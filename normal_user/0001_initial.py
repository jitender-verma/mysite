# Generated by Django 3.0.6 on 2020-05-22 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerTimezones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.IntegerField(blank=True, null=True)),
                ('timezone1', models.CharField(blank=True, max_length=100)),
                ('timezone2', models.CharField(blank=True, max_length=100)),
                ('timezone3', models.CharField(blank=True, max_length=100)),
                ('timezone4', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.BooleanField(default=1)),
                ('normal_user', models.BooleanField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email2', models.CharField(blank=True, max_length=100)),
                ('phone_no_1', models.CharField(blank=True, max_length=100)),
                ('phone_no_2', models.CharField(blank=True, max_length=100)),
                ('timezone', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('count_timer', models.CharField(blank=True, max_length=100)),
                ('it_equipment_specification', models.CharField(blank=True, max_length=100)),
                ('comment', models.CharField(blank=True, max_length=100)),
                ('function', models.CharField(blank=True, max_length=100)),
                ('add_schedule_date_time', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.IntegerField(blank=True, null=True)),
                ('task', models.TextField(blank=True, null=True)),
                ('staff_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaffStatusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.IntegerField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('staff_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvalidAttempts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempts', models.IntegerField(blank=True, null=True)),
                ('blocked', models.BooleanField(default=1)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.IntegerField(blank=True, null=True)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('descrtiption', models.CharField(blank=True, max_length=250, null=True)),
                ('to_email', models.CharField(blank=True, max_length=250, null=True)),
                ('from_email', models.CharField(blank=True, max_length=250, null=True)),
                ('staff_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.IntegerField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('staff_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlertModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.IntegerField(blank=True, null=True)),
                ('alert', models.BooleanField(default=False)),
                ('staff_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
