# Generated by Django 2.2.4 on 2019-08-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0024_featuredproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredproject',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Visible'),
        ),
    ]