# Generated by Django 2.2.4 on 2019-08-07 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_auto_20190807_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['title'], 'verbose_name': 'Portfolio', 'verbose_name_plural': 'Portfolios'},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ['name'], 'verbose_name': 'Technology', 'verbose_name_plural': 'Technologies'},
        ),
        migrations.AddField(
            model_name='technology',
            name='visible',
            field=models.BooleanField(blank=True, default=True, verbose_name='Visible'),
        ),
    ]