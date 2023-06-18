from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from core.database_functions import register_user, check_confirm_code, accept_user, set_confirm_code, get_all_user_orders
from core.confirm_code_generator import generate_code
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from core.decorators import nologin_required
from django.core.mail import send_mail
from django.template.loader import render_to_string



class SignUp(CreateView):
    template_name = 'users/signup.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('shop:index')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class ConfirmUser(View):
    def get(self, request, username):
        template = 'users/confirm_user.html'
        context = {'username': username, "user": request.user}
        code = set_confirm_code(username)
        send_mail(f'Подтверждение аккаунта {request.user.email}', message='123', from_email='test_smtp_timp@mail.ru', recipient_list=[f"{request.user.email}"], html_message=render_to_string('core/confirm_mail.html', {"user": request.user, "code": code}))
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
    def get(self, request):
        template = 'users/profile.html'
        orders = get_all_user_orders(request.user.id)
        context = {'orders': orders, 'user': request.user, "orders_count": len(orders)}
        return render(request, template, context)