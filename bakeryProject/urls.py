"""bakeryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path
from rest_framework import routers
from api import views
from django.conf.urls.static import static
from django.conf import settings

from api.views import PayCallbackView, use_promo

router = routers.DefaultRouter()

router.register(r'products', views.ProductViewSet)
router.register(r'codes', views.DiscoutCodesViewSet)
router.register(r'categories', views.CategoriesViewSet)
router.register(r'mainpage', views.MainPageViewSet)
router.register(r'order', views.OrdersViewSet)
router.register(r'oferta', views.OfertaViewSet)
router.register(r'about_us', views.AboutUsViewSet)
router.register(r'privacy_policy', views.PrivacyPolicyViewSet)
router.register(r'delivery_and_payment', views.DeliveryAndPaymentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^api/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/checkout/', views.checkout, name='checkout'),
    path('api/send_bot/', views.send_message_to_channel, name='send_bot'),
    path('api/add_order/', views.add_order, name="add_order"),
    path("api/use_promo/", views.use_promo, name="use_promo"),
    re_path(r'^api/pay-callback/$', PayCallbackView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
