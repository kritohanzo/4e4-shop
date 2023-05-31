from django.shortcuts import render
from django.views import View

# Create your views here.
class ShopView(View):
    def get(self, request):
        template = 'shop/shop.html'
        return render(request, template)
    
class KediView(View):
    def get(self, request):
        template = 'shop/shop-kedi.html'
        return render(request, template)
    
class KrossiView(View):
    def get(self, request):
        template = 'shop/shop-krossi.html'
        return render(request, template)
    
class TufliView(View):
    def get(self, request):
        template = 'shop/shop-tufli.html'
        return render(request, template)
    
class SapogiView(View):
    def get(self, request):
        template = 'shop/shop-sapogi.html'
        return render(request, template)