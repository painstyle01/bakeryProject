from dataclasses import field
from .models import AboutUs, Categories, DeliveryAndPayment, Oferta, Order, PrivacyPolicy, Product, DiscountCodes, MainPage
from rest_framework import serializers


class MainPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainPage
        fields = ('title', 'text', 'pic')


class DiscountCodesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiscountCodes
        fields = ('usages', 'discount_percentage', 'code')


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('title',)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ("id", 'title', 'image', 'category', 'description', 'price', 'availability')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "name", 'cart', "contact_phone", "email", 'delivery_type', "messanger", "payment_type")

class AboutUsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('title','text')

class PrivacyPolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ('title','text')

class OfertaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Oferta
        fields = ('title','text')

class DeliveryAndPaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeliveryAndPayment
        fields = ('title','text')