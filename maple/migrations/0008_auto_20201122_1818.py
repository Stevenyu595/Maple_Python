# Generated by Django 2.2 on 2020-11-23 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0007_auto_20201122_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.CharField(default='https://longsshotokan.com/wp-content/uploads/2017/04/default-image-720x530.jpg', max_length=500),
        ),
    ]
