from django.shortcuts import render, redirect
from django.views import View
from core.database_functions import get_all_worker_orders, get_all_free_orders, take_order, end_order, get_all_products

# Create your views here.
class IndexView(View):
    def get(self, request):
        template = "workzone/main.html"
        orders = get_all_free_orders()
        print(orders)
        context = {'orders': orders}
        return render(request, template, context)
    

class StorageView(View):
    def get(self, request):
        template = "workzone/storage.html"
        products = get_all_products()
        print(products)
        context = {'products': products}
        return render(request, template, context)
    

class ProfileView(View):
    def get(self, request):
        template = "workzone/myorders.html"
        orders = get_all_worker_orders(request.user.id)
        context = {'orders': orders}
        return render(request, template, context)
    
class AcceptOrderView(View):
    def get(self, request, order_id):
        take_order(order_id, request.user.id)
        return redirect('workzone:profile')
    
class EndOrderView(View):
    def get(self, request, order_id):
        end_order(order_id, request.user.id)
        return redirect('workzone:profile')