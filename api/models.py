from django.db import models

from django.contrib.auth.models import User


def unique_rand():
    while True:
        code = password = User.objects.make_random_password(length=8)
        if not DiscountCodes.objects.filter(code=code).exists():
            return code


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=300)
    image = models.ImageField(upload_to="categories")

    def __str__(self):
        return self.title


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class DiscountCodes(models.Model):
    id = models.AutoField(primary_key=True)
    usages = models.IntegerField()
    discount_percentage = models.IntegerField()
    code = models.TextField(default=unique_rand, unique=True)
