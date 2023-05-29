from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUp, CustomLogin, ConfirmUser

app_name = 'users'

urlpatterns = [
    path('loginn/', LoginView.as_view(), name='login'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('confirm/<str:username>/', ConfirmUser.as_view(), name='confirm')
]