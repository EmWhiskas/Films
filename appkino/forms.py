from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ModelPodpiska
from captcha.fields import CaptchaField
class FormRegister(UserCreationForm):
    username = forms.CharField(label='Логин', help_text='')
    password1 = forms.CharField(label='Пароль', help_text='',
                                widget=forms.PasswordInput(
                                    attrs={'autocomplete':'new-password'}
                                ))
    password2 = forms.CharField(label='Подтверждение пароля', help_text='',
                                widget=forms.PasswordInput(
                                    attrs={'autocomplete':'new-password'}
                                ))
    email = forms.EmailField(label='Почта',
                             widget=forms.TextInput(
                                 attrs={'placeholder':'qwe@mail.ru'}
                             ))
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)
    captcha = CaptchaField()
class FormPodpiska(forms.Form):
    item = forms.ModelChoiceField(ModelPodpiska.objects.all(), label='Выберете')

class FormOtziv(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'name': 'text', 'rows': 5, 'cols': 50}),
                           label='Напишите комментарий', min_length=10)

    nerobot = forms.BooleanField(error_messages={'required': 'вы робот.'}, label="Вы не робот")