from django.urls import path
from .views import ShopIndex

app_name = 'shop'

urlpatterns = [
    path('index/', ShopIndex.as_view(), name='index')
]