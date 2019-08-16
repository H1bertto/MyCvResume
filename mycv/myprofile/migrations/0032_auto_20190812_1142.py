# Generated by Django 2.2.4 on 2019-08-12 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0031_auto_20190812_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skill_5',
            field=models.CharField(default='null', max_length=50, verbose_name='Professional Skill 5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='skill_6',
            field=models.CharField(default='null', max_length=50, verbose_name='Professional Skill 6'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='value_skill_5',
            field=models.IntegerField(default=0, verbose_name='% Of Skill 5'),
        ),
        migrations.AddField(
            model_name='profile',
            name='value_skill_6',
            field=models.IntegerField(default=0, verbose_name='% Of Skill 6'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill_1',
            field=models.CharField(max_length=50, verbose_name='Professional Skill 1'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill_2',
            field=models.CharField(max_length=50, verbose_name='Professional Skill 2'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill_3',
            field=models.CharField(max_length=50, verbose_name='Professional Skill 3'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill_4',
            field=models.CharField(max_length=50, verbose_name='Professional Skill 4'),
        ),
    ]
