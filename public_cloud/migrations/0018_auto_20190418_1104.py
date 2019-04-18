# Generated by Django 2.1.7 on 2019-04-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_cloud', '0017_auto_20190323_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountinfo',
            name='is_import',
            field=models.IntegerField(default=0, verbose_name='是否已导入'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='is_import',
            field=models.IntegerField(default=1, verbose_name='是否导入'),
        ),
    ]
