from users.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Name', help_text='ВАШЕ ИМЯ')
    email = forms.EmailField(label='Email', help_text='ПОЧТА')
    password = forms.CharField(label='Password', help_text='ВАШ ПАРОЛ')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
class UserLoginForm(forms.ModelForm):
    email = forms.EmailField(label='Email', help_text='ПОЧТА')
    password = forms.CharField(label='Password', help_text='ВАШ ПАРОЛ')

    class Meta:
        model = User
        fields = ('email', 'password')