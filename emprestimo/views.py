from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Emprestimo, Equipamento


@method_decorator(login_required, name='dispatch')
class ListarEmprestimo(ListView):
    template_name = 'listar_emprestimo.html'
    model = Emprestimo
    context_object_name = 'emprestimos'


@method_decorator(login_required, name='dispatch')
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
        equipamentos_disponiveis = Equipamento.objects.filter(status='1')
        if not equipamentos_disponiveis:
            context['sem_equipamentos'] = True
        return context

    def form_valid(self, form):
        emprestimo = form.save(commit=False)
        equipamento = form.cleaned_data['equipamento']
        equipamento.status = '0'
        equipamento.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['equipamento'].queryset = Equipamento.objects.filter(status='1')
        return form


@method_decorator(login_required, name='dispatch')
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
