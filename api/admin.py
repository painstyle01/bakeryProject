from django.contrib import admin
from api.models import DiscountCodes, Order, Product, Categories, MainPage

# Register your models here.
admin.site.register(DiscountCodes)
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(MainPage)
admin.site.register(Order)
