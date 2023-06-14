from django.urls import path
from equipamento import views

urlpatterns = [
    path('', views.ListarEquipamento.as_view(), name="home"),
    path('cadastrar/', views.CadastrarEquipamento.as_view(), name="cadastrar_equipamento"),
    path('editar/<int:pk>', views.EditarEquipamento.as_view(), name="editar_equipamento"),
    path('apagar/<int:pk>', views.DeletarEquipamento.as_view(), name="deletar_equipamento"),
]