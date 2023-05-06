from django.urls import path, include
from app import views

urlpatterns = [
    path('', include('user.urls'), name="login"),
    path('', include('home.urls'), name="home"),
]