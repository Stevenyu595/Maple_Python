# Generated by Django 2.2 on 2020-12-04 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0021_auto_20201204_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='images/none'),
        ),
    ]
