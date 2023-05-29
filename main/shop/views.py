from django.shortcuts import render
from django.views import View

# Create your views here.
class ShopIndex(View):
    def get(self, request):
        template = 'shop/shop.html'
        return render(request, template)