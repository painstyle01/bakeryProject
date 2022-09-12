from .models import Categories, Product, DiscountCodes
from rest_framework import serializers


class DiscountCodesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiscountCodes
        fields = ('usages', 'discount_percentage', 'code')


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('title', 'image')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'image', 'category', 'description', 'price', 'availability')
