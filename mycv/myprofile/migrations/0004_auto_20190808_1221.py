# Generated by Django 2.2.4 on 2019-08-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0003_auto_20190807_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='image_3',
            field=models.ImageField(blank=True, upload_to='portfolio/images', verbose_name='Image 3'),
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='category',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='category',
            field=models.ManyToManyField(to='myprofile.Category'),
        ),
    ]