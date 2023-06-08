from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from core.database_functions import register_user, check_confirm_code, accept_user
from core.confirm_code_generator import generate_code
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from core.decorators import nologin_required


class SignUp(CreateView):
    template_name = 'users/signup.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('shop:index')

    def form_valid(self, form):
        print(form)
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


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

class ProfileView(View):
    def get(self, request, username):
        template = 'users/profile.html'
        return render(request, template)