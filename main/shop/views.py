from django.shortcuts import render
from django.views import View
from core.decorators import confirm_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser
from core.database_functions import get_all_objects, get_all_shoes

# Create your views here.
class ShopView(View):
    @confirm_required
    def get(self, request):
        template = 'shop/shop.html'
        objects = get_all_shoes()
        print(objects)
        context = {"products": objects}
        return render(request, template, context)
    
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