from users.models import User
from django import forms
from django.utils.text import capfirst
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


# class UserRegistrationForm(forms.ModelForm):
#     username = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Имя  '}))
#     email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
#     password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'placeholder': 'Пароль'}))

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
    
class UserLoginForm(AuthenticationForm):

    username = UsernameField(label='Email', widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Почта'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    # class Meta:
    #     model = User
    #     fields = ('email', 'password')

    # def __init__(self, request=None, *args, **kwargs):
    #     """
    #     The 'request' parameter is set for custom auth use by subclasses.
    #     The form data comes in via the standard 'data' kwarg.
    #     """
    #     self.request = request
    #     self.user_cache = None
    #     super().__init__(*args, **kwargs)

    #     # Set the max length and label for the "username" field.
    #     self.email_field = User._meta.get_field(User.EMAIL_FIELD)
    #     self.fields['email'].max_length = self.email_field.max_length or 254
    #     if self.fields['email'].label is None:
    #         self.fields['email'].label = capfirst(self.email_field.verbose_name)

    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')

    #     if email is not None and password:
    #         self.user_cache = authenticate(self.request, email=email, password=password)
    #         if self.user_cache is None:
    #             raise self.get_invalid_login_error()
    #         else:
    #             self.confirm_login_allowed(self.user_cache)

    #     return self.cleaned_data
    
    # def get_invalid_login_error(self):
    #     return forms.ValidationError(
    #         self.error_messages['invalid_login'],
    #         code='invalid_login',
    #         params={'email': self.email_field.verbose_name},
    #     )

    