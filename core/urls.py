from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('login/', include('user.urls')),
    path('equipamento/', include('equipamento.urls')),
    path('emprestimo/', include('emprestimo.urls')),
]