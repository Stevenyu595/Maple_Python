# Generated by Django 2.2 on 2020-12-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0032_side'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('one', models.FloatField()),
                ('three', models.FloatField()),
                ('six', models.FloatField()),
                ('image', models.ImageField(default='https://www.takeoutlist.com/assets/images/food_default.png', upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.RemoveField(
            model_name='side',
            name='one',
        ),
        migrations.RemoveField(
            model_name='side',
            name='six',
        ),
        migrations.RemoveField(
            model_name='side',
            name='three',
        ),
    ]
