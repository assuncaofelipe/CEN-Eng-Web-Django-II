from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('', include('app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('equipamentos/', include('equipamento.urls')),
    path('emprestimo/', include('emprestimo.urls')),
]