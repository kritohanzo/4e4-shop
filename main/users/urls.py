from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUp, ConfirmUser, ProfileView
from .forms import UserLoginForm
from core.decorators import nologin_required, noconfirm_nologin_required


app_name = 'users'

urlpatterns = [
    path('login/', nologin_required(LoginView.as_view(template_name='users/login.html', form_class=UserLoginForm)), name='login'),
    path('signup/', nologin_required(SignUp.as_view()), name='signup'),
    path('confirm/<str:username>/', noconfirm_nologin_required(ConfirmUser.as_view()), name='confirm'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
]