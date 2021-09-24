# Generated by Django 2.2 on 2020-12-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0031_auto_20201227_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('large', models.FloatField()),
                ('regular', models.FloatField()),
                ('one', models.FloatField()),
                ('three', models.FloatField()),
                ('six', models.FloatField()),
                ('image', models.ImageField(default='https://www.takeoutlist.com/assets/images/food_default.png', upload_to='images')),
            ],
        ),
    ]
