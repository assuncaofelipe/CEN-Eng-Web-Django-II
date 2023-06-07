# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Emprestimo


# @method_decorator(login_required, name='dispatch')
class ListarEmprestimo(ListView):
    template_name = 'listar_emprestimo.html'
    model = Emprestimo
    context_object_name = 'emprestimos'


# @method_decorator(login_required, name='dispatch')
class CadastrarEmprestimo(CreateView):
    template_name = 'crud_emprestimo.html'
    model = Emprestimo
    fields = ['nome', 'matricula', 'curso',
              'equipamento', 'data_emprestimo',
              'data_devolucao', 'observacao']
    success_url = reverse_lazy('listar_emprestimo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Cadastrar"
        return context


# @method_decorator(login_required, name='dispatch')
class EditarEmprestimo(UpdateView):
    template_name = 'crud_emprestimo.html'
    model = Emprestimo
    fields = ['nome', 'matricula', 'curso',
              'equipamento', 'data_emprestimo',
              'data_devolucao', 'observacao']
    success_url = reverse_lazy('listar_emprestimo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar"
        return context
