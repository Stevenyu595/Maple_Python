# Generated by Django 2.2 on 2020-12-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0034_auto_20201228_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='six',
            field=models.FloatField(verbose_name='2f'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='three',
            field=models.FloatField(verbose_name='2f'),
        ),
    ]
