# Generated by Django 2.2 on 2020-12-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0014_auto_20201203_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='images', upload_to='images/none/noimg.jpg'),
        ),
    ]
