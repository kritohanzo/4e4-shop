from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUp, CustomLogin, ConfirmUser
from .forms import UserLoginForm

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', form_class=UserLoginForm), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('confirm/<str:username>/', ConfirmUser.as_view(), name='confirm'),
    path('logout/', LogoutView.as_view(), name='logout'),
]