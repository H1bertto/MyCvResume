# Generated by Django 2.2.4 on 2019-08-09 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0008_education_review_workexperience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='period',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='period',
        ),
        migrations.AddField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='education',
            name='is_actual',
            field=models.BooleanField(default=False, verbose_name='Is Actual?'),
        ),
        migrations.AddField(
            model_name='education',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Start Date'),
        ),
        migrations.AddField(
            model_name='review',
            name='role',
            field=models.CharField(max_length=50, null=True, verbose_name='Role'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='is_actual',
            field=models.BooleanField(default=False, verbose_name='Is Actual?'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='role_1',
            field=models.CharField(max_length=100, verbose_name='Role 1'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='role_2',
            field=models.CharField(max_length=100, verbose_name='Role 2'),
        ),
    ]