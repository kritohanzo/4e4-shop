from users.models import User
from django import forms
from django.utils.text import capfirst
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import authenticate

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Имя  '}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
class UserLoginForm(AuthenticationForm):

    username = UsernameField(label='Username', widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Имя'}))
    # username = None
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    