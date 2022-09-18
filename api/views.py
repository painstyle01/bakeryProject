import random

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework import viewsets
from .models import *
from .serializers import DiscountCodesSerializer, ProductSerializer, CategoriesSerializer, MainPageSerializer
import json
from liqpay import LiqPay
from django.views.decorators.csrf import csrf_exempt

PUBLIC_KEY = "sandbox_i34833063512"
PRIVATE_KEY = "sandbox_cuqc4wGddoGwXZz0spEhMpkanF4NY88Ja8ADeUQo"


@csrf_exempt
def checkout(request):
    if request.method == "POST":
        data = json.loads(request.body.decode())
        print(data)
        cash = data["money"]
        liqpay = LiqPay(PUBLIC_KEY, PRIVATE_KEY)
        params = {
            'action': 'pay',
            'amount': cash,
            'currency': 'UAH',
            'description': f'Онлайн оплата замовлення: 123',
            'order_id': random.randint(0, 1000000000),
            'version': '3',
            'sandbox': 1,  # sandbox mode, set to 1 to enable it
            'server_url': 'http://165.227.148.180:8000/api/pay-callback/',
            'result_url': "https://google.com"
        }
        resp = liqpay.cnb_form(params)
        print(resp)
        return HttpResponse(resp)


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
        return HttpResponse()


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
