from django.shortcuts import render, redirect
from django.views import View
from core.database_functions import register_user

# Create your views here.
class SignUp(View):
    def get(self, request):
        return redirect('users:login')
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        register_user(username, email, password)
        return render(request, 'shop/shop.html')


