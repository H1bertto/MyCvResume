# Generated by Django 2.2.4 on 2019-08-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0029_profile_hire_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hire_me',
            field=models.TextField(verbose_name='Why Hire Me?'),
        ),
    ]
