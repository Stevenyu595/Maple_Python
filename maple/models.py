from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Side(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    large = models.DecimalField(decimal_places=2, max_digits=4)
    regular = models.DecimalField(decimal_places=2, max_digits=4)
    image = models.ImageField(upload_to='images', default="https://www.takeoutlist.com/assets/images/food_default.png")

class Menu(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    one = models.DecimalField(decimal_places=2, max_digits=4)
    three = models.DecimalField(decimal_places=2, max_digits=4)
    six = models.DecimalField(decimal_places=2, max_digits=4)
    image = models.ImageField(upload_to='images', default="https://www.takeoutlist.com/assets/images/food_default.png")
    # image = models.ImageField(upload_to='images', default='images/none/sz.jpg')

class Chicken(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    large = models.DecimalField(decimal_places=2, max_digits=4)
    regular = models.DecimalField(decimal_places=2, max_digits=4)
    image = models.ImageField(upload_to='images', default="https://www.takeoutlist.com/assets/images/food_default.png")

class Beef(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    large = models.DecimalField(decimal_places=2, max_digits=4)
    regular = models.DecimalField(decimal_places=2, max_digits=4)
    image = models.ImageField(upload_to='images', default="https://www.takeoutlist.com/assets/images/food_default.png")

class Application(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    references = models.TextField(max_length=2000)
    previous_work = models.TextField(max_length=1000)
    job_position = models.TextField(max_length=1000)