from django.db.models import QuerySet

from .models import Cliente

# Lógica de negócios para obter queryset de clientes, considerando os parâmetros de listagem e atualização
# include_inactive: indica se a listagem deve incluir clientes inativos (usado para o parâmetro ?todos=1)
# for_partial_update: indica se a consulta é para um PATCH de atualização parcial, permitindo acessar clientes inativos para reativação
def get_clientes_queryset(*, include_inactive: bool, for_partial_update: bool) -> QuerySet[Cliente]:
    queryset = Cliente.objects.all()

    if for_partial_update or include_inactive:
        return queryset

    return queryset.filter(ativo=True)
