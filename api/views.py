from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import DiscountCodesSerializer, ProductSerializer, CategoriesSerializer

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