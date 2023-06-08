from django.urls import path
from .views import ShopView, KediView, KrossiView, TufliView, SapogiView
from django.contrib.auth.decorators import login_required

app_name = 'shop'

urlpatterns = [
    path('', login_required(ShopView.as_view()), name='index'),
    path('kedi/', KediView.as_view(), name='kedi'),
    path('krossi/', KrossiView.as_view(), name='krossi'),
    path('tufli/', TufliView.as_view(), name='tufli'),
    path('sapogi/', SapogiView.as_view(), name='sapogi'),

]