from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm  # Importe o seu formulário personalizado

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(authentication_form=CustomAuthenticationForm),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
