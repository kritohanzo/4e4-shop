from django import forms


class BuyForm(forms.Form):
    product = forms.Field(label="Продукт", widget=forms.TextInput(attrs={'class': 'd-none'}))
    full_name = forms.CharField(label="ФИО", max_length=64, widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'на чьё имя отправляем', 'class': 'text-center'}))
    number = forms.CharField(label="Номер телефона", max_length=16, widget=forms.TextInput(attrs={'placeholder': 'куда сообщим', 'class': 'text-center'}))
    mail_index = forms.CharField(label="Почтовый индекс", max_length=12, widget=forms.TextInput(attrs={'placeholder': 'индекс отправки', 'class': 'text-center'}))

class FeedbackForm(forms.Form):
    feedback = forms.CharField(label="Обратная связь", widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Оставьте здесь свои пожелания', 'class': 'text-center', 'style': "height: calc(16em + 4.75rem + 2px); width: calc(16em + 4.75rem + 2px);"}))