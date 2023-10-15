from django.urls import path
from emprestimo import views

urlpatterns = [
    path('', views.ListarEmprestimo.as_view(), name="listar_emprestimo"),
    path('cadastrar/', views.CadastrarEmprestimo.as_view(), name="cadastrar_emprestimo"),
    path('editar/<int:pk>', views.EditarEmprestimo.as_view(), name="editar_emprestimo"),
    path('apagar/<int:pk>', views.DeletarEmprestimo.as_view(), name="deletar_emprestimo"),
    path('devolver_emprestimo/<int:emprestimo_id>/', views.DevolverEmprestimo.as_view(), name='devolver_emprestimo'),
]
