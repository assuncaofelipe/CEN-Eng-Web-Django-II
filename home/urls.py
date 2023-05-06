from django.urls import path

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    ]