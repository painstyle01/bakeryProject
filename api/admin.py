from django.contrib import admin
from api.models import DiscountCodes, Product, Categories

# Register your models here.
admin.site.register(DiscountCodes)
admin.site.register(Product)
admin.site.register(Categories)
