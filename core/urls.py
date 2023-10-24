from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("app.urls")),
    path("accounts/", include("user.urls")),
    path("admin", admin.site.urls),
    path("equipamento/", include("equipamento.urls")),
    path("emprestimo/", include("emprestimo.urls")),
]
