
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework import viewsets
from .models import *
from .serializers import DiscountCodesSerializer, OrderSerializer, ProductSerializer, CategoriesSerializer, \
    MainPageSerializer
import json
from liqpay import LiqPay
from django.views.decorators.csrf import csrf_exempt
import telebot

PUBLIC_KEY = "sandbox_i20334026307"
PRIVATE_KEY = "sandbox_gi37dYhcivXvsbBvsJD1FBobwRpjmrDM3q4CtNQn"

BOT_TOKEN = "5611537678:AAFlY1cUgbyRDQaCMzM4j92MXriAnz2nCAA"
CHANNEL_ID = "-1001742666834"


@csrf_exempt
def checkout(request):
    if request.method == "POST":
        data = json.loads(request.body.decode())
        print(data)
        cash = data["money"]
        order = data['order_id']
        liqpay = LiqPay(PUBLIC_KEY, PRIVATE_KEY)
        params = {
            'action': 'pay',
            'amount': cash,
            'currency': 'UAH',
            'description': f'Онлайн оплата замовлення: {order}',
            'order_id': str(order),
            'version': '3',
            'sandbox': 1,  # sandbox mode, set to 1 to enable it
            'server_url': 'https://185.65.244.209:3000/api/pay-callback/',
            'result_url': "https://guculybakery.com.ua/payment"
        }
        resp = liqpay.cnb_form(params)
        print(resp)
        return HttpResponse(resp)
    else:
        return HttpResponse(403)


@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(PUBLIC_KEY, PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(PRIVATE_KEY + data + PRIVATE_KEY)
        if sign == signature:
            print('callback is valid')
        response = liqpay.decode_data_from_str(data)
        print('callback data', response)
        if response["status"] == "success" or response["status"] == "sandbox":
            order = Order.objects.get(id=response["order_id"])
            send_payment_to_channel(f"НОВЕ ЗАМОВЛЕННЯ: {order.id}\n{order.cart}\n{order.name}\n{order.contact_phone}|{order.email}\nMessager: {order.messanger}\n{order.delivery_type}\nОПЛАЧЕНО ОНЛАЙН")
        return HttpResponse(200)

def send_payment_to_channel(text):
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(CHANNEL_ID, f"{text}")

@csrf_exempt
def send_message_to_channel(request):
    if request.method == "POST":
        bot = telebot.TeleBot(BOT_TOKEN)
        data = json.loads(request.body.decode())
        print(data)
        bot.send_message(CHANNEL_ID, f"{data['text']}")
        return HttpResponse(200)
    else:
        return HttpResponse(403)

@csrf_exempt
def use_promo(request):
    if request.method == "POST":
        data = json.loads(request.body.decode())
        print(data)
        code = data['code']
        v = DiscountCodes.objects.get(code = code)
        old = v.usages
        v.usages = old - 1
        v.save()
        return HttpResponse(200)

@csrf_exempt
def add_order(request):
    if request.method == "POST":
        data = json.loads(request.body.decode())
        name = data["name"]
        cart = data["cart"]
        phone = data["phone"]
        email = data["email"]
        delivery = data['delivery']
        messanger = data["messanger"]
        payment = data['payment']
        object_instance = Order.objects.create(name = name, cart = cart, contact_phone = phone, email = email, delivery_type = delivery, messanger = messanger, payment_type = payment)
        object_instance.save()
        print(object_instance)
        return HttpResponse(object_instance)
    else:
        return HttpResponse(403)

# Create your views here.
class DiscoutCodesViewSet(viewsets.ModelViewSet):
    queryset = DiscountCodes.objects.all()
    serializer_class = DiscountCodesSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class MainPageViewSet(viewsets.ModelViewSet):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
