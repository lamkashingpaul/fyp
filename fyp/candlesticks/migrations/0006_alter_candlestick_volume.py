# Generated by Django 3.2.4 on 2021-07-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candlesticks', '0005_auto_20210628_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candlestick',
            name='volume',
            field=models.FloatField(verbose_name='Volume (M)'),
        ),
    ]
