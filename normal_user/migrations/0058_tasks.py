# Generated by Django 3.0.6 on 2020-07-31 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0057_auto_20200729_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(blank=True, null=True)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='normal_user.TaskModel')),
            ],
        ),
    ]
