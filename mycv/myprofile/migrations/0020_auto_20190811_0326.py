# Generated by Django 2.2.4 on 2019-08-11 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0019_auto_20190811_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='testimonial',
            field=models.TextField(max_length=200),
        ),
    ]
