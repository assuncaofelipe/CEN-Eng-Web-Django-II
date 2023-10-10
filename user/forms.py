from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Seu nome de usuário'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Sua senha'}))