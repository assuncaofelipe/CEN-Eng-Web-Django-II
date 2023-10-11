from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="", widget=forms.TextInput(attrs={"placeholder": "Usuário..."})
    )
    password = forms.CharField(
        label="", widget=forms.PasswordInput(attrs={"placeholder": "Senha..."})
    )
