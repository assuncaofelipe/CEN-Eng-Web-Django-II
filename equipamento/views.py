from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Equipamento


@method_decorator(login_required, name='dispatch')
class ListarEquipamento(ListView):
    template_name = 'listar_equipamento.html'
    model = Equipamento
    context_object_name = 'equipamentos'


@method_decorator(login_required, name='dispatch')
class CadastrarEquipamento(CreateView):
    template_name = 'crud_equipamento.html'
    model = Equipamento
    fields = ['nome', 'patrimonio', 'codigo',
              'situacao', 'observacao', 'status']
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Cadastrar"
        return context


@method_decorator(login_required, name='dispatch')
class EditarEquipamento(UpdateView):
    template_name = 'crud_equipamento.html'
    model = Equipamento
    fields = ['nome', 'patrimonio', 'codigo',
              'situacao', 'observacao', 'status']
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar"
        return context
