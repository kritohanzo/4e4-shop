from django.shortcuts import render, redirect
from django.views import View
from core.database_functions import register_user, check_confirm_code, accept_user
from core.confirm_code_generator import generate_code
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.views import LoginView

# Create your views here.

class SignUp(View):
    def get(self, request):
        template = 'users/signup.html'
        user_form = UserRegistrationForm()
        context = {'form': user_form}
        return render(request, template, context)
    
    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.confirm_code = generate_code()
            new_user.save()
            return redirect('users:confirm', username=new_user.username)
        return redirect('users:login')
    
    # def post(self, request):
    #     username = request.POST.get('username')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     register_user(username, email, password)
    #     return render(request, 'shop/shop.html')

class CustomLogin(View):
    def get(self, request):
        signup_form = UserRegistrationForm()
        login_form = UserLoginForm()    
        template = 'users/index.html'
        context = {'signup_form': signup_form, 'login_form': login_form}
        return render(request, template, context)
    
    def post():
        pass

class ConfirmUser(View):
    def get(self, request, username):
        template = 'users/confirm_user.html'
        context = {'username': username}
        return render(request, template, context)
    
    def post(self, request, username):
        user_code = request.POST.get('confirm_code')
        correct = check_confirm_code(username, user_code)
        print(correct)
        if correct:
            accept_user(username)
            return redirect('shop:index')
        return redirect('users:confirm', username=username)
