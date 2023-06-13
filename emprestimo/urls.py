from django.urls import path
from emprestimo import views

urlpatterns = [
    path('', views.ListarEmprestimo.as_view(), name="listar_emprestimo"),
    path('cadastrar/', views.CadastrarEmprestimo.as_view(), name="cadastrar_emprestimo"),
    path('editar/<int:pk>', views.EditarEmprestimo.as_view(), name="editar_emprestimo"),
]
