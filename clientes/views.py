from django.shortcuts import get_object_or_404, redirect, render
from .models import Cliente

#substituindo o .all() por .filter(ativo=True) para retornar os ativos por padrao
def lista_clientes(request):
    #filtro opcional para mostrar todos os clientes (usabilidade: http://localhost:8000/clientes/?todos=1)
    mostrar_todos = request.GET.get("todos")

    if mostrar_todos == "1":
        clientes = Cliente.objects.all()
    else:
        clientes = Cliente.objects.filter(ativo=True)
    
    return render(request, "clientes/lista_clientes.html", {"clientes": clientes})

#Função para inativar um cliente apenas mudando o valor de cliente.ativo
def inativar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.ativo = False
    cliente.save(update_fields=["ativo"])
    return redirect("lista_clientes")

#Função para reativar um cliente apenas mudando o valor de cliente.ativo
def reativar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.ativo = True
    cliente.save(update_fields=["ativo"])
    return redirect("lista_clientes")