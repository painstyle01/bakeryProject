from django.contrib import admin
from api.models import DiscountCodes, Order, Product, Categories, MainPage, PrivacyPolicy, AboutUs, Oferta, DeliveryAndPayment

# Register your models here.
admin.site.register(DiscountCodes)
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(MainPage)
admin.site.register(Order)
admin.site.register(PrivacyPolicy)
admin.site.register(DeliveryAndPayment)
admin.site.register(Oferta)
admin.site.register(AboutUs)