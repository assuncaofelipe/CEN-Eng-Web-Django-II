from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Emprestimo, Equipamento
from django.db.models import Q
from django import forms
from django.http import HttpResponseRedirect
from django.views import View

@method_decorator(login_required, name="dispatch")
class ListarEmprestimo(ListView):
    template_name = "listar_emprestimo.html"
    model = Emprestimo
    context_object_name = "emprestimos"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search")
        if search_query:
            queryset = queryset.filter(
                Q(nome__icontains=search_query)
                | Q(equipamento__nome__icontains=search_query)
            )
        return queryset


class DateInput(forms.DateInput):
    input_type = "date"


class CadastrarEmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = [
            "nome",
            "matricula",
            "curso",
            "equipamento",
            "data_emprestimo",
            "data_devolucao",
            "observacao",
        ]
        widgets = {
            "data_emprestimo": DateInput(format="%d/%m/%Y"),
            "data_devolucao": DateInput(format="%d/%m/%Y"),
        }


def clean(self):
    cleaned_data = super().clean()
    data_emprestimo = cleaned_data.get("data_emprestimo")
    data_devolucao = cleaned_data.get("data_devolucao")

    if data_emprestimo and data_devolucao and data_devolucao < data_emprestimo:
        raise forms.ValidationError(
            "A data de devolução deve ser igual ou maior que a data de início."
        )


@method_decorator(login_required, name="dispatch")
class CadastrarEmprestimo(CreateView):
    template_name = "crud_emprestimo.html"
    model = Emprestimo
    form_class = CadastrarEmprestimoForm
    success_url = reverse_lazy("listar_emprestimo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Cadastrar"
        equipamentos_disponiveis = Equipamento.objects.filter(status="1")
        if not equipamentos_disponiveis:
            context["sem_equipamentos"] = True
        return context

    def form_valid(self, form):
        form.save(commit=False)
        equipamento = form.cleaned_data["equipamento"]
        equipamento.status = "0"
        equipamento.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["equipamento"].queryset = Equipamento.objects.filter(status="1")
        return form


@method_decorator(login_required, name="dispatch")
class EditarEmprestimo(UpdateView):
    template_name = "crud_emprestimo.html"
    model = Emprestimo
    fields = [
        "nome",
        "matricula",
        "curso",
        "equipamento",
        "data_emprestimo",
        "data_devolucao",
        "observacao",
    ]
    success_url = reverse_lazy("listar_emprestimo")

    def form_valid(self, form):
        emprestimo = form.instance
        if emprestimo.status_emprestimo == Emprestimo.EM_ANDAMENTO:
            emprestimo.status_emprestimo = Emprestimo.DEVOLVIDO
            emprestimo.equipamento.status = Equipamento.DISPOSICAO
            emprestimo.equipamento.save()
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class DeletarEmprestimo(DeleteView):
    model = Emprestimo
    template_name = "deletar_emprestimo.html"
    success_url = reverse_lazy("listar_emprestimo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Excluir"
        return context

@method_decorator(login_required, name="dispatch")
class DevolverEmprestimo(View):
    def post(self, request, emprestimo_id):
        emprestimo = get_object_or_404(Emprestimo, id_emprestimo=emprestimo_id)
        if emprestimo.status_emprestimo == Emprestimo.EM_ANDAMENTO:
            emprestimo.status_emprestimo = Emprestimo.DEVOLVIDO
            emprestimo.equipamento.status = Equipamento.DISPOSIÇÃO
            emprestimo.equipamento.save()
            emprestimo.save()
        return HttpResponseRedirect("listar_emprestimo")