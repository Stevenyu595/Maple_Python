# Generated by Django 2.2 on 2020-12-04 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0016_auto_20201204_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='profilepic.jpg', upload_to='profile_pictures'),
        ),
    ]
