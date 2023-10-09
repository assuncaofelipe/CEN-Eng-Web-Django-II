from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def Home(request):
    return render(request, 'home.html')
    
@login_required
def ListarEquipamentos(request):
    return render(request, 'listar_equipamento.html')
