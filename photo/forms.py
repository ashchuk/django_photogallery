# coding=utf-8
__author__ = 'ashchuk'

from django import forms
from nocaptcha_recaptcha import NoReCaptchaField


class ReCaptchaForm(forms.Form):
    name = forms.CharField(
            label='Your name',
            required=True,
            widget=forms.TextInput(
                    attrs={'class': 'validate[required] text-input',
                           'type': "text", 'name': "name", 'id': "name", 'placeholder': "Имя"}))
    subject = forms.CharField(
            label='Your subject',
            required=True,
            widget=forms.TextInput(
                    attrs={'class': 'validate[required] text-input',
                           'type': "text", 'name': "subject", 'id': "subject", 'placeholder': "Заголовок"}))
    email = forms.EmailField(
            label='Your e-mail address',
            required=True,
            widget=forms.TextInput(attrs={'class': 'validate[required,custom[email]] text-input',
                                          'type': "text", 'name': "email", 'id': "email", 'placeholder': "Электронная почта"}))
    message = forms.CharField(
            label='Your message',
            required=True,
            widget=forms.Textarea(attrs={'class': 'validate[required] text-input',
                                         'type': "text", 'name': "message", 'id': "message", 'placeholder': "Текст сообщения"}))
    recaptcha = NoReCaptchaField(gtag_attrs={'data-theme':'dark'})