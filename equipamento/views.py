from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Equipamento
from django.db.models import Q


@method_decorator(login_required, name="dispatch")
class ListarEquipamento(ListView):
    template_name = "listar_equipamento.html"
    model = Equipamento
    context_object_name = "equipamentos"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search")
        status_filter = self.request.GET.get("status_filter")

        if search_query:
            queryset = queryset.filter(
                Q(nome__icontains=search_query) | Q(codigo__icontains=search_query)
            )
            queryset = queryset.order_by('-created_at')

        if status_filter == "disponivel":
            queryset = queryset.filter(status="1")
        elif status_filter == "indisponivel":
            queryset = queryset.filter(status="0")

        queryset = queryset.order_by('-created_at')
        return queryset


@method_decorator(login_required, name="dispatch")
class CadastrarEquipamento(CreateView):
    template_name = "novo_equipamento.html"
    model = Equipamento
    fields = ["nome", "patrimonio", "codigo", "situacao", "observacao", "status"]
    success_url = reverse_lazy("listar_equipamento")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Cadastrar"
        return context


@method_decorator(login_required, name="dispatch")
class EditarEquipamento(UpdateView):
    template_name = "edit_equipamento.html"
    model = Equipamento
    fields = ["nome", "patrimonio", "codigo", "situacao", "observacao", "status"]
    success_url = reverse_lazy("listar_equipamento")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.object.status != '1':
            form.fields["status"].required = False
            form.fields["status"].widget.attrs["disabled"] = True

        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar"
        return context


@method_decorator(login_required, name="dispatch")
class DeletarEquipamento(DeleteView):
    model = Equipamento
    template_name = "deletar_equipamento.html"
    success_url = reverse_lazy("listar_equipamento")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Excluir"
        return context
