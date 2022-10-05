from email.policy import default
from statistics import mode
from turtle import title
from django.db import models

from django.contrib.auth.models import User


def unique_rand():
    while True:
        code = password = User.objects.make_random_password(length=8)
        if not DiscountCodes.objects.filter(code=code).exists():
            return code


class MainPage(models.Model):
    title = models.TextField()
    text = models.TextField()
    pic = models.ImageField(upload_to="main_page")

    def __str__(self):
        return self.text

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=300)

    def __str__(self):
        return self.title

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    cart = models.TextField()
    contact_phone = models.TextField()
    email = models.TextField()
    delivery_type = models.TextField()
    messanger = models.TextField()
    payment_type = models.TextField()

    def __str__(self) -> str:
        return str(self.id)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)
    image = models.ImageField(upload_to="products")
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

class PrivacyPolicy(models.Model):
    title = models.TextField(default="Політика конфіденційності")
    text = models.TextField()

class Oferta(models.Model):
    title = models.TextField(default='Оферта')
    text = models.TextField()

class AboutUs(models.Model):
    title = models.TextField(default='Про нас')
    text = models.TextField()

class DeliveryAndPayment(models.Model):
    title = models.TextField(default="Оплата і доставка")
    text = models.TextField()