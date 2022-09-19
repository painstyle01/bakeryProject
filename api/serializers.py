from .models import Categories, Product, DiscountCodes, MainPage
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
