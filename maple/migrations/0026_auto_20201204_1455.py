# Generated by Django 2.2 on 2020-12-04 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0025_auto_20201204_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.CharField(default='https://www.takeoutlist.com/assets/images/food_default.png', max_length=500),
        ),
    ]
